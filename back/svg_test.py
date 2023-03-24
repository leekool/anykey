import json

svg_open = '<svg version="1.1" width="2000" height="1000" xmlns="http://www.w3.org/2000/svg">'
svg_close = '</svg>'

row_x = 60
row_y = 60
key_h = 40
key_w = 40
key_text_x = row_x + key_h / 2
key_text_y = row_y + key_w / 2

split_size = [6, 6, 6, 6, 3]
line_size = [12, 12, 12, 12, 6]
line_count = 0
split_count = 0
split_x = 0
font_color = ['red', 'green', 'yellow', 'blue', 'pink', 'white']

with open('parsed_keys.json', 'r') as f:

    with open('layout.svg', 'w') as file:
        full_layout = f.readlines()

        file.write(svg_open)
        file.write('<rect width="100%" height="100%" fill="transparent" />')

        for lidx, key_row in enumerate(full_layout):
            array_key_row = json.loads(key_row)

            for index, switches in enumerate(array_key_row):
                split_count = 0
                line_count = 0
                for idx, key_cap in enumerate(switches['keys']):
                        if idx % split_size[line_count] == 0:
                            row_x += 200
                            split_count += 1

                        if idx % line_size[line_count] == 0:
                            print('new line')
                            line_count += 1
                            row_y += 45
                            row_x = 60

                            if min(line_size) == line_size[line_count]:
                                 row_x = 60 + (45 * (max(split_size) - min(split_size)))

                        row_x += 45
                        key_text_x = row_x + key_h / 2
                        key_text_y = row_y + key_w / 2

                        print(key_cap)
                        print(idx)
                        print(index)



                        file.write('<rect x="{0}px" y="{1}px" width="{2}px" height="{3}px" stroke="{4}" fill="transparent" stroke-width="1" />'.format(row_x, row_y, key_h, key_w, font_color[index]))
                        file.write('<text x="{0}px" y="{1}px" font-size="8" dominant-baseline="middle" text-anchor="middle" fill="white">{2}</text>'.format(key_text_x, key_text_y, key_cap))
                row_y += 45

            row_y += 500
            row_x = 60
                
        file.write(svg_close)
    file.close()
    
