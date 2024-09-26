
# data = {'a': 1, 1: "Hello World", 1: 123, True: 321}
# print(data[True])
#
# data["course"] = "Python Programming"
# print(data["course"])
# print(data)

# studentList = {}
student1 = {"name":"HAK YANY","gender":"Female","subject": ["Pyton Programming","Mobile App Development"], "status":"Single" }
# studentList[1] = student1
# print(student1)

# List Example
idList = ["id",1]
# print(idList)
nameList = ["name","HAK YANY"]
# print(nameList)
idAndName = [idList, nameList]
studentList = dict(idAndName)
# print(studentList)




# Tuple
school = (("university","BELTEI"), ("faculty","IT"))
print(school)
schoolDict = dict(school)
print(schoolDict)


# Clear
# schoolDict.clear()
# print(f"schoolDict : {schoolDict}")

# Copy
school2 = schoolDict.copy()
print(school2)

# fromKey
list = ["id","name","gender","mail","phone"]
school3  = school2.fromkeys(list,"")
school3["name"] = "TOUCH TOLA"
school3["mail"] = "tola.touch@gmail.com"
print(school3)

email = school3.get("mail")
print(f" Email {email}")


school3.pop("name")
print(school3)

mail2 = school3.popitem("mail")
print(f" Mail {mail2}")


