import doctest
from typing import Union

class Box:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Коробка"
        :param capacity_volume: Объем коробки
        :param occupied_volume: Занятый объём
        Примеры:
        >>> box = Box(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем коробки должен быть численным")
        if capacity_volume <= 0:
            raise ValueError("Объем коробки не может быть отрицательным")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Занимаемый объем коробки должен быть численным")
        if occupied_volume < 0:
            raise ValueError("Занимаемый объем коробки не может быть отрицательным")
        self.occupied_volume = occupied_volume

    def is_empty_box(self) -> bool:
        """
        Функция которая проверяет есть ли что то в коробке
        :return: Наличие чего ли в коробке
        Примеры:
        >>> box = Box(500, 0)
        >>> box.is_empty_box()
        """
        ...

    def add_something_to_box(self, something: float) -> None:
        """
        Добавление чего либо в коробку.
        :param something: Объем добавляемого объекта
        :raise ValueError: Если объем добавляемого предмета больше объема коробки, то вызываем ошибку
        Примеры:
        >>> box = Box(500, 0)
        >>> box.add_something_to_box(200)
        """
        if not isinstance(something, (int, float)):
            raise TypeError("Добавляемый предмет должен быть численным")
        if something < 0:
            raise ValueError("Объем добавляемого предмета не может быть отрицательным")
        ...

    def remove_something_from_box(self, estimate_something: float) -> None:
        """
        Извлечение чего либо из коробки
        :param estimate_something: Объем извлекаемой жидкости
        :raise ValueError: Если объем извлекаемого предмета превышает объем предметов в коробке,
        то возвращается ошибка.
        :return: Объем реально извлеченных предметов
        Примеры:
        >>> box = Box(500, 500)
        >>> box.remove_something_from_box(200)
        """
        ...


class Dog:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Собака"
        :param name: Имя собаки
        :param age: Возраст собаки
        Примеры:
        >>> Jack = Dog("Jack", 3)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя собаки может быть только строкой")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст собаки должен быть целочисленным")
        if age < 0:
            raise ValueError("Возраст собаки не может быть отрицательным")
        self.age = age

    def sit(self) -> bool:
        """
        Собака садится по команде
        :return: "self.name" Сидит по команде
        Примеры:
        >>> Jack = Dog("Jack", 3)
        >>> Jack.sit()
        """
        ...

    def paw(self) -> bool:
        """
        Собака дает лапу по команде
        :return: "self.name" дает лапу
        Примеры:
        >>> Jack = Dog("Jack", 3)
        >>> Jack.paw()
        """
        ...


class Car:
    def __init__(self, color: str, max_mph: int, model: dict):
        """
        Создание и подготовка к работе объекта "Машина"
        :param color: Цвет машины
        :param max_mph: Максимальная скорость машины
        :param model: Характеристики машины
        Примеры:
        >>> Ford_Focus = Car("Black", 3, {"Type": "Oil"})  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет машины может быть только строкой")
        self.color = color

        if not isinstance(max_mph, int):
            raise TypeError("Максимальная скорость автомобиля должна быть целочисленной")
        if max_mph < 0:
            raise ValueError("Возраст собаки не может быть отрицательным")
        self.max_mph = max_mph

        if not isinstance(model, dict):
            raise TypeError("Характеристика автомобиля может быть только библиотекой")
        self.model = model

    def start_engine(self) -> bool:
        """
        Машина заводится
        :return: Машина заведена
        Примеры:
        >>> Ford_Focus = Car("Black", 3, {"Type": "Oil"})
        >>> Ford_Focus.start_engine()
        """
        ...

    def stop_engine(self) -> bool:
        """
        Заглушить двигатель
        :return: Машина заглушена
        Примеры:
        >>> Ford_Focus = Car("Black", 3, {"Type": "Oil"})
        >>> Ford_Focus.stop_engine()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации