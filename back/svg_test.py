import json
from parse_keys import get_layout

svg_open = '<svg version="1.1" width="5000" height="5000" xmlns="http://www.w3.org/2000/svg">'
svg_close = '</svg>'

level = 60
row_x = 60
row_y = 60
key_h = 100
key_w = 100
key_r = 0
row_inner_x = row_x * 1.2 + row_y * 1.2
row_inner_y = row_y * 1.2 + row_y * 1.2
key_inner_h = key_h * 0.8 + key_w * 0.8
key_inner_w = key_h * 0.8 + key_w * 0.8
key_text_x = row_x + key_h / 2
key_text_y = row_y + key_w / 2

line_count = 0
split_count = 0
split_x = 0
font_color = ['red', 'green', 'yellow', 'blue', 'pink', 'white']


def getKeyboardCoords():
    with open("keymap_layouts/liliums/Lily58.json", 'r') as j:
        contents = json.loads(j.read())
        print(next(iter(contents['layouts'])))
        return contents['layouts'][next(iter(contents['layouts']))]['layout']

    # print(contents['layouts'][next(iter(contents['layouts']))]['layout'])
    # print(type(contents['layouts'][next(iter(contents['layouts']))]))


with open('layout.svg', 'w') as file:
    full_layout = get_layout()
    coords = getKeyboardCoords()

    file.write(svg_open)
    file.write('<style>' +
                'rect {transform-origin: center; transform-box: fill-box;}'
                'text {transform-origin: center; transform-box: fill-box; font-family: sans-serif; font-size: 14;}' +
                '.key-base {stroke: black; fill: #C3C3C3; stroke-width=1;}' +
                '.key-cap {stroke: #BFBBBB; fill: white; stroke-width=1;}' +
                '.key-text {fill=black;}' +
               '</style>')
    file.write('<rect fill="transparent" />')

    for index, layer in enumerate(full_layout):
        level = level + 600
        print(row_y)
        for idx, key_cap in enumerate(layer['keys']):
            row_x = coords[idx]['x'] * 100
            row_y = level + coords[idx]['y'] * 100
            if 'h' in coords[idx]:
                key_h = coords[idx]['h'] * 100
            if 'w' in coords[idx]:
                key_w = coords[idx]['w'] * 100
            if 'r' in coords[idx]:
                key_r = coords[idx]['r']

            key_inner_h = key_h * 0.8
            key_inner_w = key_w * 0.8
            row_inner_x = row_x + key_w / 10
            row_inner_y = row_y + key_h / 10
            key_text_x = row_inner_x + key_w / 10
            key_text_y = row_inner_y + key_h / 2

            # transform="rotate({4})"
            file.write('<rect class="key-base" x="{0}" y="{1}" width="{2}" height="{3}" transform="rotate({4})" rx="8" ry="8" />'.format(row_x, row_y, key_w, key_h, key_r))
            file.write('<rect class="key-cap" x="{0}" y="{1}" width="{2}" height="{3}" transform="rotate({4})" rx="3" ry="3" />'.format(row_inner_x, row_inner_y, key_inner_w, key_inner_h, key_r))
            file.write('<text class="key-text" x="{0}" y="{1}" transform="rotate({2})">{3}</text>'.format(key_text_x, key_text_y, key_r, key_cap))

            key_h = 100
            key_w = 100
            key_r = 0
    file.write(svg_close)
