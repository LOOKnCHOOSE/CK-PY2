class Forest:
    def __init__(self, capacity: int, area: (int, float)):
        """
        Создание базового класса "Лес"
        :param capacity: Численность деревьев в лесу
        :param area: Площадь
        """
        self._capacity = None  # protected
        self._init_capacity(capacity)
        self._area = None  # protected
        self._init_area(area)

    def __str__(self) -> str:
        return f"Лес: Численность леса {self.capacity} (шт), площадь леса {self.area} (кв.м)."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(capacity={self.capacity},area={self.area})"

    def _init_capacity(self, capacity: int) -> None:
        """
        Инициализация атрибута _capacity:
        Protected: используется только при инициализации экземпляра класса
        :param capacity: Численность лесного массива
        """
        if not isinstance(capacity, int):
            raise TypeError('Численность леса должна быть типа int')
        if capacity < 0:
            raise ValueError('Численность леса должна быть не меньше 0')
        self._capacity = capacity

    def _init_area(self, area: (int, float)) -> None:
        """
        Инициализация атрибута _area:
        Protected: используется только при инициализации экземпляра класса
        :param area: Площадь леса
        """
        if not isinstance(area, (int, float)):
            raise TypeError('Площадь леса должна быть типа int или float')
        if area <= 0:
            raise ValueError('Площадь леса должна быть больше 0')
        self._area = area

    @property
    def capacity(self) -> int:
        """
        Используем getter для атрибута _capacity (не setter: protected атрибут)
        """
        return self._capacity

    @property
    def area(self) -> (int, float):
        """
        Используем getter для атрибута _volume (не setter: protected атрибут)
        """
        return self._area

    def plant_trees(self, tree: int) -> None:
        """
        Высаживаем большее количество деревьев
        :param tree: количество саженцев
        """
        if not isinstance(tree, int):
            raise TypeError('Количество саженцев должно быть типа int')
        if tree < 0:
            raise ValueError('Количество саженцев должно быть не меньше 0')
        self._capacity += tree

    def forest_fire(self, fire_area: (int, float)) -> None:
        """
        В жаркую погоду и при человеческом факторе, возможно возникновение лесных пожаров
        :param fire_area: Область горения
        """
        if not isinstance(fire_area, (int, float)):
            raise TypeError('Область горения должна быть типа int или float')
        if fire_area < 0:
            raise ValueError('Время в пути должно быть не меньше 0')
        ...


class RainForrest(Forest):
    def __init__(self, capacity: int, area: (int, float), country: str):
        """
        Создание дочернего класса "Джунгли", унаследован от класса "Лес"
        :param capacity: Численность деревьев класса "Джунгли"
        :param area: Площадь "Джунглей"
        :param country: Страна расположения "Джунглей"
        """
        super().__init__(capacity, area)
        self._country = None  # protected: константа для конкретного танкера
        self._init_country(country)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(capacity={self.capacity},area={self.area}," \
               f"type={self._country})"

    def _init_country(self, country: str) -> None:
        """
        Инициализация атрибута _country - Страна расположения "Джунглей"
        Protected: используется только при инициализации экземпляра класса
        :param country: Страна расположения "Джунглей"
        """
        if not isinstance(country, str):
            raise TypeError('Страна расположения "Джунглей" может быть только str ')

        self._country = country

    @property
    def placement(self) -> str:
        """
        Используем getter для атрибута _country (не setter: protected атрибут)
        """
        return self._country

    def forest_fire(self, fire_area: (int, float)) -> None:
        """
        В жаркую погоду возможно возникновение лесных пожаров
        Перегрузка метода базового класса ввиду того, что человеческий фактор редко является причиной возникновения пожара и его распространения
        :param route_time: время в пути
        """
        if not isinstance(fire_area, (int, float)):
            raise TypeError('Область горения должна быть типа int или float')
        if fire_area < 0:
            raise ValueError('Область горения должна быть не меньше 0')
        ...


if __name__ == "__main__":
    # Write your solution here
    pass
