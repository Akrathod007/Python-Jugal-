def sayHi():
    print("Hello")


def add(a, b):
    return a + b


def prime(n):
    f = 0

    for i in range(1, n + 1):
        if n % i == 0:
            f += 1

    if f == 2:
        print("Prime")
    else:
        print("Not Prime")


def printCounting(n):
    for i in range(1, n + 1):
        print(i)


def swapChar(ch):
    if ch >= "A" and ch <= "Z":
        ch = chr(ord(ch) + 32)
    elif ch >= "a" and ch <= "z":
        ch = chr(ord(ch) - 32)

    return ch


import string
