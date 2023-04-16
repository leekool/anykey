import json
from parse_keys import get_layout


def getKeyboardCoords(mapPath):
    with open(mapPath, 'r') as j:
        contents = json.loads(j.read())
        print(next(iter(contents['layouts'])))
        return contents['layouts'][next(iter(contents['layouts']))]['layout']

def get_keymap_svg(mapPath, fullLayout):

    svg_open = '<svg version="1.1" width="1000" height="2500" xmlns="http://www.w3.org/2000/svg">'
    svg_close = '</svg>'

    level = 30
    row_x = 30
    row_y = 30
    key_h = 50
    key_w = 50
    key_r = 0
    row_inner_x = row_x * 0.6 + row_y * 0.6
    row_inner_y = row_y * 0.6 + row_y * 0.6
    key_inner_h = key_h * 0.8 + key_w * 0.8
    key_inner_w = key_h * 0.8 + key_w * 0.8
    key_text_x = row_x + key_h / 2
    key_text_y = row_y + key_w / 2
    key_text_r = 0

    with open('layout.svg', 'w') as file:
        coords = getKeyboardCoords(mapPath)

        svg_string = svg_open

        file.write(svg_open)
        svg_string += """<style>
                    rect {transform-origin: center; transform-box: fill-box;}'
                    text {transform-origin: center; transform-box: fill-box; font-family: sans-serif; font-size: 14;}
                    .key-base {stroke: black; fill: #C3C3C3; stroke-width=1;}
                    .key-cap {stroke: #BFBBBB; fill: white; stroke-width=1;}
                    .key-text {fill=black;}
                </style>"""
        file.write('<style>' +
                    'rect {transform-origin: center; transform-box: fill-box;}'
                    'text {transform-origin: center; transform-box: fill-box; font-family: sans-serif; font-size: 14;}' +
                    '.key-base {stroke: black; fill: #C3C3C3; stroke-width=1;}' +
                    '.key-cap {stroke: #BFBBBB; fill: white; stroke-width=1;}' +
                    '.key-text {fill=black;}' +
                '</style>')
        svg_string += '<rect fill="transparent" />'
        file.write('<rect fill="transparent" />')

        for index, layer in enumerate(fullLayout):
            for idx, key_cap in enumerate(layer['keys']):
                row_x = coords[idx]['x'] * 50
                row_y = level + coords[idx]['y'] * 50
                if 'h' in coords[idx]:
                    key_h = coords[idx]['h'] * 50
                if 'w' in coords[idx]:
                    key_w = coords[idx]['w'] * 50
                if 'r' in coords[idx]:
                    key_r = coords[idx]['r']

                key_inner_h = key_h * 0.8
                key_inner_w = key_w * 0.8
                row_inner_x = row_x + key_w / 10
                row_inner_y = row_y + key_h / 10
                if (key_r != 0):
                    negative = str(key_r).find("-") != -1
                    key_text_r = key_r + 90 if negative else key_r - 90
                    key_text_x = row_inner_x + key_w / 8 if negative else row_inner_x + key_w / 5
                    key_text_y = row_inner_y + key_h / 5 if negative else row_inner_y + key_w / 1
                else:
                    key_text_x = row_inner_x + key_w / 10
                    key_text_y = row_inner_y + key_h / 2
                    key_text_r = key_r

                file.write('<rect class="key-base" width="{2}" height="{3}" transform="translate({0}, {1}) rotate({4})" rx="8" ry="8" />'.format(row_x, row_y, key_w, key_h, key_r))
                file.write('<rect class="key-cap" width="{2}" height="{3}" transform="translate({0}, {1}) rotate({4})" rx="3" ry="3" />'.format(row_inner_x, row_inner_y, key_inner_w, key_inner_h, key_r))
                file.write('<text class="key-text" transform="translate({0}, {1}) rotate({2})">{3}</text>'.format(key_text_x, key_text_y, key_text_r, key_cap))

                svg_string += '<rect class="key-base" width="{2}" height="{3}" transform="translate({0}, {1}) rotate({4})" rx="8" ry="8" />'.format(row_x, row_y, key_w, key_h, key_r)
                svg_string += '<rect class="key-cap" width="{2}" height="{3}" transform="translate({0}, {1}) rotate({4})" rx="3" ry="3" />'.format(row_inner_x, row_inner_y, key_inner_w, key_inner_h, key_r)
                svg_string += '<text class="key-text" transform="translate({0}, {1}) rotate({2})">{3}</text>'.format(key_text_x, key_text_y, key_text_r, key_cap)

                key_h = 50
                key_w = 50
                key_r = 0
                key_text_r = 0
            level = level + 300
        svg_string += svg_close
        file.write(svg_close)
        return svg_string
