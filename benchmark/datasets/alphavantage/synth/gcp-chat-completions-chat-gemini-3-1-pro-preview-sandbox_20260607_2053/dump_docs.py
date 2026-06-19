import os
import json

docs = {}
for filename in os.listdir("docs"):
    if filename.endswith(".md"):
        with open(os.path.join("docs", filename), "r") as f:
            docs[filename] = f.read()

with open("all_docs.json", "w") as f:
    json.dump(docs, f)
