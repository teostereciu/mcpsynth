import glob
import re

endpoints = []
for file in glob.glob("docs/*.md"):
    with open(file, "r") as f:
        content = f.read()
        matches = re.findall(r"^(GET|POST|DELETE)\s+(/v1/[^\s]+)", content, re.MULTILINE)
        if matches:
            for match in matches:
                endpoints.append(f"{file}: {match[0]} {match[1]}")

with open("endpoints.txt", "w") as f:
    f.write("\n".join(endpoints))
