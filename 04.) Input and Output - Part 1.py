"""
- Users can interact with the program through input.
- We can output desired values to the screen.
- How can we convert input to desired data type?
"""

# var = input("Message to the user")

name = input("What is your name? ")
print(name)

age = int(input("How old are you? "))
print(age)
print(age + 4)

score = []

for i in range(5):
    current_score = int(input("Please enter the score: "))
    score.append(current_score)
print(score)

for i in range(5):
    current_score = float(input("Please enter the score " + str(i + 1) + ": "))
    score.append(current_score)
    print("The score you entered was\n", current_score)
print(score)
