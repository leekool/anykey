keys = []

class Keymap:
    def __init__(self, *layers):
        for i, layer in enumerate(layers):
            setattr(self, f"layer{i+1}", layer)

with open("testmap.c", "r") as f:
    flag = False
    for line in f:
        if line.strip().startswith('//') == False:
            continue
        if "MATRIX" in line:
            flag = True
        if flag:
            print(line)
        if flag and "};" in line:
            break

f.close()
