"""
- How can we import data from files on our computer
- We can save our data to files by writing to them.
- Format start with open and includes what we want to do, and closing the file after we've finished with it.
"""

# file = open("filename", "r/w/a/r+")
# file.close()

cities = ["London", "Paris", "New York", "Los Angeles", "Cape Town"]

cities_file = open("cities", "w")

for city in cities:
    cities_file.write(city + "\n")

print("Done")

cities_file.close()

cities_file = open("cities", "r")

first_line = cities_file.readline()
second_line = cities_file.readline()

print(first_line)
print(second_line)

for line in cities_file:
    print(line, end="")

the_whole_file = cities_file.read()

print(the_whole_file)

cities_file.close()

final_spot = "Melbourne"

cities_file = open("cities", "a")
cities_file.write(final_spot)
cities_file.close()

cities_file = open("cities", "r")
for line in cities_file:
    print(line, end="")

cities_file.close()

for i in range(5):
    with open("cities", "r") as cities_file:
        for line in cities_file:
            print(line)
