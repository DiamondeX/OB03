import pickle
from animal import Animal
from employee import ZooEmployee

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            print("This is not an animal!")

    def add_employee(self, employee):
        if isinstance(employee, ZooEmployee):
            self.employees.append(employee)
        else:
            print("This is not an employee!")

# Функции для сохранения и загрузки состояния зоопарка

def save_zoo(zoo, filename="zoo_state.pkl"):
    with open(filename, 'wb') as file:
        pickle.dump(zoo.__dict__, file)

def load_zoo(filename="zoo_state.pkl"):
    with open(filename, 'rb') as file:
        state = pickle.load(file)
    zoo = Zoo(state['name'])
    for animal in state['animals']:
        zoo.add_animal(animal)
    for employee in state['employees']:
        zoo.add_employee(employee)
    return zoo
