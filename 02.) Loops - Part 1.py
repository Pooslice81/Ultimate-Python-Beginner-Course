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
