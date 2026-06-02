# if 5 == 5:
#     print("Hello")

# if 5 > 10:
#     print("Hello2")


# no1 = int(input("Enter a number 1 : "))
# no2 = int(input("Enter a number 2 : "))
# print(no1 + no2)


# no = int(input("Enter a number : "))
"""
if no % 2 == 0:
    print("Even")
else:
    print("Odd")

"""

"""
11 -> 00001011
1 ->  00000001
-----------------
& ->  00000001
"""

# if no & 1:
#     print("Odd")
# else:
#     print("Even")


# m1 = int(input("Enter a marks 1 : "))
# m2 = int(input("Enter a marks 2 : "))
# m3 = int(input("Enter a marks 3 : "))
# m4 = int(input("Enter a marks 4 : "))
# m5 = int(input("Enter a marks 5 : "))

# total = m1 + m2 + m3 + m4 + m5
# per = total / 5

# print("Total :", total)
# print("Percentage :", per)
# if per >= 90:
#     print("A")
# elif per >= 80:
#     print("B")
# elif per >= 70:
#     print("C")
# elif per >= 60:
#     print("D")
# elif per >= 50:
#     print("E")
# else:
#     print("Fail")


# n = int(input("Enter a number : "))

# if n > 0:
#     if n % 2 == 0:
#         print("no is positive even")
#     else:
#         print("no is positive odd")
# elif n < 0:
#     if n % 2 == 0:
#         print("no is negative even")
#     else:
#         print("no is negative odd")
# else:
#     print("Zero")


# multiple if

"""
if con:
    //code
    
if con:
    //code
    
if con:
    //code
"""

"""
note count 

Amt = 1260
n500 -> 2 -> 1260 - 1000 -> 260
n100 -> 2 -> 260 - 200 -> 60
n50 -> 1 -> 60 - 50 -> 10
n20 -> 0
n10 -> 1 -> 10 - 10 -> 0
n5 -> 0
n2 -> 0
n1 -> 0
"""


"""
amt = int(input("Enter a number : "))

n500 = n100 = n50 = n20 = n10 = n5 = n2 = n1 = 0

if amt >= 500:
    n500 = amt // 500  # n500 = 2
    amt = amt - n500 * 500
if amt >= 100:
    n100 = amt // 100  # n500 = 2
    amt = amt - n100 * 100
if amt >= 50:
    n50 = amt // 50  # n500 = 2
    amt = amt - n50 * 50
if amt >= 20:
    n20 = amt // 20  # n500 = 2
    amt = amt - n20 * 20
if amt >= 10:
    n10 = amt // 10  # n500 = 2
    amt = amt - n10 * 10
if amt >= 5:
    n5 = amt // 5  # n500 = 2
    amt = amt - n5 * 5
if amt >= 2:
    n2 = amt // 2  # n500 = 2
    amt = amt - n2 * 2
if amt >= 1:
    n1 = amt // 1  # n500 = 2
    amt = amt - n1 * 1


print("N500 :", n500)
print("N100 :", n100)
print("N50 :", n50)
print("N20 :", n20)
print("N10 :", n10)
print("N5 :", n5)
print("N2 :", n2)
print("N1 :", n1)

"""

"""
no1 = int(input("Enter a number 1 : "))
no2 = int(input("Enter a number 2 : "))
no3 = int(input("Enter a number 3 : "))

if no1 > no2 and no1 > no3:
    print("No1 is bigger")
elif no2 > no3:
    print("No2 is bigger")
else:
    print("No3 is bigger")

"""

# x = 10
# y = 20

# if x > y:
#     print("X is Bigger")
# else:
#     print("Y is bigger")


# result = "X is Bigger" if x > y else "Y is bigger"
# print(result)


# x = 10
# y = 20
# print("x is greater") if x > y else print("y is greater")


"""
 if per >= 90:
#     print("A")
# elif per >= 80:
#     print("B")
# elif per >= 70:
#     print("C")
# elif per >= 60:
#     print("D")
# elif per >= 50:
#     print("E")
# else:
#     print("Fail")
"""
per = 90
result = (
    "A"
    if per >= 90
    else (
        "B"
        if per >= 80
        else "C" if per >= 70 else "D" if per >= 60 else "E" if per >= 50 else "Fail"
    )
)
print(result)
