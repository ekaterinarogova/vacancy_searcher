import pytest
from src.functions import get_top_vacancies, get_vacancies_hh, \
    get_user_vacancies, get_vacancies_sj, print_vacancies


@pytest.fixture()
def vac_list():
    vacancies = [{
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
    return vacancies


@pytest.fixture()
def vacancy():
    vac = [{
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
    }]

    return vac


def test_get_vacancies_hh():
    keyword = 'геодезист'
    assert type(get_vacancies_hh(keyword)[0]) == dict
    assert keyword in get_vacancies_hh(keyword)[0]['Название']


def test_get_vacancies_sj():
    keyword = 'инженер'
    assert type(get_vacancies_sj(keyword)[0]) == dict
    assert keyword in get_vacancies_sj(keyword)[0]['Название']


def test_get_user_vacancies_negative():
    platform = 'один'
    user_request = 'кассир'
    user_keywords = []
    assert get_user_vacancies(platform, user_request, user_keywords) == "Неверно заданные параметры"


def test_get_top_vacancies(vac_list):
    assert len(get_top_vacancies(vac_list, 1)) == 1
    assert get_top_vacancies(vac_list, 10) == vac_list

