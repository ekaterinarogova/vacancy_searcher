import json
from abc import ABC, abstractmethod


class FileHandler(ABC):
    """
    Абстрактный класс для работы с файлами
    """

    @abstractmethod
    def add_vacancy(self, data: str) -> None:
        """
        Абстрактный метод для добавления вакансии в файл
        :param data: инфо о вакансии
        """
        ...

    @abstractmethod
    def get_vacancy(self, job_title: str) -> None:
        """
        Абстрактный метод для получения данных о вакансии из файла
        :param job_title: название о вакансии
        """
        ...

    # @abstractmethod
    # def delete_vacancy(self, data: str) -> None:
    #     """
    #     Абстрактный метод для удаления данных о вакансии из файла
    #     :param data: инфо о вакансии
    #     """
    #     ...


class FileHandlerJSON(FileHandler):
    """
    Класс для работы с файлами json
    """

    def __init__(self, filename: str) -> None:
        """
        Инициализатор класса. При инициализации получает название файла json
        c которым будет работать
        :param filename: путь до файла
        """
        self.filename = f'{filename}.json'
        self.create_file()

    def create_file(self) -> None:
        """
        Создает пустой json файл
        """
        json_data = []
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(json.dumps(json_data, indent=2))

    def add_vacancy(self, data: dict) -> None:
        """
        Абстрактный метод для добавления данных о вакансии в файл
        :param data: инфо о вакансии
        """
        with open(self.filename, encoding='utf-8') as f:
            file_reader = json.load(f)
            file_reader.append(data)
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(file_reader, file)

    def get_vacancy(self, job_title) -> None:
        """
        Метод для получения данных о вакансии из файла
        :param job_title: инфо о вакансии
        """
        with open(self.filename, encoding='utf-8') as f:
            file_reader = json.load(f)
            for i in file_reader:
                if i[job_title]:
                    return i[job_title]

    # def delete_vacancy(self,title: str, data: dict) -> None:
    #     """
    #     Абстрактный метод для получения данных о вакансии из файла
    #     :param data: инфо о вакансии
    #     :param title: название вакансии
    #     """
    #     with open(self.filename, encoding='utf-8') as f:
    #         file_reader = json.load(f)
    #         for i in file_reader:
    #             if i[title]:
    #                 del file_reader[title]
    #     with open(self.filename, 'w', encoding='utf-8') as file:
    #         json.dump(file_reader, file)
    