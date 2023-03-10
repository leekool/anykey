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

found_opening_bracket = False

flag = False

for line in lines:
    if line.strip().startswith('//'):
        continue

    if 'MATRIX' in line:
        flag = True

    if flag == False:
        continue

    if line.strip().startswith('['):
        found_opening_bracket = True
        current_layer = Layer(re.search(r'\[(.*?)\]', line).group(1))

    elif found_opening_bracket:
        current_layer.push_key(line)

    if ')' in line:
        layers.append(current_layer.return_layer())
        found_opening_bracket = False

    if flag and '};' in line:
        break

print(results)
