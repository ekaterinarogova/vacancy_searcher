import json
from abc import ABC, abstractmethod

import requests


class GetVacancy(ABC):
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


class GetVacancyHH(GetVacancy):
    """
    Класс для получения вакансий с сайта hh.ru
    """

    def get_vacancy(self, title: str):
        """
        Абстрактный метод для получения списка вакансий
        :param title: название вакансии
        """
        params = {
            'text': f'NAME:{title}',  # Текст фильтра. В имени должно быть слово "Аналитик"
            'area': 1,  # Поиск осуществляется по вакансиям города Москва
            'page': 1,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }

        response = requests.get("https://api.hh.ru/vacancies", params)
        data = response.content.decode()
        data_json = json.loads(data)
        return data_json


    def __repr__(self):
        return f"{self.__class__.__name__}"


class GetVacancySuperJob(GetVacancy):
    """
    Класс для получения вакансий с сайта superjob.ru
    """
    def get_vacancy(self, title):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}"


