import re

class Layer:
    keys = []

    def __init__(self, name):
        self.name = name

    def push_key(self, key):
        self.keys.append(key)

    def return_layer(self):
        return {self.name: self.keys}

with open('testmap.c', 'r') as f:
    lines = f.readlines()

layers = []
current_layer = []

layer_open = False
flag = False

for line in lines:
    if line.strip().startswith('//'):
        continue

    if 'MATRIX' in line:
        flag = True

    if flag == False:
        continue

    if line.strip().startswith('['):
        layer_open = True
        current_layer = Layer(re.search(r'\[(.*?)\]', line).group(1))

    elif layer_open:
        line_keys = line.split(',')

        for key in line_keys:
            if '\n' in key:
                continue

            key = key.strip()
            current_layer.push_key(key)

    if ')' in line:
        layers.append(current_layer.return_layer())
        layer_open = False

    if flag and '};' in line:
        break

print(layers)
