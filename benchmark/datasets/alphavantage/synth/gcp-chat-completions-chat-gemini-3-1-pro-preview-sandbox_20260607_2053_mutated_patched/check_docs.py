import os

for f in os.listdir('docs'):
    path = os.path.join('docs', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(f"{f}: {len(content)} chars")
