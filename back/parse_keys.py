import re
from pprint import pprint # for testing

key_dict = {
    '': ['XXXXXXX', 'KC_NO'],
    '_______': ['_______', 'KC_TRANSPARENT', 'KC_TRNS'],
    'ENTER': ['KC_ENTER', 'KC_ENT', 'KC_KP_ENTER', 'KC_PENT'],
    'ESCAPE': ['KC_ESCAPE', 'KC_ESC'],
    'BACKSPACE': ['KC_BACKSPACE', 'KC_BSPC'],
    'SPACE': ['KC_SPACE', 'KC_SPC'],
    '-': ['KC_MINUS', 'KC_MINS', 'KC_KP_MINUS', 'KC_PMNS'],
    '=': ['KC_EQUAL', 'KC_EQL', 'KC_KP_EQUAL', 'KC_PEQL'],
    '[': ['KC_LEFT_BRACKET', 'KC_LBRC'],
    ']': ['KC_RIGHT_BRACKET', 'KC_RBRC'],
    '\\': ['KC_BACKSLASH', 'KC_BSLS'],
    ';': ['KC_SEMICOLON', 'KC_SCLN'],
    '\'': ['KC_QUOTE', 'KC_QUOT'],
    '`': ['KC_GRAVE', 'KC_GRV'],
    ',': ['KC_COMMA', 'KC_COMM', 'KC_KP_COMMA', 'KC_PCMM'],
    '.': ['KC_DOT', 'KC_KP_DOT', 'KC_KP_DOT', 'KC_PDOT'],
    '/': ['KC_SLASH', 'KC_SLSH', 'KC_KP_SLASH', 'KC_PSLS'],
    'CAPS': ['KC_CAPS_LOCK', 'KC_CAPS'],
    'PRINT SCREEN': ['KC_PRINT_SCREEN', 'KC_PSCR'],
    'PAUSE': ['KC_PAUSE', 'KC_PAUS', 'KC_BRK', 'KC_BRMU'],
    'INSERT': ['KC_INSERT', 'KC_INS'],
    'HOME': ['KC_HOME'],
    'PAGE UP': ['KC_PAGE_UP', 'KC_PGUP'],
    'PAGE DOWN': ['KC_PAGE_DOWN', 'KC_PGDN'],
    'END': ['KC_END'],
    'DELETE': ['KC_DELETE', 'KC_DEL'],
    # arrow keys
    'RIGHT': ['KC_RIGHT'],
    'LEFT': ['KC_LEFT'],
    'DOWN': ['KC_DOWN'],
    'UP': ['KC_UP'],
    # -----
    'NUM LOCK': ['KC_NUM_LOCK', 'KC_NUM'],
}

# creates a new dict containing individual key/value pairs for each item in key_dict's keys
inverted_key_dict = {value: key for key, values in key_dict.items() for value in values}

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

        for switch_index, switch_dirty in enumerate(line_keys):
            invalid_keys = {'\n', '(', ')'}
            if any(x in switch_dirty for x in invalid_keys):
                continue

            switch = switch_dirty.strip()

            # todo: handle layer names that aren't sequential numbers
            if any(x in switch for x in {'KC_TRANSPARENT', 'KC_TRNS', '_______'}) and layer_num > 0:
                switch = layers[layer_num - 1]['keys'][switch_index]

            # check if switch's value matches any key in inverted_key_dict
            # if it does, switch becomes that key
            if switch in inverted_key_dict:
                switch = inverted_key_dict[switch]

            if 'KC_' in switch:
                switch = switch.replace('KC_', '')

            current_layer.keys.append(switch)

    if ')' in line:
        layers.append(current_layer.return_layer())
        current_layer = None

    if flag and '};' in line:
        break

pprint(layers, sort_dicts = False)
