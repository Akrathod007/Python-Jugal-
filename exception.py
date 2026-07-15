"""

print("Start")

try:
    no1 = int(input("Enter a number 1 : "))
    no2 = int(input("Enter a number 2 : "))
    print(no1 / no2)
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("invalid number")
print("End")


try:
    num = int(input("Enter Number: "))
    print(10 / num)

except (ValueError, ZeroDivisionError):
    print("Invalid Input")


try:
    # x = 10 / 0
    print(int("ten"))

except Exception as e:
    print("Error:", e)


try:
    num = int(input("Enter Number: "))
    result = 10 / num

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result =", result)

"""

try:
    print(10 / 0)

except:
    print("Error")

finally:
    print("Always Executes")

# print(x)

import pandas
