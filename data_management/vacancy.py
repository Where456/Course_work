from typing import List


class Vacancy:

    def __init__(self, vacancies: List[dict], amount: int, filter_words: List[str]) -> None:
        self.filter_words = filter_words
        self.vacancies = vacancies
        self.amount = amount

    @staticmethod
    def v_currency(salary: dict) -> dict:
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
    def parse_salary(salary: dict) -> str:
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
    def sort_vacancies_by_salary(vacancies: List[dict], reverse: bool = False) -> List[dict]:
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

        sorted_vacancies = sorted(vacancies, key=get_salary_key, reverse=reverse)

        return sorted_vacancies

    @staticmethod
    def sort_vacancies_by_city(vacancies: List[dict], title_city: str) -> List[dict]:
        filtered_vacancies = [vacancy for vacancy in vacancies if vacancy.get("city") == title_city]
        return filtered_vacancies

    @staticmethod
    def format_vacancy(vacancy: dict) -> str:
        description = vacancy['description']
        formatted_description = "Обязанности:\n" + (description if description else 'Не указано').replace('\n',
                                                                                                          ' ') + "\n\n" + \
                                "Требования:\n" + 'Не указано' + "\n\n" + \
                                "Условия:\n" + 'Не указано'

        formatted_salary = f"Зарплата: {Vacancy.parse_salary(vacancy['salary'])}"

        formatted_vacancy = f"Название вакансии: {vacancy['name']}\n" + \
                            f"ID: {vacancy['id']}\n" + \
                            f"Город: {vacancy['city']}\n" + \
                            f"Платформа: {vacancy['platform']}\n" + \
                            formatted_salary + "\n" + \
                            formatted_description + "\n"

        formatted_vacancy += "-" * 25
        formatted_vacancy = formatted_vacancy.replace('\n', ' ')
        return formatted_vacancy

    @staticmethod
    def print_vacancies(vacancies: List[dict]) -> List[str]:
        formatted_vacancies = []
        for vacancy in vacancies:
            formatted_vacancy = Vacancy.format_vacancy(vacancy)
            formatted_vacancies.append(formatted_vacancy)
        return formatted_vacancies

    def get_top_vacancies(self, vacancies) -> List[str]:
        top_vacancies = vacancies[:self.amount]
        return self.print_vacancies(top_vacancies)
