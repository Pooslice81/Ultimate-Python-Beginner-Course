participants = ["Jen", "Alex", "Tina", "Joe", "Ben"]

position = 1
for participant in participants:
    if participant == "Tina":
        print("About to break")
        break
    print("About to increment")
    position += 1

print(position)

for current_index in range(len(participants)):
    if participants[current_index] == "Joe":
        break

print(current_index)
