import json
import uuid

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

    ## SVG Keycap dimensions
    kCap = KeyboardCap(10, 10, 60, 60, 0, 10, 10, 96, 96, 35, 35, 0, 60)

    with open('layout.svg', 'w') as file:
        # we add the x because an ID needs to start with a letter
        mapNameId = 'x' + uuid.uuid4().hex
        coords = getKeyboardCoords(mapPath)

        largest_x = max(coords, key=lambda x: x['x'])['x']
        largest_y = max(coords, key=lambda x: x['y'])['y']
        svg_w = ((largest_x) * kCap.coord_multiplier) + kCap.key_w
        svg_h = largest_y * kCap.coord_multiplier + (kCap.key_h * 2)
        key_text_layer_x = [2.75, 20, 20, 1.75, 1.75, 2.75]
        key_text_layer_y = [2.75, 5, 1.5, 1.6, 5, 1.2]
        key_text_layer_alignment = ['dominant-baseline="middle" text-anchor="middle"','','','dominant-baseline="right" text-anchor="right"', 'dominant-baseline="right" text-anchor="right"', 'dominant-baseline="middle" text-anchor="middle"']
        key_text_layer_cmyk = ['black','cyan','magenta','yellow', 'red', 'green']
        
        svg_string = '<svg viewBox="0 0 ' + str(svg_w) + ' ' + str(svg_h) + '" preserveAspectRatio="xMidYMid meet" version="1.1" xmlns="http://www.w3.org/2000/svg" id="{0}">'.format(
            mapNameId)
        svg_string += '<style>#' + mapNameId + ' {width:' + str(svg_w) + 'px; height:' + str(svg_h) + 'px;}'
        svg_string += """
                    rect {transform-origin: center; transform-box: fill-box;}'
                    text {transform-origin: center; transform-box: fill-box;}
                    .key-base {stroke: black; fill: #e3e3e3; stroke-width=1;}
                    .key-cap {stroke: #b5b5b5; fill: #ebebeb; stroke-width=0.5;}
                    .key-text {fill: black; pointer-events: none;}
                </style>"""
        svg_string += '<rect fill="transparent" />'

        firstLayer = fullLayout[0]
        for idx, key_cap in enumerate(firstLayer['keys']):
            determineKeyPositions(level, kCap, coords, idx, key_text_layer_x, key_text_layer_y, key_text_layer_alignment, 0)

            svg_string += '<rect class="key-base" width="{0}" height="{1}" transform="translate({2}, {3}) rotate({4})" rx="8" ry="8" />'.format(kCap.key_w, kCap.key_h, kCap.pos_x, kCap.pos_y, kCap.key_r)
            svg_string += '<rect class="key-cap" width="{0}" height="{1}" transform="translate({2}, {3}) rotate({4})" rx="3" ry="3" />'.format( kCap.inner_key_w, kCap.inner_key_h, kCap.inner_pos_x, kCap.inner_pos_y, kCap.key_r)

            resetKey(kCap)

        for index, layer in enumerate(fullLayout):
            for idx, key_cap in enumerate(layer['keys']):
                print_key = checkIfKeyOnPreviousLayerIsTheSame(key_cap, kCap, level, index, idx, fullLayout)
                determineKeyPositions(level, kCap, coords, idx, key_text_layer_x, key_text_layer_y, key_text_layer_alignment, index)
                fontSize = '12' if len(key_cap) > 2 else '14'
                if (print_key):
                    print('excluding:' + key_cap)
                    key_cap = ''
                svg_string += '<text class="key-text" {0} font-size="{1}" stroke="{2}" stroke-width="0.3" transform="translate({3}, {4}) rotate({5})">{6}</text>'.format(kCap.baseline_text, fontSize, key_text_layer_cmyk[index], kCap.key_text_x, kCap.key_text_y, kCap.key_text_r, key_cap)

                resetKey(kCap)

        svg_string += '</svg>'
        file.write(svg_string)

        return svg_string

def resetKey(kCap):
    kCap.key_h = 60
    kCap.key_w = 60
    kCap.key_r = 0
    kCap.key_text_r = 0

def determineKeyPositions(level, kCap, coords, idx, key_text_layer_x, key_text_layer_y, key_text_layer_alignment, index):
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
        kCap.baseline_text = ''
    else:
        kCap.key_text_x = kCap.inner_pos_x + kCap.key_w / key_text_layer_x[index]
        kCap.key_text_y = kCap.inner_pos_y + kCap.key_h / key_text_layer_y[index]
        kCap.key_text_r = kCap.key_r
        kCap.baseline_text = key_text_layer_alignment[index]

def checkIfKeyOnPreviousLayerIsTheSame(key_cap, kCap, level, index, idx, fullLayout):
    if (index > 0 and (key_cap == fullLayout[index - 1]['keys'][idx] or key_cap == "")):
        return True
    else:
        return False
