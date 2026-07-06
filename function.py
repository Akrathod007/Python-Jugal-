"""
Types of Function :
1.Built-in Function
2.User-defined Function

Function is block of code that perform specific task

Types of User-Defined Function:

1. No Return Type No Arguments
2. No Return Type With Arguments
3. With Return Type No Arguments
4. With Return Type With Arguments
"""

# 1. No Return Type No Arguments


# def SayHello():
#     print("Hello Hiii")


# SayHello()
# SayHello()
# SayHello()
# SayHello()
# SayHello()


# # 2. No Return Type With Arguments


# def add(a, b):
#     print(f"{a} + {b} = {a+b}")


# add(10, 20)
# add(20, 45)


# # 3. With Return Type No Arguments


# def mul():
#     no1 = int(input("Enter a number 1 : "))
#     no2 = int(input("Enter a number 2 : "))

#     # print(f"{no1} * {no2} = {no1 * no2}")

#     return no1 * no2


# # mul()
# # print(mul())

# x = mul()
# print(x)


# # 4. With Return Type With Arguments


# def gradeSystem(m1, m2, m3, m4, m5):
#     total = m1 + m2 + m3 + m4 + m5
#     per = total * 100 / 500
#     print("Total :", total)
#     print("Percentage :", per)
#     if per >= 90:
#         return "A"
#     elif per >= 80:
#         return "B"
#     elif per >= 70:
#         return "C"
#     elif per >= 60:
#         return "D"
#     elif per >= 50:
#         return "E"
#     else:
#         return "F"


# g = gradeSystem(80, 85, 97, 92, 87)
# print(g)


"""
          15
def prime(n):

    1 to n :
    2
    3
    5
    7
    11
    13  
    
"""


# def prime(n):
#     pc = 0

#     for i in range(1, n + 1):
#         f = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 f += 1
#         if f == 2:
#             print(i)
#             pc += 1

#     print("Prime Count : ", pc)


# prime(10000)


# def prime2(no):
#     f = 0
#     for j in range(1, no + 1):
#         if no % j == 0:
#             f += 1
#     if f == 2:
#         print(no)


# for i in range(1, 1000):
#     prime2(i)


# def add(a, b=40, c=30):
#     print(f"{a} + {b} + {c} = {a+b+c}")


# add(10, 20)
# add(10)
# add(10, 20, 30)


# def mul(a=10, b=20, c=30):
#     print(f"{a} * {b} * {c} = {a*b*c}")


# mul(10, 20, 30)
# mul(30, 40, 50)
# mul(b=5, c=10, a=20)


# def printChar(s):
#     for i in s:
#         print(i)


# printChar("Doremon")


# def reverseStr(s):
#     return s[::-1]


# print(reverseStr("Doremon"))


# def printList(l):
#     for i in l:
#         print(i)


# li = [1, 2, 3, 4, 5]
# printList(li)
# printList([1, 2, 3, 4, 5])


# def squareList(l):
#     sl = []
#     for i in l:
#         sl.append(i * i)

#     return sl


# x = squareList([1, 2, 3, 4, 5])
# print(x)


# def Math(a, b):
#     return a + b, a - b, a * b, a / b


# x = Math(20, 10)
# print(x)
# print(type(x))

# add, sub, mul, div = x
# print(add)
# print(sub)
# print(mul)
# print(div)


# def demo(a, b, *args):
#     print(a)
#     print(b)
#     print(args)

#     total = a + b + sum(args)

#     return total


# demo(10, 20)
# demo(10, 20, 30, 40, 50)

# print(demo(10, 20, 30, 40))


# def printLi(*args):
#     print(args)


# printLi(*[1, 2, 3, 4, 5])
# li = [1, 2, 3, 4, 5]

# printLi(*li)


# def demo(a, b, *args, **kargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kargs)


# demo(10, 20, 30, 40, 50, name="Ram", age=21)


person = {"Name": "Ram", "Age": 21, "City": "Ahm"}


# def printDict(**kargs):
#     print(kargs)


# printDict(**person)

# y = 200
# z = 200


# def Demo():
#     x = 10
#     global y, z
#     y += 200  # y = y + 200
#     z = z + 100
#     print(x)
#     print(y)
#     print(z)


# Demo()
# # print(x)    #Error

# print(y)


# x = 2000


# def demo():
#     x = 100
#     print(x)


# demo()
# print(x)


# def greet():
#     print("Hello")


# x = greet  # No ()
# x()


# def greet():
#     print("Hello")


# def call_func(func):
#     func()


# call_func(greet)
# # call_func(10)


# def outer():
#     def inner():
#         print("Inner function")

#     # inner()
#     return inner


# f = outer
# # f()
# print(f()())


# def add(a, b):
#     return a + b


# def sub(a, b):
#     return a - b


# ops = [add, sub]

# print(ops[0](10, 5))
# print(ops[1](10, 5))


def outer():
    print("Outer Function")
    x = 10

    def inner():
        y = 20
        nonlocal x
        x = x + 10
        print("Inner Function")
        print(x)
        print(y)

    # print(y)
    inner()


outer()
# print(x)
