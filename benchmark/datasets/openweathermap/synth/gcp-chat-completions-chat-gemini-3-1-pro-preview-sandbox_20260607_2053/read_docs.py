import os
for f in os.listdir('docs'):
    print(f"--- {f} ---")
    with open(os.path.join('docs', f)) as file:
        print(file.read()[:200])
