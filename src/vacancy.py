import json
from datetime import datetime
from src.abstract_classes import Vacancy

class VacancyHH(Vacancy):
    """
    Класс для обработки данных по вакансиям c HeadHunter
    """
    all_vacancies = []

    def __init__(self, info: dict):
        """
        Инициализатор класса. При инициализации получает информацию о вакансии в виде словаря.
        :param info: Словарь с данными о вакансии
        """
        self.info = info
        self.title = None
        self.url = None
        self.description = None
        self.requirements = None
        self.salary = None
        self.salary_from = None
        self.salary_to = None
        self.employer = None
        self.employment = None
        self.experience = None
        self.post_date = None
        self.get_info()
        self.salary_validator()
        self.all_vacancies.append(self)
        self.sort_by_salary()

    @classmethod
    def instantiate(cls, data: dict) -> None:
        """
        Метод создающий экземпляры класса
        :param data: json словарь со списком вакансий
        """
        for i in data['items']:
            cls(i)

    def get_info(self) -> None:
        """
        Заполняет данные атрибутов экземпляра
        """
        self.title: str = self.info.get('name')
        self.url: str = self.info.get('alternate_url')
        self.description: str = self.info.get('snippet').get('responsibility')
        self.requirements: str = self.info.get('snippet').get('requirement')
        if self.info.get('salary') is not None:
            self.salary_from = self.info.get('salary').get('from')
            self.salary_to = self.info.get('salary').get('to')
        self.employer: str = self.info.get('employer').get('name')
        self.employment: str = self.info.get('employment').get('name')
        self.experience: str = self.info.get('experience').get('name')
        self.post_date: datetime = datetime.strptime(self.info.get('published_at'), '%Y-%m-%dT%H:%M:%S+%f')

    def __str__(self):
        return {
            'Название': self.title,
            'URL': self.url,
            'Описание': self.description,
            'Требования': self.requirements,
            'Зарплата': self.salary,
            'Зарплата от': self.salary_from,
            'Зарплата до': self.salary_to,
            'Компания': self.employer,
            'Занятость': self.employment,
            'Опыт работы': self.experience,
            'Дата публикации': f'{datetime.strftime(self.post_date, "%d-%m-%Y")}'
        }

    def salary_validator(self) -> None:
        """
        Приводит данные по зарплате в читаемый вид
        """
        if self.salary_from is not None and self.salary_to is not None:
            self.salary = f"{self.salary_from} - {self.salary_to}"
        elif self.salary_from is not None:
            self.salary = f"от {self.salary_from}"
        elif self.salary_to is not None:
            self.salary = f"до {self.salary_to}"
        else:
            self.salary = "не указана"

    def sort_by_salary(self):
        """
        Сортирует список всех вакансий по зарплате по убыванию.
        Вакансии в которых зарплата не указана отправляются в конец списка.
        :return: Отсортированный список вакансий
        """
        return self.all_vacancies.sort(key=lambda x: x.salary_from if x.salary_from is not None else float('-inf'), reverse=True)


class VacancySuperJob(Vacancy):
    """
    Класс для обработки данных по вакансиям c SuperJob
    """

    all_vacancies = []
    def __init__(self, info: dict):
        """
        Инициализатор класса. При инициализации получает информацию о вакансии в виде словаря.
        :param info: Словарь с данными о вакансии
        """
        self.info = info
        self.title = None
        self.url = None
        self.description = None
        self.requirements = None
        self.salary = None
        self.salary_from = None
        self.salary_to = None
        self.employer = None
        self.employment = None
        self.experience = None
        self.post_date = None
        self.get_info()
        self.salary_validator()
        self.all_vacancies.append(self)
        self.sort_by_salary()

    @classmethod
    def instantiate(cls, data: dict) -> None:
        """
        Метод создающий экземпляры класса
        :param data: json словарь со списком вакансий
        """
        for i in data['objects']:
            cls(i)

    @staticmethod
    def string_convert(string: str):
        """
        Метод для удаления ненужных символов из строки
        :param string: строка для конвертации
        :return: строка без лишних символов
        """
        symbols = ['\n', '</p>', '<p>', '</li>', '<li>', '<b>', '</b>', '<ul>', '<li>', '</li>',  '<br />', '</ul>']

        for symb in symbols:
            string = string.replace(symb, " ")

        return string

    def get_info(self) -> None:
        """
        Заполняет данные атрибутов экземпляра
        """
        self.title: str = self.info.get('profession')
        self.url: str = self.info.get('link')
        self.description: str = self.string_convert(self.info.get('vacancyRichText'))
        self.requirements: str = self.string_convert(self.info.get('candidat'))
        self.salary_from: int = int(self.info.get('payment_from'))
        self.salary_to: int = int(self.info.get('payment_to'))
        self.employer: str = self.info.get('client').get('title')
        self.employment: str = self.info.get('type_of_work').get('title')
        self.experience: str = self.info.get('experience').get('title')
        self.post_date: datetime = datetime.fromtimestamp(self.info.get('date_published'))


    def __str__(self):
        return {
            'Название': self.title,
            'URL': self.url,
            'Описание': self.description,
            'Требования': self.requirements,
            'Зарплата': self.salary,
            'Зарплата от': self.salary_from,
            'Зарплата до': self.salary_to,
            'Компания': self.employer,
            'Занятость': self.employment,
            'Опыт работы': self.experience,
            'Дата публикации': f'{datetime.strftime(self.post_date, "%d-%m-%Y")}'
        }

    def salary_validator(self) -> None:
        """
        Приводит данные по зарплате в читаемый вид
        """
        if self.salary_from != 0 and self.salary_to != 0:
            self.salary = f"{self.salary_from} - {self.salary_to}"
        elif self.salary_from != 0:
            self.salary = f"от {self.salary_from}"
        elif self.salary_to != 0:
            self.salary = f"до {self.salary_to}"
        else:
            self.salary = "не указана"


    def sort_by_salary(self):
        """
        Сортирует список всех вакансий по зарплате по убыванию.
        Вакансии в которых зарплата не указана отправляются в конец списка.
        :return: Отсортированный список вакансий
        """
        return self.all_vacancies.sort(key=lambda x: x.salary_from if x.salary_from != 0 else float('-inf'), reverse=True)







