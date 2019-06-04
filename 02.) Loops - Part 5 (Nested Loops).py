'''Put a loop inside another loop (nested loop)
Adding flow control into loops
Print custom output using nested loops. '''

#  | |   0
# -----  1
#  | |   2
# -----  3
#  | |   4

for row in range(5):  # 0,1 ,2, 3, 4
    if row % 2 == 0:
        print(" | | ")
    else:
        print("-----")
print()
print()

#  | |   1
# -----  2
#  | |   3
# -----  4
#  | |   5

for row in range(1, 6):
    if row % 2 == 1:
        for column in range(1, 6):
            if column % 2 == 1:
                if column != 5:
                    print(" ", end="")
                else:
                    print(" ")
            else:
                print("|", end="")
    else:
        print("-----")
