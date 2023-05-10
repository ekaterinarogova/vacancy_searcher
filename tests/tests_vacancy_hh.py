from datetime import datetime
import pytest
from src.vacancy import VacancyHH, VacancySuperJob


@pytest.fixture
def hh_data1():
    data = {
        'name': 'Визажист (Новинский)',
        'salary': {
            'from': 80000,
            'to': None, 'currency': 'RUR'},
        'published_at': '2023-05-10T11:55:06+0300',
        'alternate_url': 'https://hh.ru/vacancy/80229822',
        'employer': {'id': '142251', 'name': 'Aldo Coppola'},
        'snippet': {
            'requirement': 'Аналогичный опыт работы от 3-х лет в салоне красоты. '
                           'Опыт работы с люксовыми брендами (CD, Tom Ford и др.).',
            'responsibility': 'Выполнение всех видов макияжа, в т.ч. touch up, дневной, вечерний. '
                              'Окрашивание, коррекция и укладка бровей. Перманентный макияж. Наращивание ресниц.'},
        'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
        'employment': {'id': 'full', 'name': 'Полная занятость'}
    }
    return data


@pytest.fixture()
def hh_data2():
    data = {'items': [
        {
            'name': 'Визажист 1',
            'salary': None,
            'published_at': '2023-05-10T11:55:06+0300',
            'alternate_url': 'https://hh.ru/vacancy/80229822',
            'employer': {'id': '142251', 'name': 'Beauty'},
            'snippet': {
                'requirement': 'Аналогичный опыт работы от 3-х лет в салоне красоты. ',
                'responsibility': 'Выполнение всех видов макияжа'},
            'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
            'employment': {'id': 'full', 'name': 'Полная занятость'}
        },
        {'name': 'Визажист 2',
         'salary': {
             'from': 80000,
             'to': None, 'currency': 'RUR'},
         'published_at': '2023-05-10T11:55:06+0300',
         'alternate_url': 'https://hh.ru/vacancy/80229822',
         'employer': {'id': '142251', 'name': 'Aldo Coppola'},
         'snippet': {
             'requirement': 'Аналогичный опыт работы от 3-х лет в салоне красоты. '
                            'Опыт работы с люксовыми брендами (CD, Tom Ford и др.).',
             'responsibility': 'Выполнение всех видов макияжа, в т.ч. touch up, дневной, вечерний. '
                               'Окрашивание, коррекция и укладка бровей. Перманентный макияж. Наращивание ресниц.'},
         'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
         'employment': {'id': 'full', 'name': 'Полная занятость'}
         }
    ]}
    return data


def test_instantiate_hh(hh_data2):
    data = hh_data2
    VacancyHH.instantiate(data)
    assert len(VacancyHH.all_vacancies) == 2


def test_sort_by_salary_hh(hh_data2):
    VacancyHH.instantiate(hh_data2)
    assert VacancyHH.all_vacancies[0].title == 'Визажист 2'


def test_init_hh(hh_data1):
    hh = VacancyHH(hh_data1)
    assert hh.title == 'Визажист (Новинский)'
    assert hh.post_date == datetime(2023, 5, 10, 11, 55, 6, 30000)
    assert hh.salary == 'от 80000'


def test_str_hh(hh_data1):
    hh = VacancyHH(hh_data1)
    assert hh.__str__() == {
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
    }
