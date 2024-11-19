from zoo import Zoo, animal_sound, save_zoo, load_zoo
from animal import Bird, Mammal, Reptile
from employee import ZooKeeper, Veterinarian

if __name__ == "__main__":
    zoo = Zoo("Wildlife Park")

    # Добавление животных
    zoo.add_animal(Bird("Sparrow", 1, 0.2))
    zoo.add_animal(Mammal("Lion", 5, "gold"))
    zoo.add_animal(Reptile("Snake", 3))

    # Добавление сотрудников
    zoo.add_employee(ZooKeeper("John Doe", "Zookeeper"))
    zoo.add_employee(Veterinarian("Dr. Jane", "Veterinarian"))

    # Демонстрация полиморфизма
    animal_sound(zoo.animals)

    # Сохранение состояния
    save_zoo(zoo)

    # Загрузка состояния
    loaded_zoo = load_zoo()
    print(loaded_zoo.name)  # Должно вывести "Wildlife Park"

    # Проверка после загрузки
    animal_sound(loaded_zoo.animals)