# rename_files.py
import os

# Rename all .txt files in a folder to add '_old'
for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        new_name = filename.replace('.txt', '_old.txt')
        os.rename(filename, new_name)
        print(f'Renamed: {filename} → {new_name}')
