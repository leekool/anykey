import json

class KeyboardCap:
    def __init__(self, pos_x, pos_y, key_h, key_w, key_r, inner_pos_x, inner_pos_y, inner_key_h, inner_key_w, key_text_x, key_text_y, key_text_r, coord_multiplier, baseline_text):
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
        self.baseline_text = baseline_text

def getKeyboardCoords(mapPath):
    with open(mapPath, 'r') as j:
        contents = json.loads(j.read())
        print(next(iter(contents['layouts'])))
        return contents['layouts'][next(iter(contents['layouts']))]['layout']

def get_keymap_svg(mapPath, fullLayout):

    level = 10
    svg_w = 0
    svg_h = 0
    coord_multiplier = 60

    kCap = KeyboardCap(10, 10, 60, 60, 0, 10, 10, 96, 96, 35, 35, 0, 60, '')

    with open('layout.svg', 'w') as file:
        print('mapPath')
        print(mapPath)
        mapNameId = mapPath[mapPath.rfind('\\') + 1:mapPath.rfind('.')]
        coords = getKeyboardCoords(mapPath)

        largest_x = max(coords, key=lambda x: x['x'])['x']
        largest_y = max(coords, key=lambda x: x['y'])['y']
        svg_w = ((largest_x) * coord_multiplier) + kCap.key_w

        step1 = largest_y * coord_multiplier
        step2 = step1 + kCap.key_h
        step3 = step2 * len(fullLayout)
        svg_h = step3 + kCap.key_h * len(fullLayout)

        
        svg_string = '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" id="{0}">'.format(mapNameId)
        svg_string += '<style>#' + mapNameId + ' {width:' + str(svg_w) + 'px; height:' + str(svg_h) + 'px;}'
        svg_string += """
                    rect {transform-origin: center; transform-box: fill-box;}'
                    text {transform-origin: center; transform-box: fill-box;}
                    .key-base {stroke: black; fill: #E0CFB3; stroke-width=1;}
                    .key-cap {stroke: #9E9483; fill: #E1D6C3; stroke-width=0.5;}
                    .key-text {fill=black; pointer-events: none;}
                </style>"""
        svg_string += '<rect fill="transparent" />'

        for index, layer in enumerate(fullLayout):
            for idx, key_cap in enumerate(layer['keys']):
                determineKeyPosition(level, coord_multiplier, kCap, coords, idx)

                svg_string += '<rect class="key-base" fill="url(#RadialGradient1)" width="{0}" height="{1}" transform="translate({2}, {3}) rotate({4})" rx="8" ry="8" />'.format(kCap.key_w, kCap.key_h, kCap.pos_x, kCap.pos_y, kCap.key_r)
                svg_string += '<rect class="key-cap" width="{0}" height="{1}" transform="translate({2}, {3}) rotate({4})" rx="3" ry="3" />'.format(kCap.inner_key_w, kCap.inner_key_h, kCap.inner_pos_x, kCap.inner_pos_y, kCap.key_r)
                svg_string += '<text class="key-text" {0} transform="translate({1}, {2}) rotate({3})">{4}</text>'.format(kCap.baseline_text, kCap.key_text_x, kCap.key_text_y, kCap.key_text_r, key_cap)

                kCap.key_h = 60
                kCap.key_w = 60
                kCap.key_r = 0
                kCap.key_text_r = 0
            level = kCap.pos_y + 100
        svg_string += '</svg>'
        file.write(svg_string)

        return svg_string

def determineKeyPosition(level, coord_multiplier, kCap, coords, idx):
    kCap.pos_x = coords[idx]['x'] * coord_multiplier
    kCap.pos_y = level + coords[idx]['y'] * coord_multiplier
    if 'h' in coords[idx]:
        kCap.key_h = coords[idx]['h'] * coord_multiplier
    if 'w' in coords[idx]:
        kCap.key_w = coords[idx]['w'] * coord_multiplier
    if 'r' in coords[idx]:
        kCap.key_r = coords[idx]['r']

    kCap.inner_key_h = kCap.key_h * 0.75
    kCap.inner_key_w = kCap.key_w * 0.75
    if (kCap.key_r != 0):
        kCap.inner_pos_x = kCap.pos_x + kCap.key_w / 10
        kCap.inner_pos_y = kCap.pos_y + kCap.key_h / 10
        negative = str(kCap.key_r).find("-") != -1
        kCap.key_text_r = kCap.key_r + 90 if negative else kCap.key_r - 90
        kCap.key_text_x = kCap.inner_pos_x + kCap.key_w / 8 if negative else kCap.inner_pos_x + kCap.key_w / 5
        kCap.key_text_y = kCap.inner_pos_y + kCap.key_h / 5 if negative else kCap.inner_pos_y + kCap.key_w / 1
        kCap.baseline_text = ''
    else:
        kCap.inner_pos_x = kCap.pos_x + kCap.key_w / 8
        kCap.inner_pos_y = kCap.pos_y + kCap.key_h / 18
        kCap.key_text_x = kCap.inner_pos_x + kCap.inner_key_w / 2
        kCap.key_text_y = kCap.inner_pos_y + kCap.inner_key_h / 2
        kCap.key_text_r = kCap.key_r
        kCap.baseline_text = 'dominant-baseline="middle" text-anchor="middle"'
