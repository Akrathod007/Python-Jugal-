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

"""
1. Count Frequency of Characters
word = "python"

freq = {
    "p":1
}

2. Count Frequency of Words
sentence = "python is easy python is powerful"

3. Create Dictionary of Number and Cube
data = {}

data = {
    1:1,
    2:8,
    3:27
}

4. Swap Keys and Values
data = {"a": 1,"b": 2, "c": 3}

5. Find Duplicate Values
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30
}

6. Create Dictionary From String Length
words = ["python", "java", "ai"]

data = {
    "Python":6
}

7. Count Vowels in Sentence
sentence = "python programming"

8. Create Dictionary of Factorials
data = {
    1:1,
    2:2,
    3:6,
    4:24,
    5:120
}

9. Group Numbers by Positive and Negative
numbers = [10, -5, 7, -2, 0]

data = {
    "positive": [],
    "negative": [],
    "zero": []
}

10. Separate Even and Odd Numbers
numbers = [1, 2, 3, 4, 5, 6]

data = {
    "even": [],
    "odd": []
}

"""


# 1. Count Frequency of Characters
# word = "madam"

# d = {}

# for i in word:
#     d[i] = d.get(i, 0) + 1

# print(d)


"""
2. Count Frequency of Words
sentence = "python is easy python is powerful"
"""
# sentence = "python is easy python is powerful"
# li = sentence.split()

# d = {}

# for i in li:
#     d[i] = d.get(i, 0) + 1

# print(d)


# 3. Create Dictionary of Number and Cube
# data = {}

# for i in range(1, 11):
#     data[i] = i**3

# print(data)


"""
4. Swap Keys and Values
data = {"a": 1,"b": 2, "c": 3}
"""
# data = {"a": 1, "b": 2, "c": 3}
# d = {}
# for k, v in data.items():
#     d[v] = k

# print(d)


"""
5. Find Duplicate Values
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30
}
"""
# data = {"a": 10, "b": 20, "c": 10, "d": 20}
# duplicate = []

# values = list(data.values())

# for i in values:
#     if values.count(i) > 1 and i not in duplicate:
#         duplicate.append(i)


# print(duplicate)


"""
6. Create Dictionary From String Length
words = ["python", "java", "ai"]
"""
# words = ["python", "java", "ai"]

# d = {}
# for word in words:
#     d[word] = len(word)

# print(d)
