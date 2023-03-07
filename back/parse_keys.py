keys = ()

with open("testmap.c", "r") as f:
    flag = False
    for line in f:
        if "MATRIX_COLS" in line:
            flag = True
        if flag and line.strip().startswith('//') == False:
            print(line)
        if flag == True and "};" in line:
            break

f.close()
