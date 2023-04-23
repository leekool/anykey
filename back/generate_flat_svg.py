import json

class KeyboardCap:
    def __init__(self, pos_x, pos_y, key_h, key_w, key_r, inner_pos_x, inner_pos_y, inner_key_h, inner_key_w, key_text_x, key_text_y, key_text_r, coord_multiplier):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.key_h = key_h
        self.key_w = key_w
        self.key_r = key_r
        self.inner_pos_x = inner_pos_x
        self.inner_pos_y = inner_pos_y
        self.inner_key_h = inner_key_h
        self.inner_key_w = inner_key_w
        self.key_text_x = key_text_x
        self.key_text_y = key_text_y
        self.key_text_r = key_text_r
        self.coord_multiplier = coord_multiplier


def getKeyboardCoords(mapPath):
    with open(mapPath, 'r') as j:
        contents = json.loads(j.read())
        print(next(iter(contents['layouts'])))
        return contents['layouts'][next(iter(contents['layouts']))]['layout']

def get_flat_keymap_svg(mapPath, fullLayout):

    level = 10
    svg_w = 0
    svg_h = 0

    kCap = KeyboardCap(10, 10, 60, 60, 0, 10, 10, 96, 96, 35, 35, 0, 60)

    with open('layout.svg', 'w') as file:
        coords = getKeyboardCoords(mapPath)

        largest_x = max(coords, key=lambda x: x['x'])['x']
        largest_y = max(coords, key=lambda x: x['y'])['y']
        svg_w = ((largest_x) * kCap.coord_multiplier) + kCap.key_w
        svg_h = largest_y * kCap.coord_multiplier + (kCap.key_h * 2)
        key_text_layer_x = [20, 20, 20, 20]
        key_text_layer_y = [5, 2.4, 1.5, 5]
        
        svg_string = '<svg version="1.1" xmlns="http://www.w3.org/2000/svg">'

        svg_string += '<style>svg {width:' + str(svg_w) + 'px; height:' + str(svg_h) + 'px;}'
        svg_string += """
                    rect {transform-origin: center; transform-box: fill-box;}'
                    text {transform-origin: center; transform-box: fill-box;}
                    .key-base {stroke: black; fill: #C3C3C3; stroke-width=1;}
                    .key-cap {stroke: #BFBBBB; fill: white; stroke-width=1;}
                    .key-text {fill=black; pointer-events: none;}
                </style>"""
        svg_string += '<rect fill="transparent" />'

        firstLayer = fullLayout[0]
        for idx, key_cap in enumerate(firstLayer['keys']):
            determineKeyPositions(level, kCap, coords, idx, key_text_layer_x, key_text_layer_y, 0)

            svg_string += '<rect class="key-base" width="{0}" height="{1}" transform="translate({2}, {3}) rotate({4})" rx="8" ry="8" />'.format(kCap.key_w, kCap.key_h, kCap.pos_x, kCap.pos_y, kCap.key_r)
            svg_string += '<rect class="key-cap" width="{0}" height="{1}" transform="translate({2}, {3}) rotate({4})" rx="3" ry="3" />'.format( kCap.inner_key_w, kCap.inner_key_h, kCap.inner_pos_x, kCap.inner_pos_y, kCap.key_r)

            resetKey(kCap)

        for index, layer in enumerate(fullLayout):
            for idx, key_cap in enumerate(layer['keys']):
                determineKeyPositions(level, kCap, coords, idx, key_text_layer_x, key_text_layer_y, index)

                svg_string += '<text class="key-text" transform="translate({0}, {1}) rotate({2})">{3}</text>'.format(kCap.key_text_x, kCap.key_text_y, kCap.key_text_r, key_cap)

                resetKey(kCap)

        svg_string += '</svg>'
        file.write(svg_string)

        return svg_string

def resetKey(kCap):
    kCap.key_h = 60
    kCap.key_w = 60
    kCap.key_r = 0
    kCap.key_text_r = 0

def determineKeyPositions(level, kCap, coords, idx, key_text_layer_x, key_text_layer_y, index):
    kCap.pos_x = coords[idx]['x'] * kCap.coord_multiplier
    kCap.pos_y = level + coords[idx]['y'] * kCap.coord_multiplier
    if 'h' in coords[idx]:
        kCap.key_h = coords[idx]['h'] * kCap.coord_multiplier
    if 'w' in coords[idx]:
        kCap.key_w = coords[idx]['w'] * kCap.coord_multiplier
    if 'r' in coords[idx]:
        kCap.key_r = coords[idx]['r']

    kCap.inner_key_h = kCap.key_h * 0.75
    kCap.inner_key_w = kCap.key_w * 0.75
    kCap.inner_pos_x = kCap.pos_x + kCap.key_w / 8
    kCap.inner_pos_y = kCap.pos_y + kCap.key_h / 18
    if (kCap.key_r != 0):
        negative = str(kCap.key_r).find("-") != -1
        kCap.key_text_r = kCap.key_r + 90 if negative else kCap.key_r - 90
        kCap.key_text_x = kCap.inner_pos_x + kCap.key_w / 8 if negative else kCap.inner_pos_x + kCap.key_w / 5
        kCap.key_text_y = kCap.inner_pos_y + kCap.key_h / 5 if negative else kCap.inner_pos_y + kCap.key_w / 1
    else:
        kCap.key_text_x = kCap.inner_pos_x + kCap.key_w / key_text_layer_x[index]
        kCap.key_text_y = kCap.inner_pos_y + kCap.key_h / key_text_layer_y[index]
        kCap.key_text_r = kCap.key_r
