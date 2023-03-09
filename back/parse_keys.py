import re

# keys = []

# # class Keymap:
# #     def __init__(self, *layers):
# #         for layer in layers:
# #             name, keys = layer
# #             setattr(self, name, keys)

class Layer:
    keys = []

    def __init__(self, name):
        self.name = name

    def push_key(self, key):
        self.keys.append(key)

    def return_layer(self):
        return {self.name: self.keys}

# with open("testmap.c", "r") as f:
#     flag = False
#     for line in f:
#         if line.strip().startswith('//'):
#             continue
#         if "MATRIX" in line:
#             flag = True
#         if flag and line.strip().startswith('['):
#             layer_name = re.search(r'\[(.*?)\]', line).group(1)
#             print(layer_name)
#         # if flag:
#         #     print(line)
#         if flag and "};" in line:
#             break

# f.close()

with open('testmap.c', 'r') as f:
    lines = f.readlines()

results = []
found_opening_bracket = False
current_result = []
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
        current_result = Layer(re.search(r'\[(.*?)\]', line).group(1))

    elif found_opening_bracket:
        current_result.push_key(line)

    if ')' in line:
        results.append(current_result.return_layer())
        found_opening_bracket = False

    if flag and '};' in line:
        break

# Append the final result after we have finished iterating over all the lines

print(results)
