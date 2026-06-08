s1 = "Hello"
s2 = "bye"
s3 = """HEllo"""

# print(s1, s2, s3)


"""
    H   E   L   L   O
    0   1   2   3   4
   -5  -4  -3  -2  -1

"""
# print(s1[2])
# print(s1[0])
# print(s1[-1])
# print(s1[-2])


"""

        M       i       s       s       i       s       s       i       p       p       i
        0       1       2       3       4       5       6       7       8       9       10
        -11     -10     -9      -8      -7      -6      -5      -4      -3      -2      -1
"""

# s2 = "Mississippi"
# print(s2[0:5])
# print(s2[4:9])
# print(s2[:7])
# print(s2[3:])
# print(s2[:])
# print(s2[0:9:2])
# print(s2[0:9:4])
# print(s2[-4:-9])
# print(s2[-9:-4])
# print(s2[::-1])
# print(s2[1:7:-1])
# print(s2[7:1:-1])
# print(s2[-4:-9:-1])
# print(s2[-4:-9:-3])
# print(s2[2:-3])

# 1) Case Conversion :

"""
s3 = "hello World"

print(s3.upper())
print(s3.lower())
print(s3.title())
print(s3.capitalize())
print(s3.swapcase())

"""

# 2) Searching & Finding :
"""
s2 = "Mississippi"
# print(s2.find("i"))
# print(s2.find("i", 4))
# print(s2.find("i", 5, 9))
# print(s2.find("ss"))
# print(s2.find("ssss"))

# print(s2.rfind("i"))
# print(s2.rfind("i", 2, 7))
# print(s2.rfind("ssss"))


# print(s2.index("i"))
# print(s2.index("i", 4))
# print(s2.index("i", 5, 9))
# # print(s2.index("iii"))
# print(s2.rindex("i"))
# print(s2.rindex("i", 4))
# print(s2.rindex("i", 5, 9))

print(s2.count("i"))
print(s2.startswith("Mi"))
print(s2.startswith("mi"))
print(s2.startswith("i", 4, 8))
print(s2.endswith("pi"))
print(s2.endswith("pi", 5))
print(s2.endswith("pi", 5, 9))

"""

# 3) Modification & Replacement :
"""
s3 = "   Hello   "
print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())


s4 = "Mississippi"
print(s4.replace("i", "o"))
print(s4.replace("ss", "rr"))

"""

# 4) Splitting & Joining :
"""
s4 = "I am Python"
print(s4.split())

s4 = "demo123@gmail.com"
print(s4.split("@"))

s4 = "a-b-c-d-e"
print(s4.split("-"))
print(s4.split("-", 2))
print(s4.rsplit("-"))
print(s4.rsplit("-", 2))

s4 = "a\nb\nc"
print(s4)
print(s4.splitlines())
print(s4.split("\n"))

li = ["a", "b", "c"]

print("-".join(li))
print("$".join(li))

"""

# 5) Checking Content :
"""
s = "abc123"
print(s.isalnum())
s = "abc"
print(s.isalnum())
s = "123"
print(s.isalnum())
print("-------------------------------------------------------")
s = "abc123"
print(s.isalpha())
s = "123"
print(s.isalpha())
s = "abc"
print(s.isalpha())
print("-------------------------------------------------------")
s = "abc123"
print(s.isdigit())
s = "123"
print(s.isdigit())
s = "abc"
print(s.isdigit())
print("-------------------------------------------------------")
s = "abc123"
print(s.isdigit())
s = "123"
print(s.isdigit())
s = "abc"
print(s.isdigit())
print("-------------------------------------------------------")
s = "abc123"
print(s.isdecimal())
s = "123"
print(s.isdecimal())
s = "abc"
print(s.isdecimal())
print("-------------------------------------------------------")
s = "¹"
print(s.isdigit())
print(s.isdecimal())
print("-------------------------------------------------------")
s = "⅔"
print(s.isnumeric())
print("-------------------------------------------------------")

s = "var1"
print(s.isidentifier())
s = "1var"
print(s.isidentifier())
s = "var_1"
print(s.isidentifier())
s = "var()"
print(s.isidentifier())
s = "_"
print(s.isidentifier())
print("-------------------------------------------------------")

s = "    "
print(s.isspace())
s = " 4   "
print(s.isspace())
print("-------------------------------------------------------")

print("hello".isupper())
print("hello".islower())
print("HELLO".isupper())
print("HELLO".islower())
print("hello World".istitle())
print("Hello world".istitle())
print("Hello World".istitle())
print("-------------------------------------------------------")

"""

# 6) Alignment & Formatting :
"""
s = "hi"
print(s.center(10, "$"))
s = "hii"
print(s.center(10, "$"))
s = "hiii"
print(s.center(10, "$"))
s = "hiii"
print(s.center(2, "$"))

s = "hi"
print(s.ljust(10, "$"))
print(s.rjust(10, "$"))

s = "43"
print(s.zfill(1))
print(s.zfill(5))

"""

name = "Ram"
age = 21

print("Name is", name, "and age is", age)
print("Name is {} and age is {}".format(name, age))
print("Name is {} and age is {}".format(age, name))
print("Name is {name} and age is {age}".format_map({"name": "Ram", "age": 21}))
print("Name is {name} and age is {age}".format_map({"name": name, "age": age}))

s2 = "Mississippi"
print(len(s2))

print(f"Name is {name} and age is {age}")
print("My name is %s and I am %d years old." % (name, age))
print("My name is %s and I am %d years old." % (age, name))
