from src.api import HeadHunterAPI, SuperJobAPI
from src.vacancy import VacancyHH, VacancySuperJob
from src.file_handler import FileHandlerJSON


def get_top_vacancies(vacancies: list, top_n=5) -> list:
    """
    Выводит топ N вакансий
    :param vacancies: список вакансий
    :param top_n: количество вакансий для вывода пользователю
    :return: список вакансий
    """
    top_vacancies = []
    try:
        for i in range(int(top_n)):
            top_vacancies.append(vacancies[i])
    except IndexError:
        print(f'Всего вакансий, соответствующих запросу {len(vacancies)}')

    return top_vacancies


def print_vacancies(vacancy: list) -> None:
    """
    Функция для вывода вакансий на экран в удобном формате
    :param vacancy: список вакансий для вывода на экран
    """
    for i in vacancy:
        print(f"""Название: {i['Название']}
Зарплата: {i['Зарплата']}
Описание вакансии: {i['Описание']}
Требования: {i['Требования']}
Занятость: {i['Занятость']}
Опыт работы: {i['Опыт работы']}
Компания: {i['Компания']}
Ссылка на вакансию: {i['URL']}
Опубликовано: {i['Дата публикации']}\n""")


def get_vacancies_hh(user_request: str) -> list:
    """
    Функция для получения списка вакансий по запросу пользователя с сайта headhunter.ru
    :param user_request: название должности для поиска вакансии
    :return: список вакансий
    """
    api = HeadHunterAPI()
    search = api.get_vacancy(user_request)
    VacancyHH.instantiate(search)

    vacancies = []
    for vacancy in VacancyHH.all_vacancies:
        vacancies.append(vacancy.__str__())

    return vacancies


def get_vacancies_sj(user_request: str) -> list:
    """
    Функция для получения списка вакансий по запросу пользователя с сайта superjob.ru
    :param user_request: название должности для поиска вакансии
    :return: список вакансий
    """
    api = SuperJobAPI()
    search = api.get_vacancy(user_request)
    VacancySuperJob.instantiate(search)

    vacancies = []
    for vacancy in VacancySuperJob.all_vacancies:
        vacancies.append(vacancy.__str__())

    return vacancies


def get_user_vacancies(platforms: str, user_request: str, user_keywords: list):
    """
    Функция для обработки запроса от пользователя. Получает название платформы,
    название должности и ключевые слова для поиска вакансий
    :param platforms: платформа для поиска вакансий
    :param user_request: название должности
    :param user_keywords: ключевые слова для поиска вакансий
    :return: список вакансий, отфильтрованый по ключевым словам и отсортированный по зарплате
    """
    if platforms == "1":
        vacancies = get_vacancies_hh(user_request)

    elif platforms == "2":
        vacancies = get_vacancies_sj(user_request)
    else:
        return "Неверно заданные данные"

    json_file = FileHandlerJSON(user_request)
    json_file.add_vacancy(vacancies)
    user_vac = json_file.get_vacancy(user_keywords)

    return user_vac
