with open("testmap.c", "r") as f:
    for line in f:
        if "MATRIX_COLS" in line:
            result = line.split("MATRIX_COLS", 1)[1]
            print(result)

f.close()
