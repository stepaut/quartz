import os
import shutil
from pathlib import Path
import regex as re

source = os.getcwd()
pattern = re.compile(r'\[([^][]+)\](\(((?:[^()]+|(?2))+)\))')

def check_file(path, file):
    full_path = os.path.join(path, file)

    data = ""
    
    with open(full_path, 'r', encoding='utf-8') as f:
        data = f.read()
        print(full_path)

        for match in pattern.finditer(data):
            description, _, url = match.groups()
            finded = match.group()
            print(f"{description}: {url}")
            data = data.replace(finded, f"[[{description}]]")

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(data)


for path, dir_folder, files in os.walk(source):
    for file in files:
        if file.endswith(".md"):
            check_file(path, file)
