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
            city = None
            address = vacancy.get("address")
            if address is not None:
                city = address.get("city")
            if city is None:
                city = "Не указано"
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
                "city": city,
                "platform": "HeadHunter"
            }
            formatted_vacancies.append(formatted_vacancy)

        return formatted_vacancies


if __name__ == "__main__":
    pprint(HeadHunterAPI('образование').get_vacancies())
