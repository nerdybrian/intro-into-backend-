class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sound(self):
      print("i dont know who i am")
class Dog(Pet):
    def sound(self):
        print(f"my name is{self.name} and my age is {self.age}")
class Cat(Pet):
    def sound(self):
        print(f"my name is{self.name} and my age is {self.age}")
class fish(Pet):
    pass

pet1 = Dog("dog a","12")
pet1.sound()

pet2 = Cat("dog b", "13")
pet2.sound()

pet3 = fish("fish", "17")
pet3.sound()

#create a class student