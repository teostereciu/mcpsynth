"""
Qwen 3.5 Model Hosting via vLLM on Krylov H100 Nodes
=====================================================

Hosts Qwen 3.5 models as an OpenAI-compatible API using vLLM on Krylov H100 nodes.

Models supported:
    qwen3p5-9b        — Qwen3.5-9B       (1× H100, dense,  ~18 GB bf16)
    qwen3p5-27b       — Qwen3.5-27B      (1× H100, dense,  ~54 GB bf16)
    qwen3p5-35b-a3b   — Qwen3.5-35B-A3B  (2× H100, MoE,    ~70 GB bf16)

Prerequisites:
    1. Model weights downloaded to /mnt/cii/tstereciu/models/
    2. Docker image: hub.tess.io/cii/llm-hosting-vllm:v4
       (required for Qwen3.5/Qwen3.6 — has qwen3_5_moe architecture support)
    3. pykrylov installed and account configured

IMPORTANT — Thinking mode:
    Qwen3.5 models default to "thinking mode" (chain-of-thought reasoning).
    For structured-output tasks (e.g., JSON generation), disable it at inference time:
        extra_body={"chat_template_kwargs": {"enable_thinking": False}}
    NOTE: Qwen3.5 uses "enable_thinking", NOT "thinking" (used by Qwen3-VL).

Usage:
    # Submit a single model to Krylov
    python serve_qwen_h100.py --model qwen3p5-9b

    # Submit all models (one Krylov job each)
    python serve_qwen_h100.py --model all

    # Run directly on this node for local testing (blocks until killed)
    python serve_qwen_h100.py --model qwen3p5-9b --local

After each job starts, grab the node IP from the logs and use the API:
    curl http://<NODE_IP>:8011/v1/models

Inference example (OpenAI-compatible):
    from openai import OpenAI
    client = OpenAI(api_key="EMPTY", base_url="http://<HOST>:<PORT>/v1")
    response = client.chat.completions.create(
        model="qwen3p5_9b",
        messages=[{"role": "user", "content": "Rewrite this title: ..."}],
        extra_body={"chat_template_kwargs": {"enable_thinking": False}},
    )
    print(response.choices[0].message.content)
"""

import os
import pykrylov
import argis parse
import random


# =========================
# CONFIGURATION
# =========================

ACCOUNT       = "tstereciu"
DOCKER_IMAGE  = "hub.tess.io/cii/llm-hosting-vllm:v4"

# If you have model weights already on a mounted volume, set this to the local
# path and update model_path entries below to use it, then re-add mount_pvc()
# in submit_krylov_job. Otherwise, vLLM downloads from HuggingFace at job start.
# HF_TOKEN is only needed for gated models; Qwen3.5 is public.
HF_TOKEN = os.environ.get("HF_TOKEN", "")

# Set to the path of your CUDA compat libraries if the H100 nodes need a shim
# (check with the cluster admin). Set to None to skip.
CUDA_COMPAT_PATH = None


# =========================
# MODEL CONFIGURATIONS
# =========================
# model_path entries are HuggingFace repo IDs — vLLM downloads and caches them.
# H100 SXM5 has 80 GB HBM3 each.
# max_model_len is set conservatively to leave headroom for KV cache.

HOSTING_CONFIGS = {
    "qwen3p5-9b": {
        "model_path":         "Qwen/Qwen3.5-9B",
        "served_model_name":  "qwen3p5_9b",
        "port":               8011,
        "n_gpus":             1,
        "max_model_len":      32768,
        "max_num_seqs":       4,
    },
    "qwen3p5-27b": {
        "model_path":         "Qwen/Qwen3.5-27B",
        "served_model_name":  "qwen3p5_27b",
        "port":               8012,
        "n_gpus":             1,       # fits on 1× H100 (unlike A100 which needed 2)
        "max_model_len":      32768,
        "max_num_seqs":       2,
    },
    "qwen3p5-35b-a3b": {
        "model_path":         "Qwen/Qwen3.5-35B-A3B",
        "served_model_name":  "qwen3p5_35b_a3b",
        "port":               8013,
        "n_gpus":             2,
        "max_model_len":      65536,   # MoE: small active footprint → extra headroom
        "max_num_seqs":       4,
    },
}


# =========================
# VLLM COMMAND BUILDER
# =========================

