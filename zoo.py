import json
from animal import Animal, Bird, Mammal, Reptile
from employee import ZooEmployee, ZooKeeper, Veterinarian


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

    # Новые функции для сохранения и загрузки состояния зоопарка

def save_zoo_state(zoo, filename="zoo_state.json"):
    with open(filename, 'w') as file:
        state = {
            "name": zoo.name,
            "animals": [{"name": a.name, "age": a.age, "type": type(a).__name__} for a in zoo.animals],
            "employees": [{"name": e.name, "position": e.position, "type": type(e).__name__} for e in zoo.employees]
        }
        json.dump(state, file)

def load_zoo_state(filename="zoo_state.json"):
    from animal import Bird, Mammal, Reptile
    from employee import ZooKeeper, Veterinarian
    with open(filename, 'r') as file:
        data = json.load(file)
        zoo = Zoo(data["name"])
        class_map = {
            "Bird": Bird,
            "Mammal": Mammal,
            "Reptile": Reptile,
            "ZooKeeper": ZooKeeper,
            "Veterinarian": Veterinarian
        }

        for animal_data in data["animals"]:
            animal_class = class_map[animal_data["type"]]
            zoo.add_animal(animal_class(name=animal_data["name"], age=animal_data["age"]))

        for employee_data in data["employees"]:
            employee_class = class_map[employee_data["type"]]
            zoo.add_employee(employee_class(name=employee_data["name"], position=employee_data["position"]))

        return zoo