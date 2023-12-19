import json
import uuid
import requests
import svg


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


def getKeyboardCoords(keyboardName):
    response = requests.get(f"https://keyboards.qmk.fm/v1/keyboards/" + keyboardName + "/info.json")
    keyboardJson = json.loads(response.content)
    layoutName = next(iter(keyboardJson['keyboards'][keyboardName]['layouts']))
    return keyboardJson['keyboards'][keyboardName]['layouts'][layoutName]['layout']


def get_keymap_svg(keyboardName, fullLayout):
    # we add the x because an ID needs to start with a letter
    mapNameId = 'x' + uuid.uuid4().hex
    coords = getKeyboardCoords(keyboardName)
    kCap = KeyboardCap(10, 10, 60, 60, 0, 10, 10, 96, 96, 35, 35, 0, 60, '')
    level = 10
    svg_w = 0
    svg_h = 0
    coord_multiplier = 60

    largest_x = max(coords, key=lambda x: x['x'])['x']
    largest_y = max(coords, key=lambda x: x['y'])['y']

    svg_w = (largest_x * coord_multiplier) + kCap.key_w
    svg_h = ((largest_y * coord_multiplier) + kCap.key_h * 1.8) * len(fullLayout)

    canvas = svg.SVG(style='transform-origin: center; transform-box: fill-box;', preserveAspectRatio = 'xMidYMin meet' ,width = svg_w, height = svg_h, id = mapNameId, viewBox= svg.ViewBoxSpec(0, 0, svg_w, svg_h))
    elements = []

    for index, layer in enumerate(fullLayout):
        for idx, key_cap in enumerate(layer['keys']):
            determineKeyPosition(level, coord_multiplier, kCap, coords, idx)
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
            keytext = svg.Text(transform=[svg.Rotate(kCap.key_text_r),svg.Translate(kCap.key_text_x, kCap.key_text_y)],
                                text = key_cap, 
                                font_weight = 600,
                                dominant_baseline='middle',
                                text_anchor='middle',
                                style = 'fill=black; pointer-events: none;')

            elements.extend([keybase, keycap, keytext])

            kCap.key_h = 60
            kCap.key_w = 60
            kCap.key_r = 0
            kCap.key_text_r = 0
        level = kCap.pos_y + 100


    canvas.elements = elements
    return canvas


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
        kCap.inner_pos_x = kCap.pos_x + kCap.key_w / 8
        kCap.inner_pos_y = kCap.pos_y + kCap.key_h / 14

        if (kCap.key_h > 60):
            kCap.inner_pos_x = kCap.pos_x + kCap.key_w / 10
            kCap.inner_pos_y = kCap.pos_y + kCap.key_h / 10

        negative = str(kCap.key_r).find("-") != -1

        # kCap.key_text_r = kCap.key_r + 90 if negative else kCap.key_r - 90
        kCap.key_text_r = kCap.key_r

        # kCap.key_text_x = kCap.inner_pos_x + kCap.key_w / \
        #     8 if negative else kCap.inner_pos_x + kCap.key_w / 5
        # kCap.key_text_y = kCap.inner_pos_y + kCap.key_h / \
        #     5 if negative else kCap.inner_pos_y + kCap.key_w / 1
        # kCap.baseline_text = ''
        kCap.key_text_x = kCap.inner_pos_x + kCap.key_w / \
            3 if negative else kCap.inner_pos_x + kCap.key_w / 3
        kCap.key_text_y = kCap.inner_pos_y + kCap.key_h / 3

    else:
        kCap.inner_pos_x = kCap.pos_x + kCap.key_w / 8
        kCap.inner_pos_y = kCap.pos_y + kCap.key_h / 14
        kCap.key_text_x = kCap.inner_pos_x + kCap.inner_key_w / 2
        kCap.key_text_y = kCap.inner_pos_y + kCap.inner_key_h / 2
        kCap.key_text_r = kCap.key_r
        kCap.baseline_text = 'dominant-baseline="middle" text-anchor="middle"'
