import re

class Layer:
    def __init__(self, name):
        self.name = name
        self.keys = []

    def push_key(self, key):
        self.keys.append(key)

    def return_layer(self):
        return {'name': self.name, 'keys': self.keys}

layers = []
current_layer = None

with open('testmap.c', 'r') as f:
    lines = f.readlines()

flag = False

for line in lines:
    if line.strip().startswith('//'):
        continue

    if 'MATRIX' in line:
        flag = True

    if not flag:
        continue

    if line.strip().startswith('['):
        current_layer = Layer(re.search(r'\[(.*?)\]', line).group(1))
    elif current_layer:
        line_keys = line.split(',')

        for key in line_keys:
            invalid_keys = {'\n', '(', ')'}

            if any(x in key for x in invalid_keys):
                continue

            key = key.strip()
            current_layer.push_key(key)

    if ')' in line:
        layers.append(current_layer.return_layer())
        current_layer = None

    if flag and '};' in line:
        break

print(layers)
