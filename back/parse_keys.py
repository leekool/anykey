import re
from key_dict import get_dict
from pprint import pprint  # for testing

key_dict = get_dict()


class Layer:
    def __init__(self, name):
        self.name = name
        self.keys = []

    def return_layer(self):
        return {'name': self.name, 'keys': self.keys}


def parse_map(keymap):
    layers = []
    current_layer = None
    lines = keymap.readlines()
    flag = False

    # --- process layers ---
    for bline in lines:
        line = bline.decode('utf-8')
        if line.strip().startswith(('//', '/*', '*', '*/')):
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
            line_keys = filter(None, line.strip().split(','))

            # todo: refactor into switch handling function
            for switch_dirty in line_keys:
                invalid_keys = {'\n', '(', ')'}
                # if any(x in switch_dirty for x in invalid_keys):
                if switch_dirty in invalid_keys:
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
            if switch in key_dict:
                layer['keys'][switch_idx] = key_dict[switch]

            if 'KC_' in layer['keys'][switch_idx]:
                layer['keys'][switch_idx] = switch.replace('KC_', '')

    pprint(layers, sort_dicts=False)
    return layers
