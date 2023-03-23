import re
from pprint import pprint # for testing

# todo: separate key_dict into separate file
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
    'NUM LOCK': ['KC_NUM_LOCK', 'KC_NUM'],
    # arrow keys
    'RIGHT': ['KC_RIGHT'],
    'LEFT': ['KC_LEFT'],
    'DOWN': ['KC_DOWN'],
    'UP': ['KC_UP'],
    # mouse keys
    'MOUSE RIGHT': ['KC_MS_RIGHT', 'KC_MS_R'],
    'MOUSE LEFT': ['KC_MS_LEFT', 'KC_MS_L'],
    'MOUSE DOWN': ['KC_MS_DOWN', 'KC_MS_D'],
    'MOUSE UP': ['KC_MS_UP', 'KC_MS_U'],
    'MWHEEL RIGHT': ['KC_MS_WH_RIGHT', 'KC_WH_R'],
    'MWHEEL LEFT': ['KC_MS_WH_LEFT', 'KC_WH_L'],
    'MWHEEL DOWN': ['KC_MS_WH_DOWN', 'KC_WH_D'],
    'MWHEEL UP': ['KC_MS_WH_UP', 'KC_WH_U'],
    'LEFT CLICK': ['KC_MS_BTN1', 'KC_BTN1'],
    'RIGHT CLICK': ['KC_MS_BTN2', 'KC_BTN2'],
    'MIDDLE CLICK': ['KC_MS_BTN3', 'KC_BTN3'],
    # symbols
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
    '>': ['KC_RIGHT_ANGLE_BRACKET', 'KC_RABK', 'KC_GT'],
    '?': ['KC_QUESTION', 'KC_QUES'],
    # modifiers - possibly separate left & right later
    'CTRL': ['KC_LEFT_CTRL', 'KC_LCTL', 'KC_RIGHT_CTRL', 'KC_RCTL'],
    'ALT': ['KC_LEFT_ALT', 'KC_LALT', 'KC_LOPT', 'KC_RIGHT_ALT', 'KC_RALT', 'KC_ROPT', 'KC_ALGR'],
    'SHIFT': ['KC_LEFT_SHIFT', 'KC_LSFT', 'KC_RIGHT_SHIFT', 'KC_RSFT'],
    'GUI': ['KC_LEFT_GUI', 'KC_LGUI', 'KC_LCMD', 'KC_LWIN', 'KC_RIGHT_GUI', 'KC_RGUI', 'KC_RCMD', 'KC_RWIN'],
    # -----
    'POWER': ['KC_SYSTEM_POWER', 'KC_PWR'],
    'SLEEP': ['KC_SYSTEM_SLEEP', 'KC_SLEP'],
    'WAKE': ['KC_SYSTEM_WAKE', 'KC_WAKE'],
    'MUTE': ['KC_AUDIO_MUTE', 'KC_MUTE'],
    'VOL +': ['KC_AUDIO_VOL_UP', 'KC_VOLU'],
    'VOL -': ['KC_AUDIO_VOL_DOWN', 'KC_VOLD'],
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

# --- process layers ---
for line in lines:
    if line.strip().startswith('//'):
        continue

    if 'MATRIX' in line:
        flag = True

    if not flag:
        continue

    if line.strip().startswith('['):
        layer_name = re.search(r'\[(.*?)\]', line).group(1)
        current_layer = Layer(layer_name)
    elif current_layer:
        # split line into list of keys
        line_keys = line.split(',')

        # todo: refactor into switch handling function
        for switch_dirty in line_keys:
            invalid_keys = {'\n', '(', ')'}
            if any(x in switch_dirty for x in invalid_keys):
                continue

            switch = switch_dirty.strip()

            current_layer.keys.append(switch)

    if ')' in line:
        layers.append(current_layer.return_layer())
        current_layer = None

    if flag and '};' in line:
        break

# --- process switches ---
for layer_idx, layer in enumerate(layers):
    for switch_idx, switch in enumerate(layer['keys']):
        if any(x in switch for x in {'KC_TRANSPARENT', 'KC_TRNS', '_______'}) and layer_idx > 0:
            layer['keys'][switch_idx] = layers[layer_idx - 1]['keys'][switch_idx]
            continue

        # check if switch's value matches any key in inverted_key_dict
        # if it does, switch becomes that key
        if switch in inverted_key_dict:
            layer['keys'][switch_idx] = inverted_key_dict[switch]

        if 'KC_' in layer['keys'][switch_idx]:
            layer['keys'][switch_idx] = switch.replace('KC_', '')

pprint(layers, sort_dicts = False)
