participants = ["Jen", "Alex", "Tina", "Joe", "Ben"]

position = 1
for participant in participants:
    if participant == "Tina":
        print("About to break")
        break
    print("About to increment")
    position += 1

print(position)
print()

for current_index in range(len(participants)):
    print(current_index)
    if participants[current_index] == "Joe":
        print("Have breaked")
        break
    print("Not breaked")

print(current_index)  # index starts at zero
print(current_index + 1)  # to get position, add 1 to index. this is because position = 1 at the start of script
print()

for number in range(10):
    if number % 3 == 0:
        print(number)
        print(number, "is divisible by 3")
        continue
    print(number, "is not divisible by 3")
print()
