"""
Sets contain each unique element.
Dictionaries store using key-value pairs.
Both are unpaired.
"""

# sets = {"element1", "element2", "element3", "element4"}
# print(sets)
#
# if "element1" in sets:
#     print("yes")

country_list = []
for i in range(5):
    country = input("Please enter your country: ")
    country_list.append(country)

# country_set = set(country_list)
#
# print(country_list)
# print(country_set)
#
# if "Australia" in country_set:
#     print("Australia is in", country_set)
#
# print()
#
# dictionary = {"Key1":"Value1",
#               "Key2":"Value2",
#               "Key3":"Value3"}

country_dictionary = {}
for country in country_list:
    if country in country_dictionary:
        country_dictionary[country] += 1
    else:
        country_dictionary[country] = 1

print(country_dictionary)
