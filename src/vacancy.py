import json


class Vacancy:
    """
    Класс для обработки данных по вакансиям
    """
    all_vacancies = []

    def __init__(self, info: dict):
        """
        Инициализатор класса. Все данные подтягиваются при инициализации из описания вакансии
        """
        self.info = info
        self.title = None
        self.url = None
        self.description = None
        self.requirements = None
        self.salary = None
        self.address = None
        self.employer = None
        self.employment = None
        self.experience = None
        self.get_info()
        self.all_vacancies.append(self)

    @classmethod
    def instantiate_from_json(cls, job_title: str, filename: str):
        """
        Метод создающий экземпляры класса из json файла
        """
        with open(filename, encoding='utf-8') as f:
            data = json.load(f)
            for i in data:
                for item in i['items']:
                    if job_title in item['name']:
                        cls(item)

    def get_info(self) -> None:
        """
        Заполняет данные атрибутов экземпляра
        """
        self.title: str = self.info.get('name')
        self.url: str = self.info.get('url')
        self.description: str = self.info.get('snippet').get('responsibility')
        self.requirements: str = self.info.get('snippet').get('requirement')
        if self.info.get('salary') is None:
            self.salary = None
        else:
            self.salary = self.info.get('salary').get('from')
        if self.info.get('address') is not None:
            self.address: str = self.info.get('address').get('raw')
        self.employer: str = self.info.get('employer').get('name')
        self.employment: str = self.info.get('employment').get('name')
        self.experience: str = self.info.get('experience').get('name')

    def __repr__(self):
        return f"{self.__class__.__name__} ('название - {self.title}', 'ссылка - {self.url}', 'описание - {self.description}', " \
               f"'требования - {self.requirements}', 'зарплата {self.salary}', " \
               f"'адресс - {self.address}', 'компания - {self.employer}', 'занятость - {self.employment}', " \
               f"'опыт работы - '{self.experience}' "

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            if self.salary is not None and other.salary is not None:
                return self.salary > other.salary
        return "некорректные данные для сравнения"
