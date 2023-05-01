from src.request import GetVacancyHH
from src.file_handler import FileHandlerJSON
from src.vacancy import Vacancy

user_vacancy = GetVacancyHH()
job_title = 'анестезиолог'
json_file = FileHandlerJSON(job_title)
json_file.add_vacancy(user_vacancy.get_vacancy(job_title))
Vacancy.instantiate_from_json(job_title, json_file.filename)
print(Vacancy.all_vacancies)

