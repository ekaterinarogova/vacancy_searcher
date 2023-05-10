from abc import ABC, abstractmethod


class API(ABC):
    """
    Абстрактный класс для получения данных по вакансиям
    """

    @abstractmethod
    def get_vacancy(self, title):
        """
        Абстрактный метод для получения списка вакансий
        :param title: название вакансии
        """
        ...


class Vacancy(ABC):
    """
    Абстрактный класс для работы с вакансиями
    """

    def __init__(self, info: dict):
        ...

    @classmethod
    def instantiate(cls, data: dict):
        """
        Абстрактный метод для создания экземпляров класса
        :param data: словарь со списком вакансий
        """
        ...

    def sort_by_salary(self):
        """
        Абстрактный метод для сортировки вакансий по уровню зарплаты по убыванию
        """
        ...

    def salary_validator(self):
        """
        Абстрактный метод для приведения данных по зарплате в читаемый вид
        """
        ...

class FileHandler(ABC):
    """
    Абстрактный класс для работы с файлами
    """

    @abstractmethod
    def add_vacancy(self, data) -> None:
        """
        Абстрактный метод для добавления вакансии в файл
        :param data: инфо о вакансии
        """
        ...

    @abstractmethod
    def get_vacancy(self, keywords: list) -> list:
        """
        Абстрактный метод для получения списка вакансий по ключевому слову
        """
        ...

    @abstractmethod
    def delete_vacancy(self, title: str) -> None:
        """
        Абстрактный метод для удаления данных о вакансии из файла
        :param title: название вакансии
        """
        ...
