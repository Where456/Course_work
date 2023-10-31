import json

from models.vacancies import Vacancies


# from models.vacancy import Vacancy


class JSONSaver:
    def __init__(self):
        self.file_name = "vacancies.json"
        self.vacancies = []
        self.load_from_json()
        self.current_id = 1

    def add_vacancy(self, vacancy):
        self.vacancies.append(vars(vacancy))
        self.save_to_json()

    def read_vacancy(self, vacancy_id):
        for vacancy in self.vacancies:
            if vacancy.get('id') == vacancy_id:
                return vacancy
        return None

    def update_vacancy(self, vacancy_id, name=None, url=None, salary=None, description=None):
        vacancy = self.read_vacancy(vacancy_id)
        if vacancy:
            if salary:
                salary = self.parse_salary(salary)
            if name:
                vacancy['name'] = name
            if url:
                vacancy['url'] = url
            if salary:
                vacancy['salary'] = salary
            if description:
                vacancy['description'] = description
            self.save_to_json()
            return vacancy
        return None

    def delete_vacancy(self, vacancy):
        self.vacancies.remove(vars(vacancy))
        self.save_to_json()

    def get_vacancies_by_salary(self, salary_range):
        filtered_vacancies = [v for v in self.vacancies if v['salary'] == salary_range]
        return filtered_vacancies

    def parse_salary(self, salary_str):
        parts = salary_str.split(' - ')
        if len(parts) == 2:
            currency = "rub"
            from_salary = int(parts[0].replace(' ', ''))
            to_salary = int(parts[1].replace(' ', ''))
            return {"currency": currency, "from": from_salary, "to": to_salary}
        return None

    def save_to_json(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.vacancies, file)

    def load_from_json(self):
        try:
            with open(self.file_name, 'r') as file:
                self.vacancies = json.load(file)
        except FileNotFoundError:
            self.vacancies = []


# vacancy = Vacancies("Python Developer", "https://hh.ru/vacancy/123456", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
#
# # Создаем экземпляр JSONSaver
# json_saver = JSONSaver()
#
# # Добавляем вакансию
# json_saver.add_vacancy(vacancy)
#
# # Получаем вакансии по зарплате
# filtered_vacancies = json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
# print("Vacancies by salary:")
# print(filtered_vacancies)