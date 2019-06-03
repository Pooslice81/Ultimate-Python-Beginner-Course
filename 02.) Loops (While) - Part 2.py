# while (condition):
#     Action
#     Action 2
#     Action 3

counter = 1
s = 0

while counter <= 100:
    print(counter)
    s += counter
    counter += 1

print(s)

letters = ["a", "b", "c", "d", "e"]

index = 0
while index < len(letters):
    print(index)
    print(letters[index])
    index += 1
print()

height = 5213
velocity = 48
time = 0

while height > 0:
    height -= velocity
    time += 1

print(height)
print(time)
