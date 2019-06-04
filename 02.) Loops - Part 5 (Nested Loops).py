'''Put a loop inside another loop (nested loop)
Adding flow control into loops
Print custom output using nested loops. '''

# | |   0
# -----  1
# | |   2
# -----  3
# | |   4

for row in range(5):  # 0,1 ,2, 3, 4
    if row % 2 == 0:
        print(" | | ")
    else:
        print("-----")
