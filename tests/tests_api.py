import os

import pytest
from src.api import HeadHunterAPI, SuperJobAPI


def test_get_vacancy_hh():
    hh = HeadHunterAPI()
    title = 'ветеринарный врач'
    assert type(hh.get_vacancy(title)) == dict
    assert type(hh.get_vacancy(title)['items']) == list


def test_get_vacancy_sj():
    sj = SuperJobAPI()
    title = 'бармен'
    assert type(sj.get_vacancy(title)) == dict
    assert type(sj.get_vacancy(title)['objects']) == list

