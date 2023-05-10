from src.functions import get_top_vacancies, print_vacancies, get_user_vacancies


if __name__ == '__main__':
    user_request = input("Введите название вакансии для поиска: ")

    platforms = input("С какого сайта хотите получать данные?\n "
                      "Введите:\n"
                      "'1' - HeadHunter.ru\n"
                      "'2' - Superjob.ru\n")
    try:
        top_n = int(input("Введите количество вакансий для вывода на экран:"))
    except ValueError:
        print("Неверно введенное значение. На экран будет выведено топ-5 вакансий ")
        top_n = 5

    user_keywords = input("Введите ключевые слова для вывода вакансий "
                          "или нажмите 'enter' для пропуска этого пункта: ").split(',')

    # получаем список вакансий с выбранной платформы по критериям пользователя
    user_vac = get_user_vacancies(platforms, user_request, user_keywords)

    # получаем список выбранного количества вакансий и выводим в удобном виде на экран
    top_vac = get_top_vacancies(user_vac, top_n)
    print("")
    print_vacancies(top_vac)
