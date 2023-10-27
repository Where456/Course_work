from pprint import pprint

import requests

from api.job_search_api import JobSearchAPI
from models.vacancy import Vacancy


class HeadHunterAPI(JobSearchAPI):
    def __init__(self):
        self._url = "https://api.hh.ru"

    def get_vacancies(self):
        url = f"{self._url}/vacancies"
        response = requests.get(url)
        if response.status_code == 200:
            vacancies = response.json()
            formatted_vacancies = []
            for vacancy in vacancies['items']:
                description = vacancy.get('snippet', {})
                requirements = description.get("requirement", "Не указано")
                responsibilities = description.get("responsibility", "Не указано")

                if requirements == "Не указано" and responsibilities == "Не указано":
                    formatted_description = "Не указано"
                else:
                    formatted_description = f"Требования: {requirements}\nОбязанности: {responsibilities}"
                formatted_vacancy = {
                    "id": vacancy.get("id", "Не указано"),
                    "name": vacancy.get("name", "Не указано"),
                    "salary": Vacancy('','', '','').parse_salary(vacancy.get("salary", "Не указано")),
                    "description": formatted_description,

                    "url": vacancy.get("alternate_url", "Не указано"),
                    "platform": "HeadHunter"
                }
                formatted_vacancies.append(formatted_vacancy)

            return formatted_vacancies
        else:
            print("Ошибка при получении вакансий:", response.text)
            return []


# if __name__ == "__main__":
#     pprint(HeadHunterAPI().get_vacancies())
