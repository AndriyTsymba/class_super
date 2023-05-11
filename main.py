# Успадккування класів
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name,"is eating")
class Dog(Animal):
    def __init__(self,name,age,bread):
        super().__init__(name,age)
        self.breed = bread
    def bark(self):
        print(self.name + "is barking")
dog = Dog("ronik",3,"korgi")
print(dog.name)
print(dog.age)
print(dog.breed)
dog.eat()
dog.bark()
#2
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"name{self.name},age {self.age}"
class Student(Person):
    def __init__(self,name,age,student_id):
      super().__init__(name,age)
      self.student_id = student_id
    def __str__(self):
        return super().__str__() + f" student_id {self.student_id}"
student1 = Student('Andriy',21,45453)
print(student1)
with open("info_student.txt","w") as file:
    file.write(str(student1))