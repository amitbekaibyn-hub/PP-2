class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"My name is: {self.name}, age: {self.age}, grade: {self.grade}")
s1=Student("Aibyn",18,1)
s1.introduce()
    
class Doctor:
    def __init__(self, name, age,profession, hospital):
        super().__init__(name,age)
        self.profession = profession
        self.hospital = hospital


    def introduce(self):
        print(f"my profession is:{self.profession},and hospital is:{self.hospital} ")
d1=Doctor("Merei","doctor",29)
d1.introduce()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f"Hi my name is:{self.name}")
p1=Person("Samat",18)
p1.introduce()


class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
