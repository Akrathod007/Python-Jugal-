# for i in range(11):
#     print(i)

# for i in range(1, 11):
#     print(i)

# for i in range(1, 11, 3):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# for i in range(10, 0, -2):
#     print(i)

# sum = 0

# for i in range(1, 11):
#     sum += i

# print("Sum :", sum)


# es = 0
# os = 0

# for i in range(1, 11):
#     if i % 2 == 0:
#         es += i
#     else:
#         os += i

# print("Even Sum :", es)
# print("Odd Sum :", os)


# no = int(input("Enter a number : "))

# for i in range(1, no + 1):
#     if no % i == 0:
#         print(i)

"""
5 * 1 = 5
5 * 2 = 10
"""

"""
no = int(input("Enter a number : "))

for i in range(1, 11):
    print(no, "*", i, "=", no * i)

"""
"""
no = int(input("Enter a number : "))
f = 1
for i in range(1, no + 1):
    f = f * i

print("Factorial of", no, "is", f)

"""

# no = int(input("Enter a number : "))

# Approach 1 :

# f = 0
# for i in range(1, no + 1):
#     if no % i == 0:
#         f += 1

# if f == 2:
#     print("Prime")
# else:
#     print("Not Prime")

# Approach 2 :
"""
f = 1
for i in range(2, no):
    if no % i == 0:
        f = 0
        break

if f == 1:
    print("Prime")
else:
    print("Not Prime")

"""


# base = 2
# expo = 4
# 2 ^ 4 -> 16
"""
b = int(input("Enter a base : "))
e = int(input("Enter a expo : "))

ans = 1

for i in range(1, e + 1):
    ans = ans * b

print("Ans :", ans)

"""

"""
for i in range(1, 6):
    for j in range(1, 4):
        print("i :", i, " j:", j)
        
"""
