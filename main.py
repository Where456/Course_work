# Creating a class instance to work with the APIs of job search sites
from pprint import pprint

from api.headhunter_api import HeadHunterAPI
from api.superjob_api import SuperJobAPI
from data_management.json_saver import JSONSaver
from data_management.vacancy import Vacancy
from models.vacancies import Vacancies

vacancy = Vacancies("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
                    "Требования: опыт работы от 3 лет...")

# Saving information about vacancies to a file
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
json_saver.delete_vacancy(vacancy)


def user_interaction():
    platform = input('Choose your platform (SuperJob or HeadHunter): ')
    filter_words = input("Enter keywords to filter vacancies: ").split()
    amount = int(input("Enter the number of vacancies to display in top N: "))
    filtered_vacancies = []

    if platform.lower() == 'headhunter':
        hh_api = HeadHunterAPI(filter_words)
        filtered_vacancies = hh_api.get_vacancies()
    elif platform.lower() == 'superjob':
        superjob_api = SuperJobAPI(filter_words)
        filtered_vacancies = superjob_api.get_vacancies()
    vacancy = Vacancy(filtered_vacancies, amount, filter_words)
    sorted_vacancies = vacancy.get_top_vacancies()
    return pprint(sorted_vacancies)


if __name__ == "__main__":
    print(user_interaction())
