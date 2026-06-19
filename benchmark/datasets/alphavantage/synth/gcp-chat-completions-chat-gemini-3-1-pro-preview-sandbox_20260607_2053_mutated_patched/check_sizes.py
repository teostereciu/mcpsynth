import os
for f in os.listdir('docs'):
    path = os.path.join('docs', f)
    print(f"{f}: {os.path.getsize(path)}")
