import doctest


class Person:
    """
    Класс для представления человека.

    Атрибуты:
    name (str): Имя человека.
    age (int): Возраст человека.

    Методы:
    greet(): Приветствует человека по имени.
    """

    def __init__(self, name: str, age: int):
        """
        Инициализация объекта Person.

        :param name: Имя человека.
        :param age: Возраст человека.
        """
        self.name = name
        self.age = age

    def greet(self) -> str:
        """
        Приветствует человека по имени.

        :return: Строка приветствия.

        Пример:
        >>> person = Person("Иван", 30)
        >>> person.greet()
        'Привет, Иван!'
        """
        return f"Привет, {self.name}!"


class Car:
    """
    Класс для представления автомобиля.

    Атрибуты:
    model (str): Модель автомобиля.
    year (int): Год выпуска автомобиля.

    Методы:
    car_info(): Возвращает информацию о машине.
    """

    def __init__(self, model: str, year: int):
        """
        Инициализация объекта Car.

        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        """
        self.model = model
        self.year = year

    def car_info(self) -> str:
        """
        Возвращает информацию о машине.

        :return: Строка с информацией о машине.

        Пример:
        >>> car = Car("Toyota", 2020)
        >>> car.car_info()
        'Модель: Toyota, Год выпуска: 2020'
        """
        return f"Модель: {self.model}, Год выпуска: {self.year}"


class BankAccount:
    """
    Класс для представления банковского счета.

    Атрибуты:
    balance (float): Баланс счета.

    Методы:
    deposit(amount: float): Пополнение счета на указанную сумму.
    withdraw(amount: float): Снятие суммы со счета.
    get_balance(): Получение текущего баланса.
    """

    def __init__(self, balance: float = 0.0):
        """
        Инициализация объекта BankAccount.

        :param balance: Начальный баланс счета.
        """
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Пополнение счета на указанную сумму.

        :param amount: Сумма для пополнения.

        Пример:
        >>> account = BankAccount(100)
        >>> account.deposit(50)
        >>> account.get_balance()
        150.0
        """
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Сумма пополнения должна быть положительной")

    def withdraw(self, amount: float) -> None:
        """
        Снятие суммы со счета.

        :param amount: Сумма для снятия.

        Пример:
        >>> account = BankAccount(100)
        >>> account.withdraw(30)
        >>> account.get_balance()
        70.0
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Недостаточно средств или неправильная сумма")

    def get_balance(self) -> float:
        """
        Получение текущего баланса.

        :return: Текущий баланс счета.

        Пример:
        >>> account = BankAccount(200)
        >>> account.get_balance()
        200.0
        """
        return self.balance


if __name__ == "__main__":
    doctest.testmod()
