# class Student:
#     name = "Raj"
#     age = 25

#     def display(self):
#         print(f"{self.name} and {self.age}")


# s1 = Student()
# print(s1.name)
# print(s1.age)

# s1.display()

# s2 = Student()
# s2.name = "Ram"
# s2.age = 29
# s2.display()

# s3 = Student()
# s3.name = "Manan"
# s3.age = 30
# s3.display()


class Student:
    # def __init__(self):
    #     print("Hello")
    # self.name = "Ram"
    # self.age = 23

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} and {self.age}")


s1 = Student("Ram", 25)
s1.display()

s2 = Student("Shyam", 30)
s2.display()

s3 = Student("Raj", 24)
s3.display()


class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age


p1 = Person("Ram")
p2 = Person("Shyam", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)


class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def greet(self):
        print(self)
        print("Hello, my name is " + self.name)


p1 = Person("Ram", 30, "Ahm", "India")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
p1.greet()
print(p1)


class Person:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def greet(abc):
        print("Hello, my name is " + abc.name)


p1 = Person("Emil", 36)
p1.greet()


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")


car1 = Car("BenZ", "Maybec", 2020)
car1.display_info()


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome")


p1 = Person("Tilak")
p1.welcome()
