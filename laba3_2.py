class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name_ = name
        self.author_ = author
    @property
    def name(self):
        return self.name
    def author(self):
        return self.author
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages):
        super().__init__(name, author)
        if not isinstance(pages, int):
          raise TypeError("Число страниц должно быть целым числом")
        if pages<=0:
          raise ValueError("Число страниц не может быть неположительным числом")
        self.pages = pages
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.author!r}, {self.pages!r})'
class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
          raise TypeError("Длительность должна быть дробным числом")
        if duration<=0:
          raise ValueError("Длительность не может быть неположительным числом")
        self.duration = duration
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.author!r}, {self.duration!r})'

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"