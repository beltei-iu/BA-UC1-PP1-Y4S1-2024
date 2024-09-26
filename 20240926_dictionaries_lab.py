students = []

if __name__ == '__main__':
    id = 1
    while True:
        print("""
            1. List all items
            2. Insert new item
            3. Update item
            4. Delete item
        """)
        option = int(input("Enter your choice: "))
        if option == 1:
            print(students)
        elif option == 2:
            name = input("Enter your name: ")
            idList = ["id", id]
            nameList = ["name", name]
            studentDict = dict([idList, nameList])
            id = id + 1
            students.append(studentDict)







