class Book:

    def __init__(self, name: str, author: str):
        self._name = None
        self._author = None
        self.name = name
        self.author = author

    @property
    def name(self) -> str:

        return self._name

    @name.setter
    def name(self, value: str) -> None:

        if not isinstance(value, str):
            raise ValueError("Имя книги должно быть строкой.")
        if not value.strip():
            raise ValueError("Имя книги не может быть пустым.")
        self._name = value

    @property
    def author(self) -> str:

        return self._author

    @author.setter
    def author(self, value: str) -> None:

        if not isinstance(value, str):
            raise ValueError("Имя автора должно быть строкой.")
        if not value.strip():
            raise ValueError("Имя автора не может быть пустым.")
        self._author = value

    def __str__(self) -> str:

        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:

        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Сеттер устанавливает значение pages

    @property
    def pages(self) -> int:

        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:

        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self._pages = value

    def __str__(self) -> str:

        return f"{super().__str__()}, Страниц: {self.pages}"

    def __repr__(self) -> str:

        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, pages={self.pages})")


class AudioBook(Book):

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:

        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:

        if not isinstance(value, (int, float)):
            raise ValueError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self) -> str:

        return f"{super().__str__()}, Продолжительность: {self.duration} ч."

    def __repr__(self) -> str:

        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, duration={self.duration})")
