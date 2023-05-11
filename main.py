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