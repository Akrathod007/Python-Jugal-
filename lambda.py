# def add(a, b):
#     return a + b


# add2 = lambda a, b: a + b

# print(add(20, 10))
# print(add2(20, 10))


# def evenOdd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


# print(evenOdd(10))

# evenOdd2 = lambda n: "Even" if n % 2 == 0 else "Odd"
# print(evenOdd2(11))


def demo(n):
    if n > 0:
        return "Pos"
    elif n < 0:
        return "Neg"
    else:
        return "Zero"


print(demo(10))

demo2 = lambda n: "Pos" if n > 0 else "Neg" if n < 0 else "Zero"
print(demo2(-10))


login = lambda user, pwd: (
    "Admin Login"
    if user == "admin" and pwd == "007"
    else "User Login" if user == "user" and pwd == "xyz" else "Invalid Login"
)

print(login("admin", "123"))
print(login("admin", "007"))
print(login("user", "xyz"))
