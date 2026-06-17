"""

user = {"Name": "Ram", "Age": 21, "City": "Ahm"}
print(user)
print(type(user))

person = dict(name="Shyam", age="22")
print(person)

print(user["Name"])
print(user["City"])
# print(user["State"])
print(user.get("Name"))
print(user.get("State", "Not Found"))

# del user["City"]
# print(user["City"])

elm = user.pop("City")
print(elm)
print(user)

t = user.popitem()
print(t)
print(user)

user.clear()
print(user)

d = {}
print(type(d))

"""

"""
person = {"Name": "Ram", "Age": 21, "City": "Ahm", "State": "Guj"}
print(person)

person["City"] = "Surat"
print(person)

person["Country"] = "India"
print(person)
"""
"""
for i in person:
    # print(i, "->", person[i])
    print(i, "->", person.get(i))

"""
"""
for i in person.keys():
    print(i, "->", person.get(i))

for i in person.values():
    print(i)

for i in person.items():
    print(i)

print(person.keys())
print(person.values())
print(person.items())

"""

"""
student = {"name": "Raju", "age": 21}
student.update({"age": 22, "city": "Surat"})
print(student)

# elm = student.pop("State", "Not Found")
# print(elm)

new_student1 = student.copy()
new_student2 = student
print(new_student1)
new_student1["State"] = "Guj"
new_student2["State"] = "Mumbai"
print(new_student1)
print(new_student2)
print(student)

keys = ["math", "science", "english"]
marks = dict.fromkeys(keys, 1000)
print(marks)

"""

"""
keys = ("math", "science", "english")
marks = dict.fromkeys(keys, 1000)
print(marks)

student = {"name": "Raju"}
print(student.setdefault("age", 20))
print(student.setdefault("name"))
print(student)
print(len(student))

keys = ["Name", "Age", "City"]
values = ["Ram", 21, "Ahm"]

d = dict(zip(keys, values))
print(d)

"""

d = {1: "Ram", 2: "Shaym", 3: "Manan"}
print(d)

d2 = {("Hello",): "Hi", 1: "Bye", "Name": "Ram"}
print(d2)

# d3 = {[1, 2, 3]: "Hi"}
# print(d3)

d4 = {
    "person": {"Name": "Shyam", "Age": 21},
    "Address": {"City": "Ahm", "State": "Guj"},
}

print(d4)
print(d4["person"]["Name"])
print(d4["person"].get("Name"))
print(d4["Address"])

d5 = {
    "Virat": [98, 67, 56, 78, 77],
    "Dhoni": [45, 98, 88, 79, 67],
    "Rohit": [87, 66, 59, 45, 23],
}

print(d5)
d5["Dhoni"][2] = 77
print(d5)

final_Score = 0
for i in d5:
    print(i, "->", d5[i])
    sum = 0
    for j in d5[i]:
        sum = sum + j
    final_Score += sum
    print("Sum :", sum)

print("Final Score :", final_Score)
