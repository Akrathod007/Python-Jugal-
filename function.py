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


def SayHello():
    print("Hello Hiii")


SayHello()
SayHello()
SayHello()
SayHello()
SayHello()


# 2. No Return Type With Arguments


def add(a, b):
    print(f"{a} + {b} = {a+b}")


add(10, 20)
add(20, 45)


# 3. With Return Type No Arguments


def mul():
    no1 = int(input("Enter a number 1 : "))
    no2 = int(input("Enter a number 2 : "))

    # print(f"{no1} * {no2} = {no1 * no2}")

    return no1 * no2


# mul()
# print(mul())

x = mul()
print(x)


# 4. With Return Type With Arguments


def gradeSystem(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    per = total * 100 / 500
    print("Total :", total)
    print("Percentage :", per)
    if per >= 90:
        return "A"
    elif per >= 80:
        return "B"
    elif per >= 70:
        return "C"
    elif per >= 60:
        return "D"
    elif per >= 50:
        return "E"
    else:
        return "F"


g = gradeSystem(80, 85, 97, 92, 87)
print(g)
