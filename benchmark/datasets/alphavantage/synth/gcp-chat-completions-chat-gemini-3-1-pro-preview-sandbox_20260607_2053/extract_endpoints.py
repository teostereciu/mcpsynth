import os
import glob
import re
import json

endpoints = {}
for file in glob.glob("docs/*.md"):
    with open(file, "r") as f:
        content = f.read()
        # Find all lines starting with #### 
        matches = re.findall(r'^#### (.*)', content, re.MULTILINE)
        endpoints[file] = matches

with open("endpoints.json", "w") as f:
    json.dump(endpoints, f, indent=2)
