# if condition:
#     action


# click = False
# like = 0
# print(like)
#
# click = True
#
# if click:
#     like += 1
#     click = False
#
# print(like)
#
# temperature = 20
# thermo = 15
# print(thermo)
#
# if temperature <= 15:
#     thermo = thermo + 5
#
# print(thermo)
#
# if temperature <= 20:
#     thermo += - 3
#
# print(thermo)

time = "Night"
sleepy = True
pajamas = "Off"

if time == "Night" and sleepy == True:
    pajamas = "On"

print(pajamas)

time = "Day"
sleepy = False
pajamas = "Off"
in_bed = True

if time == "Night" or sleepy == True:
    pajamas = "On"
elif time == "Morning" and in_bed == True:
    pajamas = "On"

print(pajamas)