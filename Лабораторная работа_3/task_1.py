class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Возвращаем название книги."""
        return self._name

    @name.setter
    def name(self, name) -> None:
        """Изменяем название книги."""
        if not isinstance(name, str):  # Используем проверку
            raise TypeError('Название книги должно быть str!')
        self._name = name

    @property
    def author(self) -> str:
        """Возвращаем автора книги."""
        return self._author

    @author.setter
    def author(self, author) -> None:
        """Изменяем автора книги."""
        if not isinstance(author, str):  # Используем проверку
            raise TypeError('Имя автора должно быть str!')
        self._author = author

    def __str__(self):  # Наследование
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):  # Наследование
    """Бумажная книга"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        """Возвращаем число страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """Изменяем число страниц в книге."""
        if not isinstance(pages, int):  # Используем проверку данных
            raise TypeError('Число страниц должно быть int!')
        if pages <= 0:
            raise ValueError('Число страниц должно быть положительным!')
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):  # Наследование
    """Аудио книга"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        """Возвращаем длительность аудио книги."""
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        """Изменяем длительность аудио книги."""
        if not isinstance(duration, float):  # Используем проверку данных
            raise TypeError('Продолжительность книги должна быть int!')
        if duration <= 0:
            raise ValueError('Продолжительность книги должна быть положительной!')
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    
