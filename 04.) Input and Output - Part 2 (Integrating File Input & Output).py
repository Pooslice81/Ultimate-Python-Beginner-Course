"""
- How can we import data from files on our computer
- We can save our data to files by writing to them.
- Format start with open and includes what we want to do, and closing the file after we've finished with it.
"""

# file = open("filename", "r/w/a/r+")
# file.close()

cities = ["London\n", "Paris\n", "New York\n", "Los Angeles\n", "Cape Town\n"]

cities_file = open("cities", "w")

for city in cities:
    cities_file.write(city)

print("Done")

cities_file.close()

cities_file = open("cities", "r")

the_whole_file = cities_file.read()

print(the_whole_file)

cities_file.close()
