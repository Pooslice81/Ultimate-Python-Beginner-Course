length = 20
to_print = "o"

for pos in range(1, length + 1):
    print(to_print * pos)

for pos in range(length + 1, 0, -1):
    print(to_print * pos)
