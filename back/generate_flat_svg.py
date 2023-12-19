import json
import uuid
import requests
import svg

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

def getKeyboardCoords(keyboardName):
    response = requests.get(f"https://keyboards.qmk.fm/v1/keyboards/" + keyboardName + "/info.json")
    keyboardJson = json.loads(response.content)
    layoutName = next(iter(keyboardJson['keyboards'][keyboardName]['layouts']))
    return keyboardJson['keyboards'][keyboardName]['layouts'][layoutName]['layout']

def get_flat_keymap_svg(keyboardName, fullLayout):

    level = 10
    svg_w = 0
    svg_h = 0

    # SVG Keycap dimensions
    kCap = KeyboardCap(10, 10, 60, 60, 0, 10, 10, 96, 96, 35, 35, 0, 60)

    # we add the x because an ID needs to start with a letter
    mapNameId = 'x' + uuid.uuid4().hex
    coords = getKeyboardCoords(keyboardName)

    largest_x = max(coords, key=lambda x: x['x'])['x']
    largest_y = max(coords, key=lambda x: x['y'])['y']
    svg_w = (largest_x * kCap.coord_multiplier) + kCap.key_w
    svg_h = largest_y * kCap.coord_multiplier + (kCap.key_h * 2)

    # Layer changes for up to 6 layers
    key_text_layer_x = [2.75, 20, 20, 1.5, 1.5, 2.75]
    key_text_layer_y = [2.75, 5, 1.5, 1.6, 5, 1.2]
    key_text_layer_cmyk = ['black', 'cyan', 'magenta', 'yellow', 'red', 'green']
    key_text_layer_alignment = [
            'middle',  # black
            'start',   # cyan
            '',        # magenta
            'start',   # yellow
            'start',   # red
            'middle'   # green
    ]
    key_text_layer_anchor = [
            'middle',  # black
            '',        # cyan
            '',        # magenta
            'end',     # yellow
            'end',     # red
            'middle'   # green
    ]

    canvas = svg.SVG(style='transform-origin: center; transform-box: fill-box;', preserveAspectRatio = 'xMidYMin meet', width = svg_w, height = svg_h, id = mapNameId, viewBox= svg.ViewBoxSpec(0, 0, svg_w, svg_h))
    elements = []

    firstLayer = fullLayout[0]
    for idx, key_cap in enumerate(firstLayer['keys']):
        determineKeyPositions(level, kCap, coords, idx, key_text_layer_x, key_text_layer_y, key_text_layer_alignment, key_text_layer_anchor, 0)

        keybase = svg.Rect(transform = [svg.Rotate(kCap.key_r), svg.Translate(kCap.pos_x, kCap.pos_y)],
                            width = kCap.key_w,
                            height = kCap.key_h,
                            fill = 'url(#RadialGradient1)',
                            rx = 8,
                            ry = 8,
                            style = 'stroke: black; fill: #e3e3e3; stroke-width=1;')
        keycap = svg.Rect(transform = [svg.Rotate(kCap.key_r), svg.Translate(kCap.inner_pos_x,kCap.inner_pos_y)],
                            width = kCap.inner_key_w, 
                            height = kCap.inner_key_h,
                            rx = 3,
                            ry = 3,
                            style = 'stroke: #b5b5b5; fill: #ebebeb; stroke-width=0.5;')

        elements.extend([keybase, keycap])

        resetKey(kCap)

    for index, layer in enumerate(fullLayout):
        for idx, key_cap in enumerate(layer['keys']):
            print_key = checkIfKeyOnPreviousLayerIsTheSame(key_cap, kCap, level, index, idx, fullLayout)
            determineKeyPositions(level, kCap, coords, idx, key_text_layer_x, key_text_layer_y, key_text_layer_alignment, key_text_layer_anchor, index)
            # fontSize = '12' if len(key_cap) > 2 else '14'
            if (print_key):
                print('excluding:' + key_cap)
                key_cap = ''
            keytext = svg.Text(transform=[svg.Rotate(kCap.key_text_r),svg.Translate(kCap.key_text_x, kCap.key_text_y)],
                        text = key_cap, 
                        dominant_baseline = key_text_layer_alignment[index],
                        text_anchor = key_text_layer_anchor[index],
                        style = 'fill=black; pointer-events: none;', font_size = 12, stroke = key_text_layer_cmyk[index], stroke_width = 0.3)
            
            elements.extend([keytext])

            resetKey(kCap)

    canvas.elements = elements
    return canvas

def resetKey(kCap):
    kCap.key_h = 60
    kCap.key_w = 60
    kCap.key_r = 0
    kCap.key_text_r = 0

def determineKeyPositions(level, kCap, coords, idx, key_text_layer_x, key_text_layer_y, key_text_layer_alignment, key_text_layer_anchor, index):
    kCap.pos_x = coords[idx]['x'] * kCap.coord_multiplier
    kCap.pos_y = level + coords[idx]['y'] * kCap.coord_multiplier
    if 'h' in coords[idx]:
        kCap.key_h = coords[idx]['h'] * kCap.coord_multiplier
    if 'w' in coords[idx]:
        kCap.key_w = coords[idx]['w'] * kCap.coord_multiplier
    if 'r' in coords[idx]:
        kCap.key_r = coords[idx]['r']

    kCap.inner_pos_x = kCap.pos_x + kCap.key_w / 8
    kCap.inner_pos_y = kCap.pos_y + kCap.key_h / 14

    if (kCap.key_h > 60):
        kCap.inner_pos_x = kCap.pos_x + kCap.key_w / 10
        kCap.inner_pos_y = kCap.pos_y + kCap.key_h / 10

    kCap.inner_key_h = kCap.key_h * 0.75
    kCap.inner_key_w = kCap.key_w * 0.75

    if (kCap.key_r != 0):
        negative = str(kCap.key_r).find("-") != -1
        kCap.key_text_r = kCap.key_r + 90 if negative else kCap.key_r - 90
        kCap.key_text_x = kCap.inner_pos_x + kCap.key_w / 8 if negative else kCap.inner_pos_x + kCap.key_w / 5
        kCap.key_text_y = kCap.inner_pos_y + kCap.key_h / 5 if negative else kCap.inner_pos_y + kCap.key_w / 1
    else:
        kCap.key_text_x = kCap.inner_pos_x + kCap.key_w / key_text_layer_x[index]
        kCap.key_text_y = kCap.inner_pos_y + kCap.key_h / key_text_layer_y[index]
        kCap.key_text_r = kCap.key_r

def checkIfKeyOnPreviousLayerIsTheSame(key_cap, kCap, level, index, idx, fullLayout):
    if (index > 0 and (key_cap == fullLayout[index - 1]['keys'][idx] or key_cap == "")):
        return True
    else:
        return False
