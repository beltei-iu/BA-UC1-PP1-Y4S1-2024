# name = "BELTEI \n IU"
# # using str
# print(str(name))
# # using repr
# print(repr(name))

# unicode_string = "Café"
# print(unicode_string)

# text = "Hello, World!"
# byte_string = text.encode('utf-8')
# print(byte_string)

# text = "Hello, World!"
# byte_array = bytearray(text, 'utf-8')
# print(byte_array)


#
# firstName = "Raksa"
# lastName = "Sok"
# fullName = lastName + " " + firstName
# print(fullName)


# name = "BELTIE \n  IU"
# print(" String Represent as str :" + str(name))
#
# print(" String represent as repr :" + repr(name))

# context = """
#     BELTEI International University, Campus 1 (Tuol Sleng):
#     № 21, St.360, Sangkat Boeng Keng Kang 3, Khan Boeng Keng Kang,
#     Phnom Penh (100 meters South of Tuol Sleng Genocide Museum),
#     a 15-storey building with 110 rooms, 1 Lecture Hall with 150 seats,
#      1 conference hall with a capacity of 700 seats, 1 cafeteria, 1 library
#      and 2-basement parking lots.
# """

context = """
    BELTEI International University, Campus 1 (Tuol Sleng): 
    № 21, St.360, Sangkat Boeng Keng Kang 3, Khan Boeng Keng Kang, 
    Phnom Penh (100 meters South of Tuol Sleng Genocide Museum), 
    a 15-storey building with 110 rooms, 1 Lecture Hall with 150 seats,
     1 conference hall with a capacity of 700 seats, 1 cafeteria, 1 library 
     and 2-basement parking lots.
"""

sql_query = '''
    select * from tbl_users 
    left joint tbl_products 
    right joint ....
'''

# print(context)
# print(sql_query)

# print("This is a cat \N{Cat}")

# print("Welcome $name")
name = "Ly Naruth"
print(f"Welcome to {name}")


















