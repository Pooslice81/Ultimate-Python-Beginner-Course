# test_list = ["element1", "element2", "element3"]
# test_list = [0,1,2] each element has it's own index number, starting at 0.

scores = [70, 85, 67.5, 90, 80]
print(scores)
print(scores[1])  # Square brackets allow reference to a specific element in the list. first element starts with "0"
print(scores[-2])  # negative values count backwards from the last element. last element is referred to as "-1"
print(scores[0:2])  # print from the 1st element up to but not including the 3rd element
print(scores[1:2])  # print from the 1st element (inclusive) up to but not including the 3rd element
print(scores[2:])  # print from the 3rd element to the end.

scores[0] = 1  # how to reassign values of elements
scores[1] = "A"
print(scores)

scores[0:1] = []  # how to remove list elements

scores[1] = ["Hello", "World"]  # How to embed a list in another list
print(scores[1][1])  # How to print an element from within an embedded list.

scores.append("new_element")  # how to append an element to the end of an existing list.
