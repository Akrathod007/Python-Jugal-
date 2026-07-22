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

"""
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
"""

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# s1 = Student("Ram", 24)
# print(s1.age)
# s1.age = 26
# print(s1.age)

# del s1.age
# print(s1.age)

"""
class Student:
    school = "XYZ School"

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Ram", 24)
s2 = Student("Shyam", 23)

print("Student 1 Name : ", s1.name)
print("Student 1 Age : ", s1.age)
print("Student 2 Name : ", s2.name)
print("Student 2 Age : ", s2.age)

print(s1.school)
print(s2.school)


class Person:
    lastname = ""

    def __init__(self, name):
        self.name = name


p1 = Person("Ram")
p2 = Person("Shyam")

Person.lastname = "Pandey"

print(p1.lastname)
print(p2.lastname)


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)


p1 = Person("Manan")
p1.greet()


class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")

    def __str__(self):
        return f"{self.name} and {self.age}"


p1 = Person("Ram", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

print(p1)

"""


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")

    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f"- {song}")


my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()

party_Playlist = Playlist("Party")
party_Playlist.add_song("XYZ")
party_Playlist.add_song("ABC")
party_Playlist.show_songs()
party_Playlist.remove_song("XYZ")
party_Playlist.show_songs()


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello!")


p1 = Person("Emil")

# del Person.greet

# p1.greet()
