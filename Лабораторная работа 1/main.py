import doctest

class Rock:
    def __init__(self, size: float, location: str):
        """
        Создание и подготовка к работе объекта "Камень"
        :param size: Размер камня
        :param location: Местоположение камня
        Примеры:
        >>> pebble = Rock(1.2, "Beach")  # инициализация экземпляра класса
        """
        if not isinstance(size, float):
            raise TypeError("Размер камня может быть только числом")
        self.size = size
        if not isinstance(location, str):
            raise TypeError("Местоположение камня может быть только строкой")
        self.location = location

    def throw(self) -> bool:
        """
        Кинуть камень
        Примеры:
        >>> pebble = Rock(1.2, "Beach")
        >>> pebble.throw()
        """
        ...

    def take(self) -> bool:
        """
        Поднять камень
        Примеры:
        >>> pebble = Rock(1.2, "Beach")
        >>> pebble.take()
        """
        ...


class Hamster:
    def __init__(self, name: str, color: str):
        """
        Создание и подготовка к работе объекта "Хомяк"
        :param name: Имя хомяка
        :param age: Возраст Хомяка
        Примеры:
        >>> pip = Hamster("Pip", "Black")  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя хомяка может быть только строкой")
        self.name = name

        if not isinstance(color, str):
            raise TypeError("Цвет хомяка может быть только строкой")
        self.color = color

    def feed(self) -> str:
        """
        Покормить Хомяка
        :return: "self.name" кушает. Повторите эту команду через час
        Примеры:
        >>> pip = Hamster("Pip", "Black")
        >>> pip.feed()
        """
        ...

    def wakeup(self) -> str:
        """
        Разбудить Хомяка
        :return: "self.name" недоволен
        Примеры:
        >>> pip = Hamster("Pip", "Black")
        >>> pip.wakeup()
        """
        ...


class Cup:
    def __init__(self, capacity_vol: int, occupied_vol: int):
        """
        Создание и подготовка к работе объекта "Чашка"
        :param capacity_vol: Объем чашки
        :param occupied_vol: Наполненный объем чашки
        Примеры:
        >>> teacup = Cup(5, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_vol, int):
            raise TypeError("Объем чашки должен быть целочисленным")
        if capacity_vol <= 0:
            raise ValueError("Объем чашки не может быть отрицательным")
        self.capacity_vol = capacity_vol

        if not isinstance(occupied_vol, int):
            raise TypeError("Занимаемый объем чашки должен быть численным")
        if occupied_vol < 0:
            raise ValueError("Занимаемый объем чашки не может быть отрицательным")
        self.occupied_vol = occupied_vol


    def add_water(self, water: int) -> None:
        """
        Добавление воды в рюкзак.
        :param water: Объем добавляемой воды
        :raise ValueError: Если количество добавляемых сендвичей больше объема рюкзака
        Примеры:
        >>> teacup = Cup(5, 0)
        >>> teacup.add_water(3)
        """
        if not isinstance(water, int):
            raise TypeError("Объем добавляемой воды должен быть целым")
        if water < 0:
            raise ValueError("Объем добавляемой воды не может быть отрицательным")
        ...

    def drink(self, volume: int) -> int:
        """
        Сделать глоток из чашки
        :param volume: Размер глотка
        :raise ValueError: Если размер глотка превышает объем жидкости в чашке,
        то возвращается ошибка.
        :return: Оставшийся объем в чашке
        Примеры:
        >>> teacup = Cup(5, 4)
        >>> teacup.drink(2)
        """
        ...



if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    
