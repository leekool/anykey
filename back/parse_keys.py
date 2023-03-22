import re
from pprint import pprint # for testing

key_dict = {
    '': ['XXXXXXX', 'KC_NO'],
    '_______': ['_______', 'KC_TRANSPARENT', 'KC_TRNS'],
    'ENTER': ['KC_ENTER', 'KC_ENT', 'KC_KP_ENTER', 'KC_PENT'],
    'ESCAPE': ['KC_ESCAPE', 'KC_ESC'],
    'BACKSPACE': ['KC_BACKSPACE', 'KC_BSPC'],
    'SPACE': ['KC_SPACE', 'KC_SPC'],
    '(': ['KC_LEFT_PAREN', 'KC_LPRN'],
    ')': ['KC_RIGHT_PAREN', 'KC_RPRN'],
    '[': ['KC_LEFT_BRACKET', 'KC_LBRC'],
    ']': ['KC_RIGHT_BRACKET', 'KC_RBRC'],
    '{': ['KC_LEFT_CURLY_BRACE', 'KC_LCBR'],
    '}': ['KC_RIGHT_CURLY_BRACE', 'KC_RCBR'],
    '-': ['KC_MINUS', 'KC_MINS', 'KC_KP_MINUS', 'KC_PMNS'],
    '=': ['KC_EQUAL', 'KC_EQL', 'KC_KP_EQUAL', 'KC_PEQL'],
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
    '~': ['KC_TILDE', 'KC_TILD'],
    '!': ['KC_EXCLAIM', 'KC_EXLM'],
    '@': ['KC_AT'],
    '#': ['KC_HASH', 'KC_NONUS_HASH', 'KC_NUHS'],
    '$': ['KC_DOLLAR', 'KC_DLR'],
    '%': ['KC_PERCENT', 'KC_PERC'],
    '^': ['KC_CIRCUMFLEX', 'KC_CIRC'],
    '&': ['KC_AMPERSAND', 'KC_AMPR'],
    '*': ['KC_ASTERISK', 'KC_ASTR', 'KC_KP_ASTERISK', 'KC_PAST'],
    '_': ['KC_UNDERSCORE', 'KC_UNDS'],
    '+': ['KC_PLUS', 'KC_UNDS', 'KC_KP_PLUS', 'KC_PPLS'],
    '|': ['KC_PIPE'],
    ':': ['KC_COLON', 'KC_COLN'],
    '\"': ['KC_DOUBLE_QUOTE', 'KC_DQUO', 'KC_DQT'],
    '<': ['KC_LEFT_ANGLE_BRACKET', 'KC_LABK', 'KC_LT'],
    '<': ['KC_RIGHT_ANGLE_BRACKET', 'KC_RABK', 'KC_GT'],
    '?': ['KC_QUESTION', 'KC_QUES'],
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

# todo: gathering layers and processing keys need to be separated
# into separte functions. at the moment they both happen at the
# same time in the same for loop

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

        # todo: refactor into switch handling function
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
