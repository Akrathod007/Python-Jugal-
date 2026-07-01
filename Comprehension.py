# li = []

# for i in range(1, 11):
#     li.append(i * i)

# print(li)

# li2 = (i * i for i in range(1, 11))
# print((li2))


# even = []

# for i in range(1, 11):
#     if i % 2 == 0:
#         even.append(i)

# print(even)

# even2 = [i for i in range(1, 11) if i % 2 == 0]
# print(even2)


# li = [34, 56, 23, 21, 78, 67, 55, 54]
# evenOdd = []

# for i in li:
#     if i % 2 == 0:
#         evenOdd.append("Even")
#     else:
#         evenOdd.append("Odd")


# print(li)
# print(evenOdd)

# evenOdd2 = ["Even" if i % 2 == 0 else "Odd" for i in li]
# print(evenOdd2)

"""
marks = [90, 56, 78, 66, 85, 95, 45, 67, 34, 79]

grade = []

for i in marks:
    if i >= 90:
        grade.append("Grade A")
    elif i >= 80:
        grade.append("Grade B")
    elif i >= 70:
        grade.append("Grade C")
    elif i >= 60:
        grade.append("Grade D")
    elif i >= 50:
        grade.append("Grade E")
    else:
        grade.append("Grade F")

print(grade)

grade2 = [
    (
        "Grade A"
        if i >= 90
        else (
            "Grade B"
            if i >= 80
            else (
                "Grade C"
                if i >= 70
                else "Grade D" if i >= 60 else "Grade E" if i >= 50 else "Grade F"
            )
        )
    )
    for i in marks
]

print(grade2)


"""

# s = {i * i for i in range(1, 11)}
# print(s)


d = {x: x * x for x in range(1, 11)}
print(d)

even = {x: x * x for x in range(1, 11) if x % 2 == 0}
print(even)

evenOdd = {x: (x * x if x % 2 == 0 else x**3) for x in range(1, 11)}
print(evenOdd)
