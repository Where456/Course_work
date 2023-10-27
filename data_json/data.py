import json
import time
from pprint import pprint

from api.headhunter_api import HeadHunterAPI
from api.superjob_api import SuperJobAPI


def save_vacancies_to_file(vacancies, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(vacancies, file, ensure_ascii=False, indent=4)


def load_vacancies_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    sj_api = SuperJobAPI()
    filename = "vacancies.json"

    while True:
        vacancies = hh_api.get_vacancies() + sj_api.get_vacancies()
        save_vacancies_to_file(vacancies, 'vacancies.json')

        print("Данные обновлены.")
        print(load_vacancies_from_file(filename))
        time.sleep(1800)
