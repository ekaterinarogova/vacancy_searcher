import json

import pytest
from src.file_handler import FileHandlerJSON


@pytest.fixture()
def data():
    data = [{
        'Название': 'Визажист (Новинский)',
        'URL': 'https://hh.ru/vacancy/80229822',
        'Описание': 'Выполнение всех видов макияжа, в т.ч. touch up, дневной, вечерний. '
                    'Окрашивание, коррекция и укладка бровей. Перманентный макияж. Наращивание ресниц.',
        'Требования': 'Аналогичный опыт работы от 3-х лет в салоне красоты. '
                      'Опыт работы с люксовыми брендами (CD, Tom Ford и др.).',
        'Зарплата': 'от 80000',
        'Зарплата от': 80000,
        'Зарплата до': None,
        'Компания': 'Aldo Coppola',
        'Занятость': 'Полная занятость',
        'Опыт работы': 'От 1 года до 3 лет',
        'Дата публикации': '10-05-2023'
    },
        {
            'Название': 'Сварщик',
            'URL': 'https://ryazan.superjob.ru/vakansii/svarschik-25845072.html',
            'Описание': 'Обязанности: Сварочные работы на трубопроводах отопления и водопровода,'
                        'монтаж металлоконструкций торгового оборудования и строительных сооружений.',
            'Требования': 'Обязанности: Сварочные работы на трубопроводах отопления и водопровода,'
                          'монтаж металлоконструкций торгового оборудования и строительных сооружений.',
            'Зарплата': 'от 50000',
            'Зарплата от': 50000,
            'Зарплата до': 0,
            'Компания': 'Группа компаний Стройка',
            'Занятость': 'Полный рабочий день',
            'Опыт работы': 'От 1 года',
            'Дата публикации': '08-05-2023'
        }]
    return data


@pytest.fixture()
def json_file():
    json_file = FileHandlerJSON('test')
    return json_file


def test_init(json_file):
    assert json_file.filename == 'test.json'
    with open('test.json') as f:
        file = json.load(f)
        assert file == []


def test_add_vacancy(data, json_file):
    json_file.add_vacancy(data)
    with open('test.json') as f:
        file = json.load(f)
        assert len(file) == 2


def test_get_vacancy(json_file, data):
    json_file.add_vacancy(data)
    keywords = ['макияж']
    assert json_file.get_vacancy(keywords) == [{
        "Название": "Визажист (Новинский)",
        "URL": "https://hh.ru/vacancy/80229822",
        "Описание": "Выполнение всех видов макияжа, в т.ч. touch up, дневной, вечерний. "
                    "Окрашивание, коррекция и укладка бровей. Перманентный макияж. Наращивание ресниц.",
        "Требования": "Аналогичный опыт работы от 3-х лет в салоне красоты. "
                      "Опыт работы с люксовыми брендами (CD, Tom Ford и др.).",
        "Зарплата": "от 80000",
        "Зарплата от": 80000,
        "Зарплата до": None,
        "Компания": "Aldo Coppola",
        "Занятость": "Полная занятость",
        "Опыт работы": "От 1 года до 3 лет",
        "Дата публикации": "10-05-2023"
    }]


def test_delete_vacancy(json_file, data):
    title = 'Сварщик'
    json_file.add_vacancy(data)
    json_file.delete_vacancy(title)
    with open('test.json') as f:
        file = json.load(f)
        assert len(file) == 1
