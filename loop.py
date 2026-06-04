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

"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

A B C D E
A B C D E
A B C D E
A B C D E
A B C D E

A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
"""

for i in range(1, 6):
    for j in range(1, 6):
        # print("*", end=" ")
        # print(j, end=" ")
        # print(i, end=" ")
        # print(chr(64 + j), end=" ")
        print(chr(64 + i), end=" ")
    print()

# print("Hello", end=" ")
# print("World")


"""
*
* *
* * *
* * * *
* * * * *

1
2 3
4 5 6
7 8 9 10
"""

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


"""
    Employee Mangement System
    
    1. Add employee
    eid,name,dsgn,sal -> 
    {
        1:{"name":"Raj","dsgn":"mgr","sal":20000},
        2:{"name":"Ram","dsgn":"mgr","sal":25000}
        3:
    }
    
    2.delete employee
    ask employee id to delete
"""

"""
1 2 3 4 5
1               1
0 1             2
1 0 1           3
0 1 0 1         4
1 0 1 0 1       5
"""


# for i in range(1, 6):
#     for j in range(1, i + 1):
#         if (i + j) % 2 == 0:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()


"""
1
A B
1 2 3
A B C D
1 2 3 4 5

"""


"""
1 2 3 4 5
* * * * * 1
*       * 2
*       * 3
*       * 4
* * * * * 5


    *
    *
* * * * *
    *
    *
"""

# no = int(input("Enter a number : "))
# for i in range(1, no + 1):
#     for j in range(1, no + 1):
#         if i == 1 or i == no or j == 1 or j == no:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


no = int(input("Enter a number : "))
for i in range(1, no + 1):
    for j in range(1, no + 1):
        if i == no // 2 + 1 or j == no // 2 + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


"""
    Employee Mangement System
    
    1. Add employee
    eid,name,dsgn,sal -> 
    {
        1:{"name":"Raj","dsgn":"mgr","sal":20000},
        2:{"name":"Ram","dsgn":"mgr","sal":25000}
        3:
    }
    
    2.delete employee
    ask employee id to delete
"""

# employee = {}
# while True:
#     print("1 -> Add Employee")
#     print("2 -> Delete Employee")
#     print("3 -> Exit")
#     ch = int(input("Enter Your Choice : "))

#     if ch == 1:
#         eid = int(input("Enter a id : "))
#         name = input("Enter a name : ")
#         dsgn = input("Enter a dsgn : ")
#         sal = float(input("Enter a salary : "))

#         employee[eid] = {"name": name, "dsgn": dsgn, "salary": sal}

#     elif ch == 2:
#         eid = int(input("Enter a id you want to delete : "))

#         if eid in employee:
#             del employee[eid]

#         print("delete successfully")
#     elif ch == 3:
#         break

# print(employee)
