#1
import  random
class Animal:
    def __init__(self,species,name, age, health, hunger, happiness):
        super().__init__()
        self.species = species
        self.name = name
        self.age = age
        self.health = health
        self.hunger = hunger
        self.happiness = happiness

    def  grow(self):
        self.age += 5
        self.health = random.randint(0,10)
        self.hunger = random.randint(0,10)
        self.happiness = random.randint(0,10)
    def eat(self):
        if self.health >= 6:
            self.health +=  random.randint(0,5)
            self.happiness +=  random.randint(0,5)
            self.hunger +=  random.randint(0,5)
        else:


            print(f"{self.name},not hungry")
    def play(self):
        pass








class Zoo(Animal):
    def __init__(self,species,name, age, health, hunger, happiness,animals):
        super().__init__(species,name, age, health, hunger, happiness)
        self.animals = []










