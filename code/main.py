from os import path

basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, '..', 'token.txt'))

with open(filepath, 'r') as f:
    TOKEN = f.read()

print(TOKEN)
