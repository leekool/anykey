keys = []

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
