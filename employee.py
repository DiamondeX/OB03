class ZooEmployee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # специальный метод для сохранения объекта
    def __getstate__(self):
        return self.__dict__

    # специальный метод для восстановления объекта
    def __setstate__(self, state):
        self.__dict__ = state

class ZooKeeper(ZooEmployee):
    def feed_animal(self, animal):
        print(f"{self.name} feeds {animal.name}.")

class Veterinarian(ZooEmployee):
    def heal_animal(self, animal):
        print(f"{self.name} heals {animal.name}.")