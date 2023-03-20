import re
from pprint import pprint # for testing

# key_dict = {
#     'XXXXXXX': '',
#     'KC_A': 'A',
#     'KC_B': 'B',
#     'KC_C': 'C',
#     'KC_D': 'D',
#     'KC_E': 'E',
#     'KC_F': 'F',
#     'KC_G': 'G',
#     'KC_H': 'H',
#     'KC_I': 'I',
#     'KC_J': 'J',
#     'KC_K': 'K',
#     'KC_L': 'L',
#     'KC_M': 'M',
#     'KC_N': 'N',
#     'KC_O': 'O',
#     'KC_P': 'P',
#     'KC_Q': 'Q',
#     'KC_R': 'R',
#     'KC_S': 'S',
#     'KC_T': 'T',
#     'KC_U': 'U',
#     'KC_V': 'V',
#     'KC_W': 'W',
#     'KC_X': 'X',
#     'KC_Y': 'Y',
#     'KC_Z': 'Z',
#     'KC_1': '1',
#     'KC_2': '2',
#     'KC_3': '3',
#     'KC_4': '4',
#     'KC_5': '5',
#     'KC_6': '6',
#     'KC_7': '7',
#     'KC_8': '8',
#     'KC_9': '9',
#     'KC_0': '0',
#     'KC_F1': 'F1',
#     'KC_F2': 'F2',
#     'KC_F3': 'F3',
#     'KC_F4': 'F4',
#     'KC_F5': 'F5',
#     'KC_F6': 'F6',
#     'KC_F7': 'F7',
#     'KC_F8': 'F8',
#     'KC_F9': 'F9',
#     'KC_F10': 'F10',
#     'KC_F11': 'F11',
#     'KC_F12': 'F12',
# }

class Layer:
    def __init__(self, name):
        self.name = name
        self.keys = []

    def return_layer(self):
        return {'name': self.name, 'keys': self.keys}

layers = []
current_layer = None

with open('./testmap.c', 'r') as f:
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
        layer_index = re.search(r'\[(.*?)\]', line).group(1)
        layer_num = int(layer_index)
        current_layer = Layer(layer_index)
    elif current_layer:
        line_keys = line.split(',')

        for key_index, key_dirty in enumerate(line_keys):
            invalid_keys = {'\n', '(', ')'}
            if any(x in key_dirty for x in invalid_keys):
                continue

            key = key_dirty.strip()

            # todo: handle layer names that aren't sequential numbers
            if any(x in key for x in {'KC_TRANSPARENT', 'KC_TRNS', '_______'}) and layer_num > 0:
                key = layers[layer_num - 1]['keys'][key_index]

            if 'KC_' in key:
                key = key.replace('KC_', '')

            current_layer.keys.append(key)

    if ')' in line:
        layers.append(current_layer.return_layer())
        current_layer = None

    if flag and '};' in line:
        break
pprint(layers, sort_dicts = False)