def build_vllm_cmd(cfg):
    cuda_compat_block = ""
    if CUDA_COMPAT_PATH:
        cuda_compat_block = f"""
        export VLLM_ENABLE_CUDA_COMPATIBILITY=1
        export VLLM_CUDA_COMPATIBILITY_PATH="{CUDA_COMPAT_PATH}"
        export LD_LIBRARY_PATH="{CUDA_COMPAT_PATH}:$LD_LIBRARY_PATH"
        """

    return f"""
        bash -lc '
        set -euxo pipefail

        export VLLM_HOST=0.0.0.0
        export VLLM_PORT={cfg["port"]}
        export HF_TOKEN="{HF_TOKEN}"
        export HF_HOME=/tmp/hf_cache   # ephemeral per-job cache; models re-download each run
        {cuda_compat_block}

        echo "Node: $(hostname) / $(hostname -I | awk \"{{print \\$1}}\")"

        vllm serve {cfg["model_path"]} \\
            --tensor-parallel-size {cfg["n_gpus"]} \\
            --trust-remote-code \\
            --served-model-name {cfg["served_model_name"]} \\
            --max-model-len {cfg["max_model_len"]} \\
            --gpu-memory-utilization 0.85 \\
            --enable-prefix-caching \\
            --host $VLLM_HOST \\
            --port $VLLM_PORT \\
            --max-num-batched-tokens {cfg["max_model_len"]} \\
            --max-num-seqs {cfg["max_num_seqs"]}
        '
    """


# =========================
# KRYLOV TASK ENTRYPOINT
# =========================

def serve_model(cfg):
    import os
    import ast
    import socket

    if isinstance(cfg, str):
        cfg = ast.literal_eval(cfg)

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(f"Node IP : {ip}")
    print(f"Serving : {cfg['served_model_name']}  port={cfg['port']}")
    print(f"Model   : {cfg['model_path']}")

    os.system(build_vllm_cmd(cfg))


# =========================
# KRYLOV JOB SUBMISSION
# =========================

def submit_krylov_job(cfg, namespace, project_name):
    name = cfg["served_model_name"]
    rand = random.randint(100, 999)

    task = pykrylov.Task(
        serve_model,
        [cfg],
        docker_image=DOCKER_IMAGE,
    )
    task.add_cpu(36)
    task.add_memory(360)
    task.run_on_gpu(quantity=cfg["n_gpus"], model="h100")
    # No mount_pvc needed — models download from HuggingFace at job start.
    # If you later want to use pre-downloaded weights, add:
    #   task.mount_pvc("<namespace>", "<pvc-name>", "<cluster>")
    # and update model_path entries back to local paths.

    session = pykrylov.Session(
        namespace=namespace,
        project_name=project_name,
        job_name=f"serve_{name}_{rand}",
    )

    workflow = pykrylov.Flow(task)
    workflow.execution_parameters.add_execution_parameter("enableChooseCluster", "true")

    exp_id = session.submit_experiment(
        workflow,
        project=project_name,
        experiment_name=f"serve_{name}",
        overwrite_artifact=True,
        email_on=False,
    )

    run_id = (
        pykrylov.ems.show_experiment(exp_id)
        .get("runtime", {})
        .get("workflow", {})
        .get("runId")
    )

    print(f"\n[{name}]")
    print(f"  Run ID : {run_id}")
    print(f"  Port   : {cfg['port']}")
    print(f"  Work   : {session.get_work_directory()}")
    print(f"  → Once running: curl http://<NODE_IP>:{cfg['port']}/v1/models")


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    pykrylov.util.use_account(account_name=ACCOUNT, yubikey_required=False)

    parser = argparse.ArgumentParser(description="Host Qwen3.5 models via vLLM on Krylov H100 nodes")
    parser.add_argument(
        "--model", required=True,
        choices=list(HOSTING_CONFIGS.keys()) + ["all"],
        help="Model alias to host, or 'all' to submit all jobs",
    )
    parser.add_argument("--namespace",    default="ebay-lvs-h100")
    parser.add_argument("--project_name", default="")
    parser.add_argument(
        "--local", action="store_true",
        help="Run vllm serve directly on this machine (for testing; blocks until killed)",
    )
    args = parser.parse_args()

    models_to_run = (
        list(HOSTING_CONFIGS.values())
        if args.model == "all"
        else [HOSTING_CONFIGS[args.model]]
    )

    if args.local:
        if len(models_to_run) > 1:
            raise ValueError("--local only supports one model at a time.")
        serve_model(models_to_run[0])
    else:
        print(f"Namespace : {args.namespace}")
        print(f"Project   : {args.project_name}")
        print(f"Submitting {len(models_to_run)} job(s)...\n")
        for cfg in models_to_run:
            submit_krylov_job(cfg, namespace=args.namespace, project_name=args.project_name)
