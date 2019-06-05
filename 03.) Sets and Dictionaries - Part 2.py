"""
- Practical application of dictionaries
- Keeping track of unique item numbers
- We can easily access desired values (with their keys)
  without having to remember their original position (like on a list)
"""

black_shoes = {42:2,
               41:3,
               40:4,
               39:1,
               38:0}

while True:
    purchase_size = int(input("What shoe size would you like to buy? \n"))
    if black_shoes[purchase_size] > 0:
        black_shoes[purchase_size] -= 1
    else:
        print("Shoes are no longer in stock.")
    print(black_shoes)
