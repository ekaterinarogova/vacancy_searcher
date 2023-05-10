from datetime import datetime

import pytest
from src.vacancy import VacancySuperJob


@pytest.fixture()
def sj_data1():
    data = {
        'payment_from': 50000,
        'payment_to': 0,
        'date_published': 1683543622,
        'profession': 'Сварщик',
        'candidat': 'Обязанности: Сварочные работы на трубопроводах отопления и водопровода,'
                    'монтаж металлоконструкций торгового оборудования и строительных сооружений.',
        'vacancyRichText': 'Обязанности: Сварочные работы на трубопроводах отопления и водопровода,'
                           'монтаж металлоконструкций торгового оборудования и строительных сооружений.',
        'type_of_work': {'id': 6, 'title': 'Полный рабочий день'},
        'experience': {'id': 2, 'title': 'От 1 года'},
        'client': {'id': 969000, 'title': 'Группа компаний Стройка'},
        'link': 'https://ryazan.superjob.ru/vakansii/svarschik-25845072.html',
    }
    return data


@pytest.fixture()
def sj_data2():
    data = {'objects': [
        {
            'payment_from': 0,
            'payment_to': 0,
            'date_published': 1683543622,
            'profession': 'Сварщик',
            'candidat': 'Обязанности: Сварочные работы на трубопроводах отопления и водопровода,'
                        'монтаж металлоконструкций торгового оборудования и строительных сооружений.',
            'vacancyRichText': 'Обязанности: Сварочные работы на трубопроводах отопления и водопровода,'
                               'монтаж металлоконструкций торгового оборудования и строительных сооружений.',
            'type_of_work': {'id': 6, 'title': 'Полный рабочий день'},
            'experience': {'id': 2, 'title': 'От 1 года'},
            'client': {'id': 969000, 'title': 'Группа компаний Стройка'},
            'link': 'https://ryazan.superjob.ru/vakansii/svarschik-25845072.html',
        },
        {
            'payment_from': 100000,
            'payment_to': 0,
            'date_published': 1683543622,
            'profession': 'Сварщик 2',
            'candidat': 'Обязанности: Сварочные работы на трубопроводах отопления и водопровода,'
                        'монтаж металлоконструкций торгового оборудования и строительных сооружений.',
            'vacancyRichText': 'Обязанности: Сварочные работы на трубопроводах отопления и водопровода,'
                               'монтаж металлоконструкций торгового оборудования и строительных сооружений.',
            'type_of_work': {'id': 6, 'title': 'Полный рабочий день'},
            'experience': {'id': 2, 'title': 'От 1 года'},
            'client': {'id': 969000, 'title': 'Группа компаний Стройка'},
            'link': 'https://ryazan.superjob.ru/vakansii/svarschik-25845072.html',
        }]}
    return data


def test_instantiate_sj(sj_data2):
    data = sj_data2
    VacancySuperJob.instantiate(data)
    assert len(VacancySuperJob.all_vacancies) == 2


def test_init_sj(sj_data1):
    sj = VacancySuperJob(sj_data1)
    assert sj.salary == 'от 50000'
    assert sj.title == 'Сварщик'
    assert sj.post_date == datetime(2023, 5, 8, 14, 0, 22)


def test_str_sj(sj_data1):
    sj = VacancySuperJob(sj_data1)
    assert sj.__str__() == {
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
    }


def test_sort_by_salary(sj_data2):
    VacancySuperJob.instantiate(sj_data2)
    assert VacancySuperJob.all_vacancies[0].title == 'Сварщик 2'


def test_string_convert_sj():
    test_string = '<b>Требования:</b><br />Опыт работы желателен\n'
    assert VacancySuperJob.string_convert(test_string) == ' Требования:  Опыт работы желателен '
