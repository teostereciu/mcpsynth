import os
for f in os.listdir("docs"):
    print(f, os.path.getsize(os.path.join("docs", f)))
