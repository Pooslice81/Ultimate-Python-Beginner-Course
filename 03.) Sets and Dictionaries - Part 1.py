"""
Sets contain each unique element.
Dictionaries store using key-value pairs.
Both are unpaired.
"""

sets = {"element1", "element2", "element3", "element4"}
print(sets)

if "element1" in sets:
    print("yes")

country_list = []
for i in range(5):
    country = input("Please enter your country: ")
    country_list.append(country)

country_set = set(country_list)

print(country_list)
print(country_set)
