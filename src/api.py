import requests
import os
from src.abstract_classes import API


class HeadHunterAPI(API):
    """
    Класс для получения вакансий с сайта hh.ru
    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"

    def get_vacancy(self, title: str):
        """
        Метод для получения списка вакансий
        :param title: ключевое слово для поиска вакансии
        :return: массив данных со списком вакансий по ключевому слову
        """
        params = {
            'text': f'NAME:{title}',  # Текст фильтра.
            'area': 1,  # Поиск осуществляется по вакансиям города Москва
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }

        response = requests.get(self.__url, params).json()
        return response

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__url}')"


class SuperJobAPI(API):
    """
    Класс для получения вакансий с сайта superjob.ru
    """
    __SUPERJOB_APP_ID = os.environ.get('SUPERJOB_APP_ID')

    def __init__(self):
        self.__url = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancy(self, title: str):
        """
        Метод для получения списка вакансий
        :param title: ключевое слово для поиска вакансий
        :return: массив данных со списком вакансий по ключевому слову в названии вакансии
        """
        headers = {"X-Api-App-Id": self.__SUPERJOB_APP_ID}

        params = {
            'keyword': title,
            'count': 100
        }
        response = requests.get(self.__url, headers=headers, params=params).json()
        return response

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__url}')"
