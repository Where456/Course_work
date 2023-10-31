from pprint import pprint

import requests

from api.job_search_api import JobSearchAPI


class HeadHunterAPI(JobSearchAPI):
    def __init__(self, filter_words):
        self._url = "https://api.hh.ru"
        self.filter_words = filter_words

    def get_vacancies(self):
        params = {
            'text': self.filter_words
        }
        data = requests.get("https://api.hh.ru/vacancies", params=params).json()
        formatted_vacancies = []
        for vacancy in data['items']:
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
                "salary": vacancy.get("salary", "Не указано"),
                "description": formatted_description,
                "url": vacancy.get("alternate_url", "Не указано"),
                "platform": "HeadHunter"
            }
            formatted_vacancies.append(formatted_vacancy)

        return formatted_vacancies


if __name__ == "__main__":
    pprint(HeadHunterAPI('Профильное высшее образование').get_vacancies())
