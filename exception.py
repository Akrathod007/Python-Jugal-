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

# try:
#     print(10 / 0)

# except:
#     print("Error")

# finally:
#     print("Always Executes")

# print(x)


age = 5

if age < 0:
    raise ValueError("Age can not be negative")

print("Valid Age")


balance = 500
withdraw = 1000

try:
    if withdraw > balance:
        raise Exception("Insufficient Balance")
except Exception as e:
    print("Error :", e)


try:
    age = int(input("Enter Age: "))

    if age < 18:
        raise ValueError("You are not eligible")

    print("Eligible")

except ValueError as e:
    print("Error:", e)


class InvalidMarksError(Exception):
    pass


marks = -10

# if marks < 0:
#     raise InvalidMarksError("Marks cannot be negative")

try:
    if marks < 0:
        raise InvalidMarksError("Marks cannot be negative")
except InvalidMarksError as e:
    print("Error :", e)


balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise Exception("Insufficient Balance")

    balance -= amount
    print("Remaining Balance:", balance)

except Exception as e:
    print(e)


try:
    print("Outer Try")

    try:
        print(10 / 0)

    except ZeroDivisionError:
        print("Inner Except: Cannot divide by zero")

except:
    print("Outer Except")


try:
    print("Outer Try")

    try:
        num = int("abc")

    except ZeroDivisionError:
        print("Inner Except")

except ValueError:
    print("Outer Except: Invalid Number")


try:
    file = open("data.txt")

    try:
        data = int(file.read())
        print(data)

    except ValueError:
        print("File contains invalid data")

    finally:
        file.close()
        print("File Closed")

except FileNotFoundError:
    print("File Not Found")
