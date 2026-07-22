class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # private variable

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)


s = Student("Ansh", 90)
s.display()
# s.__marks


class Student:

    def __init__(self):
        self.__marks = 0

    def set_marks(self, m):
        self.__marks = m

    def get_marks(self):
        return self.__marks


s = Student()

s.set_marks(95)
print("Marks:", s.get_marks())
