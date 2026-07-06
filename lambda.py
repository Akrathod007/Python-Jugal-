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


# def demo(n):
#     if n > 0:
#         return "Pos"
#     elif n < 0:
#         return "Neg"
#     else:
#         return "Zero"


# print(demo(10))

# demo2 = lambda n: "Pos" if n > 0 else "Neg" if n < 0 else "Zero"
# print(demo2(-10))


# login = lambda user, pwd: (
#     "Admin Login"
#     if user == "admin" and pwd == "007"
#     else "User Login" if user == "user" and pwd == "xyz" else "Invalid Login"
# )

# print(login("admin", "123"))
# print(login("admin", "007"))
# print(login("user", "xyz"))


li = [1, 2, 3, 4, 5]


def demo(x):
    return x * 2


# result = list(map(lambda x: x * 2, li))
# result = list(map(demo, li))
# print(result)

r = list(map(lambda n: "Even" if n % 2 == 0 else "Odd", li))
print(r)


"""
Create a list of numbers and use map() to find squares of all numbers.

Create a list of numbers and use map() to convert all numbers into strings.

Given a list of temperatures in Celsius, use map() to convert them into Fahrenheit.

Create a list of names and use map() to convert all names into uppercase.

Given a list of strings, use map() to find the length of each string.

Create a list of numbers and use map() to add 10 to every element.

Given a list of words, use map() to reverse each word.

Create a list of prices and use map() to add 18% GST to every price.

Create a list of integers and use map() to check whether each number is even or odd.
"""


li = [1, 2, 3, 4, 5, 6, 7, 8]

r = list(filter(lambda x: x % 2 == 0, li))
print(r)


evenOdd = [
    list(filter(lambda x: x % 2 == 0, li)),
    list(filter(lambda x: x % 2 != 0, li)),
]
print(evenOdd)

from functools import reduce

nums = [1, 2, 3, 4, 5]

s = reduce(lambda a, b: a + b, nums)
# s = reduce(lambda a, b: a + b, nums, 10)
m = reduce(lambda a, b: a if a > b else b, nums)
print(m)
"""
a = 1,b= 2
a + b -> 3

a - > 3 , b -> 3
a + b -> 6

a -> 6
b -> 4
a + b -> 10

a -> 10
b -> 5
a + b -> 15
"""

print(s)


"""
Filter Task :

1. Filter Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

2. Filter Odd Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

3. Filter Positive Numbers
numbers = [-5, 10, -2, 8, 0]

4. Filter Names Starting With A
names = ["Akshay", "Rahul", "Amit", "Karan"]

5. Filter Strings With Length More Than 5
words = ["apple", "banana", "kiwi", "mango"]

6. Filter Vowels From List
letters = ['a', 'b', 'e', 'f', 'i']

7. Filter Palindrome Words
words = ["madam", "python", "level", "code"]

8. Filter Uppercase Words
words = ["HELLO", "Python", "WORLD", "Code"]

9. Filter Alphabet Characters
data = ['A', '1', 'B', '9', 'C']

10. Filter Strings Containing Letter "a"
words = ["apple", "mango", "berry", "banana"]


Reduce Task :

1. Concatenate Strings
words = ["Python", "is", "awesome"]

2. Reverse a String
word = "python"

3. Find Total Digits in List
numbers = [123, 45, 6789]

4. Find Highest Marks
marks = [45, 78, 90, 66, 88]

5. Count Total Words Length
words = ["python", "java", "c"]




1. Square Even Numbers and Find Sum

2. Sum of Cubes of Positive Numbers

3. Find Sum of Squares of Odd Numbers

4. Find Largest Square of Even Numbers

5. Reverse Long Words and Join
Filter words whose length is greater than 4.

"""

# 1. Square Even Numbers and Find Sum
li = [1, 2, 3, 4, 5, 6]

# even = list(filter(lambda x: x % 2 == 0, li))
# print(even)

# square = list(map(lambda x: x * x, even))
# print(square)

# s = reduce(lambda a, b: a + b, square)
# print(s)

s = reduce(
    lambda a, b: a + b,
    list(map(lambda x: x * x, list(filter(lambda x: x % 2 == 0, li)))),
)

print(s)
