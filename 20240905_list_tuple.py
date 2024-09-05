# my_list = [1,2,3,4,5,6]
from traceback import print_tb

my_list = [1,2,3,4,5,6]
#print(my_list[1])

# x : start
# y : end
# s : step

# 2, 4, 6
# print(my_list[0:5:2])


myList = ['j','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# print(myList[0:9:3])

# print(myList[::-2])

#
# m1 = [1,2,3,
#     34,5,6
# ]
#
# m2 = [
#
# ]

## Sum List
# list1 = [1,2,3]
# list2 = [4,5,6]
# print(list1 + list2)
# print(list1 * 3)


# Find Element

students = ["YANY","LYMENG","SETHA"]

# => YANY
isExist = "YANY" in students
# print(isExist)


usernameList = ["Vanna","Sreypich","Chan","Tola"]

# system allow user input username : vanna
loginSuccess = "Vanna" in usernameList
# print(loginSuccess) # true or false

#
# c = 10
# C = "Nice to meeting"
# print(c)
# print(C)

total_student = len(students)
# print(total_student)


# min_val = min(my_list)
# print(min_val)
#
# max_val = max(my_list)
# print(max_val)
#
#
# min2_val = min(myList)
# print(min2_val)
#
# max2_val = max(myList)
# print(max2_val)
#
# print(ord('a'))
# print(ord('j'))

print(students)
students[0] = "NARA"
print(students)

students.remove(students[0])
print(students)

#students.append("DAVID")
students.insert(1,"DAVID")
print(students)

# students.clear()
print(len(students))

# students2 = students.copy()
# print(students2)
# students2.remove(students2[0])
# print(students2)
print(students)


items = ["CoCaCola","ABC", "Sting"]
# count_item = items.count("ABC")
print(items)
# items.pop(0)
# items.remove(items[0]) # get element by index
# items.remove("CoCaCola") # remove by specific element
# print(items)


# items.reverse()
# print(items)

my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
