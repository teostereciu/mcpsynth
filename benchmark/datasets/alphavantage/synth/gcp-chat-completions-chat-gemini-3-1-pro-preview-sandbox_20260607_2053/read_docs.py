import os
for f in os.listdir('docs'):
    with open(os.path.join('docs', f)) as file:
        print(f"--- {f} ---")
        print(file.read()[:100])
