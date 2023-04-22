import json


def getKeyboardCoords(mapPath):
    with open(mapPath, 'r') as j:
        contents = json.loads(j.read())
        print(next(iter(contents['layouts'])))
        return contents['layouts'][next(iter(contents['layouts']))]['layout']

def get_keymap_svg(mapPath, fullLayout):

    level = 10
    row_x = 10
    row_y = 10
    key_h = 60
    key_w = 60
    key_r = 0
    row_inner_x = row_x * 0.5 + row_y * 0.5
    row_inner_y = row_y * 0.5 + row_y * 0.5
    key_inner_h = key_h * 0.7 + key_w * 0.7
    key_inner_w = key_h * 0.8 + key_w * 0.8
    key_text_x = row_x + key_h / 2
    key_text_y = row_y + key_w / 2
    key_text_r = 0
    svg_w = 0
    svg_h = 0
    coord_multiplier = 60

    with open('layout.svg', 'w') as file:
        coords = getKeyboardCoords(mapPath)

        largest_x = max(coords, key=lambda x: x['x'])['x']
        largest_y = max(coords, key=lambda x: x['y'])['y']
        svg_w = ((largest_x) * coord_multiplier) + key_w

        step1 = largest_y * coord_multiplier
        step2 = step1 + key_h
        step3 = step2 * len(fullLayout)
        svg_h = step3 + key_h * len(fullLayout)

        
        svg_string = '<svg version="1.1" xmlns="http://www.w3.org/2000/svg">'
        file.write('<svg version="1.1" xmlns="http://www.w3.org/2000/svg">')


        svg_string += '<style>svg {width:' + str(svg_w) + 'px; height:' + str(svg_h) + 'px;}'
        file.write('<style>svg {width:' + str(svg_w) + 'px; height:' + str(svg_h) + 'px;}')
        svg_string += """
                    rect {transform-origin: center; transform-box: fill-box;}'
                    text {transform-origin: center; transform-box: fill-box; font-family: sans-serif; font-size: 14;}
                    .key-base {stroke: black; fill: #C3C3C3; stroke-width=1;}
                    .key-cap {stroke: #BFBBBB; fill: white; stroke-width=1;}
                    .key-text {fill=black; pointer-events: none;letter-spacing: -1px;}
                </style>"""
        file.write('<style>' +
                    'rect {transform-origin: center; transform-box: fill-box;}'
                    'text {transform-origin: center; transform-box: fill-box; font-family: sans-serif; font-size: 14;}' +
                    '.key-base {stroke: black; fill: #C3C3C3; stroke-width=1;}' +
                    '.key-cap {stroke: #BFBBBB; fill: white; stroke-width=1;}' +
                    '.key-text {fill=black; pointer-events: none;letter-spacing: -1px;}' +
                '</style>')
        svg_string += '<rect fill="transparent" />'
        file.write('<rect fill="transparent" />')

        firstLayer = fullLayout[0]
        for idx, key_cap in enumerate(firstLayer['keys']):
            row_x = coords[idx]['x'] * coord_multiplier
            row_y = level + coords[idx]['y'] * coord_multiplier
            if 'h' in coords[idx]:
                key_h = coords[idx]['h'] * coord_multiplier
            if 'w' in coords[idx]:
                key_w = coords[idx]['w'] * coord_multiplier
            if 'r' in coords[idx]:
                key_r = coords[idx]['r']

            key_inner_h = key_h * 0.75
            key_inner_w = key_w * 0.75
            row_inner_x = row_x + key_w / 8
            row_inner_y = row_y + key_h / 18
            if (key_r != 0):
                negative = str(key_r).find("-") != -1
                key_text_r = key_r + 90 if negative else key_r - 90
                key_text_x = row_inner_x + key_w / 8 if negative else row_inner_x + key_w / 5
                key_text_y = row_inner_y + key_h / 5 if negative else row_inner_y + key_w / 1
            else:
                key_text_x = row_inner_x + key_w / 20
                key_text_y = row_inner_y + key_h / 5
                key_text_r = key_r

            file.write('<rect class="key-base" width="{2}" height="{3}" transform="translate({0}, {1}) rotate({4})" rx="8" ry="8" />'.format(row_x, row_y, key_w, key_h, key_r))
            file.write('<rect class="key-cap" width="{2}" height="{3}" transform="translate({0}, {1}) rotate({4})" rx="3" ry="3" />'.format(row_inner_x, row_inner_y, key_inner_w, key_inner_h, key_r))

            svg_string += '<rect class="key-base" width="{2}" height="{3}" transform="translate({0}, {1}) rotate({4})" rx="8" ry="8" />'.format(row_x, row_y, key_w, key_h, key_r)
            svg_string += '<rect class="key-cap" width="{2}" height="{3}" transform="translate({0}, {1}) rotate({4})" rx="3" ry="3" />'.format(row_inner_x, row_inner_y, key_inner_w, key_inner_h, key_r)

            key_h = 60
            key_w = 60
            key_r = 0
            key_text_r = 0

        key_text_layer_x = [20, 20, 20, 20]
        key_text_layer_y = [5, 2.5, 1.5, 5]

        for index, layer in enumerate(fullLayout):
            for idx, key_cap in enumerate(layer['keys']):
                row_x = coords[idx]['x'] * coord_multiplier
                row_y = level + coords[idx]['y'] * coord_multiplier
                if 'h' in coords[idx]:
                    key_h = coords[idx]['h'] * coord_multiplier
                if 'w' in coords[idx]:
                    key_w = coords[idx]['w'] * coord_multiplier
                if 'r' in coords[idx]:
                    key_r = coords[idx]['r']

                key_inner_h = key_h * 0.75
                key_inner_w = key_w * 0.75
                row_inner_x = row_x + key_w / 8
                row_inner_y = row_y + key_h / 18
                if (key_r != 0):
                    negative = str(key_r).find("-") != -1
                    key_text_r = key_r + 90 if negative else key_r - 90
                    key_text_x = row_inner_x + key_w / 8 if negative else row_inner_x + key_w / 5
                    key_text_y = row_inner_y + key_h / 5 if negative else row_inner_y + key_w / 1
                else:
                    key_text_x = row_inner_x + key_w / key_text_layer_x[index]
                    key_text_y = row_inner_y + key_h / key_text_layer_y[index]
                    key_text_r = key_r

                file.write('<text class="key-text" transform="translate({0}, {1}) rotate({2})">{3}</text>'.format(key_text_x, key_text_y, key_text_r, key_cap))

                svg_string += '<text class="key-text" transform="translate({0}, {1}) rotate({2})">{3}</text>'.format(key_text_x, key_text_y, key_text_r, key_cap)

                key_h = 60
                key_w = 60
                key_r = 0
                key_text_r = 0
        svg_string += '</svg>'
        file.write('</svg>')
        return svg_string
