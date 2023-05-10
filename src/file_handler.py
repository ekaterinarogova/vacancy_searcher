import json
from src.abstract_classes import FileHandler


class FileHandlerJSON(FileHandler):
    """
    Класс для работы с файлами json
    """

    def __init__(self, filename: str) -> None:
        """
        Инициализатор класса. При инициализации получает название файла json
        c которым будет работать
        :param filename: название файла
        """
        self.filename = f"{filename}.json"
        self.create_file()

    def create_file(self) -> None:
        """
        Создает пустой json файл
        """
        json_data = []
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(json.dumps(json_data))

    def add_vacancy(self, data: list) -> None:
        """
        Метод для добавления вакансий в файл
        :param data: инфо о вакансии
        """
        with open(self.filename, encoding='utf-8') as f:
            file_reader = json.load(f)
            file_reader.extend(data)
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(file_reader, file, indent=4, ensure_ascii=False)

    def get_vacancy(self, keywords: list) -> list:
        """
        Метод для получения списка вакансий по ключевому слову
        :param keywords: ключевые слова для поиска вакансии
        """

        with open(self.filename, encoding='utf-8') as f:
            file_reader = json.load(f)
            vacancies = []
            for i in file_reader:
                for key in keywords:
                    try:
                        if key in i['Название'] or key in i['Описание'] or key in i['Требования']:
                            vacancies.append(i)
                    except TypeError:
                        continue
            return vacancies

    def delete_vacancy(self, title: str) -> None:
        """
        Абстрактный метод для получения данных о вакансии из файла
        :param title: название вакансии
        """
        with open(self.filename, encoding='utf-8') as f:
            file_reader = json.load(f)
            file_reader_new = [i for i in file_reader if title in i['Название']]
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(file_reader_new, file, indent=4, ensure_ascii=False)
