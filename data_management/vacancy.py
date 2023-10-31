from pprint import pprint


class Vacancy:

    def __init__(self, vacancies, amount, filter_words):
        self.filter_words = filter_words
        self.vacancies = vacancies
        self.amount = amount

    @staticmethod
    def v_currency(salary):
        salary_from = salary.get("from")
        salary_to = salary.get("to")
        currency = salary.get("currency")
        if currency == 'KZT':
            if salary_from: salary_from *= 0.2
            if salary_to: salary_to *= 0.2
        if currency == 'BYR':
            if salary_from: salary_from *= 28.41
            if salary_to: salary_to *= 28.41
        return {
            "currency": "rub",
            "from": salary_from,
            "to": salary_to
        }

    @staticmethod
    def parse_salary(salary):
        if salary:
            salary_from = salary.get("from")
            salary_to = salary.get("to")
            if salary_from is not None and salary_to is not None:
                salary_string = f"{salary_from} - {salary_to}"
            elif salary_from is not None:
                salary_string = f"от {salary_from}"
            elif salary_to is not None:
                salary_string = f"до {salary_to}"
            else:
                salary_string = "Не указано"

            return salary_string

        return "Не указано"

    @staticmethod
    def sort_vacancies_by_salary(vacancies):
        def get_salary_key(vacancy):
            salary = vacancy['salary']
            from_salary = salary.get('from') if salary else None
            to_salary = salary.get('to') if salary else None

            if from_salary is not None and to_salary is not None:
                return (from_salary + to_salary) / 2
            elif from_salary is not None:
                return from_salary
            elif to_salary is not None:
                return to_salary
            else:
                return 0

        return sorted(vacancies, key=get_salary_key)

    @staticmethod
    def print_vacancies(vacancies):
        formatted_vacancies = []
        for vacancy in vacancies:
            formatted_vacancy = {
                "name": vacancy['name'],
                "salary": Vacancy.parse_salary(vacancy['salary']),
                "description": vacancy['description'],
                "id": vacancy['id'],
                "platform": vacancy['platform']
            }
            formatted_vacancies.append(formatted_vacancy)
        return formatted_vacancies

    def get_top_vacancies(self):
        sorted_vacancies = self.sort_vacancies_by_salary(self.vacancies)
        top_vacancies = sorted_vacancies[:self.amount]
        return self.print_vacancies(top_vacancies)
