import os

TARGET = os.getcwd()

for root, dirs, files in os.walk(TARGET):
    for filename in files:
        # read file content
        with open(os.path.join(root, filename)) as f:
            content = f.read()
        # replace tag by install path
        content = content.replace('$((CWD))', TARGET)
        # replace file content
        with open(os.path.join(root, filename), 'w') as f:
            f.write(content)