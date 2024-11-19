class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass  # This is here to be overridden by subclasses

    def eat(self):
        print(f"{self.name} is eating.")

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print(f"{self.name} chirps!")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} makes a mammal sound!")

class Reptile(Animal):
    def __init__(self, name, age, cold_blooded=True):
        super().__init__(name, age)
        self.cold_blooded = cold_blooded

    def make_sound(self):
        print(f"{self.name} hisses!")