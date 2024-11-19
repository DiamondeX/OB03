class ZooEmployee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class ZooKeeper(ZooEmployee):
    def feed_animal(self, animal):
        print(f"{self.name} feeds {animal.name}.")

class Veterinarian(ZooEmployee):
    def heal_animal(self, animal):
        print(f"{self.name} heals {animal.name}.")