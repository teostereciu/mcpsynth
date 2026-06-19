import glob
import os

with open('all_docs.txt', 'w') as out:
    for f in glob.glob('docs/*.md'):
        out.write(f"=== {f} ===\n")
        with open(f, 'r') as infile:
            out.write(infile.read()[:500])
            out.write("\n\n")
