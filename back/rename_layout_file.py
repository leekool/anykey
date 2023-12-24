import json
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path

onlyfiles = [f for f in listdir('keymap_layouts') if isfile(join('keymap_layouts', f))]
folderdir = 'C:/Users/Kurtis/VSCode Projects/layout_generator/back/keymap_layouts/'

for filename in onlyfiles:
    print(filename)
    keyboard_name = ''
    manufacturer = ''
    if not filename.startswith('info'):
        continue

    with open('keymap_layouts/' + filename, 'r') as j:
        contents = json.loads(j.read())

        if 'keyboard_name' in contents:
            keyboard_name = contents['keyboard_name']

            if 'manufacturer' in contents:
                manufacturer = contents['manufacturer'] + '/'

        j.close

    if keyboard_name != '':
        # if manufacturer != '':
        #     os.makedirs(manufacturer, exist_ok=True)
        filepath = Path(folderdir + manufacturer + keyboard_name + '.json')
        if filepath.exists():
            continue
        os.renames(folderdir + filename, folderdir + manufacturer + keyboard_name + '.json')
