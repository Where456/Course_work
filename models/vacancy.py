from pprint import pprint


class Vacancy:
    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description

    #
    # def __str__(self):
    #     return f"name: {self.name}\nurl: {self.url}\nSalary: {self.salary}\nDescription: {self.description}"

    # def __lt__(self, other):
    #     return self.compare_salary(other) == -1

    # def __eq__(self, other):
    #     return self.name == other.name and self.url == other.url

    # def compare_salary(self, other_vacancy):
    #     if self.salary and other_vacancy.salary:
    #         self_salary = self.parse_salary(self.salary)
    #         other_salary = self.parse_salary(other_vacancy.salary)
    #         if self_salary < other_salary:
    #             return -1
    #         elif self_salary > other_salary:
    #             return 1
    #         else:
    #             return 0
    #     return 0

    @staticmethod
    def parse_salary(salary):
        if salary:
            salary_from = salary.get("from")
            salary_to = salary.get("to")
            currency = salary.get("currency")
            if currency == 'KZT':
                if salary_from: salary_from *= 0.2
                if salary_to: salary_to *= 0.2
            if currency == 'KZT':
                if salary_from: salary_from *= 28.41
                if salary_to: salary_to *= 28.41

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
    def filter_vacancies(vacancies, filter_words):
        filtered_vacancies = []
        for vacancy in vacancies:
            description = vacancy.get("description", "").lower()
            name = vacancy.get("name", "").lower()
            if any(keyword in description or keyword in name for keyword in filter_words):
                filtered_vacancies.append(vacancy)
        return filtered_vacancies

    @staticmethod
    def sort_vacancies(vacancies):
        return sorted(vacancies, key=lambda v: v.compare_salary(v), reverse=True)

    @staticmethod
    def get_top_vacancies(vacancies, top_n):
        return vacancies[:top_n]

    # @staticmethod
    # def print_vacancies(vacancies):
    #     for vacancy in vacancies:
    #         print(vacancy)


# print(Vacancy('', '', '', '').filter_vacancies([{
#     "id": "87790296",
#     "name": "Фасовщик навогодних подарков",
#     "salary": {
#         "from": 1500,
#         "to": None,
#         "currency": "BYR",
#         "gross": False
#     },
#     "description": "Требования: Наличие сан.книжки обязательно.\nОбязанности: None",
#     "url": "https://hh.ru/vacancy/87790296",
#     "platform": "HeadHunter"
# },
#     {
#         "id": "87907825",
#         "name": "Преподаватель английского языка",
#         "salary": {
#             "from": 4000000,
#             "to": 8000000,
#             "currency": "UZS",
#             "gross": False
#         },
#         "description": "Требования: None\nОбязанности: None",
#         "url": "https://hh.ru/vacancy/87907825",
#         "platform": "HeadHunter"
#     },
#     {
#         "id": "87542041",
#         "name": "Удаленный диспетчер чатов (в Яндекс)",
#         "salary": {
#             "from": 30000,
#             "to": 44000,
#             "currency": "RUR",
#             "gross": True
#         },
#         "description": "Требования: Способен работать в команде. Способен принимать решения самостоятельно. Готов учиться и узнавать новое. Опыт работы в колл-центре или службе...\nОбязанности: Работать с клиентами или партнерами для решения разнообразных ситуаций. Совершать звонки по их обращениям и давать письменные ответы. ",
#         "url": "https://hh.ru/vacancy/87542041",
#         "platform": "HeadHunter"
#     },
#     {
#         "id": "88646425",
#         "name": "Водитель персональный",
#         "salary": {
#             "from": 100000,
#             "to": 120000,
#             "currency": "RUR",
#             "gross": False
#         },
#         "description": "Требования: Опыт работы личным/персональным водителем от 5 лет. Хорошее знание дорог Москвы и Московской области. Умение пользоваться навигатором. \nОбязанности: Транспортное сопровождение собственника компании. Подача авто в определенное время и место. Планирование оптимального маршрута и обеспечение безопасного движения с учетом...",
#         "url": "https://hh.ru/vacancy/88646425",
#         "platform": "HeadHunter"
#     },
#     {
#         "id": "88230920",
#         "name": "Оператор контактного центра на входящую линию (удаленно)",
#         "salary": {
#             "from": 40000,
#             "to": None,
#             "currency": "RUR",
#             "gross": True
#         },
#         "description": "Требования: Готовность помогать и находить контакт с людьми. Уверенность при использовании компьютера. Оборудование для удаленной работы дома (компьютер- Windows 8 и...\nОбязанности: Консультировать клиентов по тарифным планам, услугам, балансу и начислениям (общение с нашими действующими абонентами, только входящие звонки). Помогать в выборе...",
#         "url": "https://hh.ru/vacancy/88230920",
#         "platform": "HeadHunter"
#     }], 'Требования'))
