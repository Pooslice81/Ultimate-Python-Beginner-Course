# def function_name(Input):
#     Action
#     return Output


def add_one(number):
    output = number + 1
    return output


var = 0
print(var)

var1 = add_one(var)
var2 = add_one(var1)
var3 = add_one(5.4)
var4 = add_one(3.5 + 3.5)  # values in brackets are calculated before calling the function
print(var)
print(var2)
print(var3)
print(var4)


def add_one_add_two(number_one, number_two):
    output = number_one + 1
    output += number_two + 2  # output = output + number_two + 2
    return output


var5 = add_one_add_two(var2,var3)
print(var5)

