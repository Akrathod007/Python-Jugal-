# import math

# print(math.pi)
# print(math.e)

# print(math.pow(2, 5))
# print(math.sqrt(25))
# print(math.cbrt(27))


# import math as m

# print(m.pi)
# # print(math.pi)
# print(m.ceil(3.4))
# print(m.floor(3.4))
# print(m.floor(-2.4))
# print(m.ceil(-2.4))

# print(m.trunc(1.22))
# print(round(3.4))
# print(round(3.5))
# print(round(1.25))
# print(round(1.65))

# print(m.gcd(12, 18))
# # 12 -> 1,2,3,4,6,12
# # 18 -> 1,2,3,6,9,18
# print(m.lcm(12, 18))

# print(m.factorial(5))
# print(m.factorial(20))

# print(m.fabs(-3.4))
# print(m.fmod(4, 2))
# print(m.fmod(3.1, 2))

# print(m.log(100))
# print(m.log10(100))
# print(m.log2(100))

# x = float("-inf")
# y = float("inf")


# print(y > 10000000000000000000000000000000000000000000000000000000000000000000000000)
# print(y < 10000000000000000000000000000000000000000000000000000000000000000000000000)


# from math import pow
# from math import pow, sqrt
# from math import pow as p, sqrt
# from math import *

# print(pow(2, 5))
# # print(p(2, 10))
# print(sqrt(25))
# print(ceil(3.4))


import random as r
import math as m

# print(r.random())
# print(r.random() * 11)
# print(m.trunc(r.random() * 11))
# print(int(r.random() * 11))

# print(r.randint(1, 10))
# print(r.randint(10, 1)) # Error

# print(r.randrange(1, 11))
# print(r.randrange(1, 11, 2))
# print(r.randrange(1, 11, 4))


# colors = ["red", "green", "blue", "yellow"]
# print(colors)
# print(r.choice(colors))

# name = "Doremon"
# print(r.choice(name))

# print(r.choices(colors, k=5))
# # print(r.sample(colors, k=3))
# # print(r.sample(colors, k=5))


# nums = [1, 2, 3, 4, 5, 6, 7]
# r.shuffle(nums)
# print(nums)

# print(r.uniform(1.1, 5.5))


"""
1. Write a program to generate a 4-digit OTP.

2. Write a program to make Lottery Game :

Generate 5 random numbers (1 - 50).
li = [34,23,45,12,37]

Ask user to guess numbers.
for i in range(1,16):

    no = 55
    match = 2
Check how many matches.

3. Write a program to generate a random HEX color code like #A3F4C1.

4. Write a program to guess the Number Game

randomNo = 1 to 25 (18)

while True:
    no = 16 -> Too Low
    no -> 20 -> To High
    no = 18 -> Break
 


5. Write a program to make Rock Paper Scissors game

com = rock
user = paper

if com == user:
    draw

if (user == "R" and com == "S") or (user == "P" and com == "R") or (user == "S" and com == "p"):
    user win
else
    com win

"""


# import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.punctuation)
# print(string.whitespace)


# Count digits in a string :
# Count alphabets in a string :

import datetime as dt

today = dt.date.today()
print(dt.date.today())
t = dt.datetime.now()
print(dt.datetime.now())

d = dt.date(2025, 1, 1)
print(d)

d_t = dt.datetime(2025, 12, 1, 15, 30, 45)
print(d_t)

print("Year :", today.year)
print("Month :", today.month)
print("Day :", today.day)
print("Hour :", t.hour)
print("Minute :", t.minute)
print("Second :", t.second)
print("MicroSecond :", t.microsecond)

print(t.strftime("%d-%m-%Y"))
print(t.strftime("%d-%m-%y"))
print(t.strftime("%A"))
print(t.strftime("%a"))
print(t.strftime("%B"))
print(t.strftime("%b"))
print(t.strftime("%H$%p"))
print(t.strftime("%I %p"))
print(t.strftime("%H:%M:%S.%f"))
print(t.strftime("%j"))
print(t.strftime("%U"))
print(t.strftime("%W"))
print(t.strftime("%c"))
print(t.strftime("%x"))
print(t.strftime("%X"))


today = dt.date.today()
new_date = today + dt.timedelta(days=5)

print(new_date)

d1 = dt.date(2026, 2, 8)
d2 = dt.date(2026, 2, 1)

diff = d1 - d2
print(diff)
print(diff.days)

time_now = dt.datetime.now().time()
print(time_now)

date_string = "08-02-2026"
date_obj = dt.datetime.strptime(date_string, "%d-%m-%Y")

print(date_obj)


print("---------------------------------------------------")

today = dt.date.today()
print(today)
new_year = dt.date(2027, 1, 1)
print(new_year)

diff = new_year - today
print(diff.days)

import datetime

today = datetime.date.today()
next_year = today.year + 1

new_year = datetime.date(next_year, 1, 1)
days_left = (new_year - today).days

print("Days left for New Year:", days_left)


x1 = 10
y1 = 20
x2 = 5
y2 = 10

if (x1, y1) > (x2, y2):
    print("Hello")
