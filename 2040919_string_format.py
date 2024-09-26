msg = "Welcome to We BELTEI IU"
# print(msg)
# print(len(msg))
# print(msg.center(24, '$'))
# print(msg.rjust(len(msg) + 2,'_'))
# print(msg.ljust(len(msg) + 3, '_'))


# find
my_result = msg.find("We")
# print(f"{my_result}")
my_result = msg.find("abc")
# print(my_result)



# join

my_list = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
# print(my_list)
my_list.insert(5, "Saturday")
my_list.insert(6, "Sunday")
my_join_list = ",".join(my_list)
# print(my_join_list)

# split
# print(my_join_list)
my_split = my_join_list.split()
# print(my_split)
myTest = "Whitespace is the default separator."
# print(myTest.split())
myTest2 = "D:\\Documents\\Python Class"
# print(myTest2.split("\\"))


# Lower and Upper
# username = "Sok.Channa123"
# user_in_db = "sok.channa123".upper()
#
# print(username)
# print(user_in_db)
# if (username.upper() == user_in_db):
#     print("Success")
# else:
#     print("Fail")
#


programming = "Welcome to Python Programming"
# print(programming)
myReplace = programming.replace("Welcome to","I Love")
# print(myReplace)


# my_input = input("Welcome ")
# print(my_input)
# print(len(my_input))
# print(len(my_input.strip()))


a = "1"
b = "2"
print("{}{}".format(a,b))

