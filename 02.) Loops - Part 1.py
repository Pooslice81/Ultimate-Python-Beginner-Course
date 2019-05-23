word = "Hello"

for x in word:
    print(x)
print()

word_1 = "World"
letters = []

for l in word_1:
    print(l)
    if l == "r" or l == "o":
        print("This is an", l)
    letters.append(l)

print(letters)
print()

for x in letters:
    print(x)
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in numbers:
    if n % 2 == 1:
        print(n)
print()

# range(start, stopping, steps)
list_2 = []

for num in range(10):
    print(num)
print()

list_2 = []

for num in range(10):
    list_2.append(num)
    print(num)
print(list_2)
print()

list_2 = []

for num in range(1, 10, 2):
    list_2.append(num)
    print(num)
print(list_2)
print()
