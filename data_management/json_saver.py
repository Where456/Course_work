import json

from data_management.vacancy_manager import VacancyManager
from models.vacancy import Vacancy


class JSONSaver(VacancyManager):
    def __init__(self):
        self.vacancies = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vacancy)

    def get_vacancies_by_salary(self, salary_range):
        filtered_vacancies = [v for v in self.vacancies if v.salary == salary_range]
        return filtered_vacancies

    def delete_vacancy(self, vacancy):
        self.vacancies.remove(vacancy)

    def save_to_json(self, file_name):
        with open(file_name, 'w') as file:
            json.dump([vars(v) for v in self.vacancies], file)

    def load_from_json(self, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
            self.vacancies = [Vacancy(**v) for v in data]
