"""

day = int(input("Enter a day number between 1 to 7 : "))

match day:
    case 1:
        print("MON")
    case 2:
        print("TUE")
    case 3:
        print("WED")
    case 4:
        print("THU")
    case 5:
        print("FRI")
    case 6:
        print("SAT")
    case 7:
        print("SUN")
    case _:
        print("Invalid Day Number")

"""

# ch = input("Enter a character : ")
"""
match ch:
    
    
    case "A":
        print("Vowel")
    case "a":
        print("Vowel")
    case "E":
        print("Vowel")
    case "e":
        print("Vowel")
    case "I":
        print("Vowel")
    case "i":
        print("Vowel")
    case "O":
        print("Vowel")
    case "o":
        print("Vowel")
    case "U":
        print("Vowel")
    case "u":
        print("Vowel")

"""

"""
match ch:

    case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u":
        print("Vowel")
    case _:
        print("Not Vowel")

"""
"""
num = 12

match num:
    case n if n % 2 == 0:
        # print(f"{n} is Even")
        print(n, "is Even")
    case n if n % 2 != 0:
        print(f"{n} is Odd")

"""

print("1 -> Gujarati")
print("2 -> Punjabi")
print("3 -> South Indian")
print("4 -> Chinese")
print("5 -> Italian")

ch = int(input("Enter Your Choice : "))
total_bill = 0
match ch:
    case 1:
        print("You Selected Gujarati")
        print("1 -> Dal Dhokli")
        print("2 -> Jalebi-Fafda")
        print("3 -> Undhiyu")
        ch2 = int(input("Enter a choice in gujarati : "))
        match ch2:
            case 1:
                print("You Selected Dal Dhokli")
            case 2:
                print("You Selected Dal Jalebi-Fafda")
            case 3:
                print("You Selected Dal Undhiyu")
        qty = int(input("How Much Do You Want : "))
        if ch2 == 1:
            total_bill = qty * 50
        elif ch2 == 2:
            total_bill = qty * 70
        elif ch2 == 3:
            total_bill = qty * 120

    case 2:
        print("You Selected Punjabi")
    case 3:
        print("You Selected South Indian")
    case 4:
        print("You Selected Chinese")
    case 5:
        print("You Selected Italian")


print("Total Bill :", total_bill)
