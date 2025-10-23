import os

# Rename all .txt files in the current folder to add '_old'
for filename in os.listdir('.'):
    name, ext = os.path.splitext(filename)
    if ext == '.txt':
        new_name = f'{name}_old{ext}'
        os.rename(filename, new_name)
        print(f'Renamed: {filename} → {new_name}')
