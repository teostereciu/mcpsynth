import os
for f in os.listdir("docs"):
    if f.endswith(".md"):
        with open(os.path.join("docs", f)) as file:
            content = file.read()
            if "TASK.md" not in content:
                print(f, len(content))
