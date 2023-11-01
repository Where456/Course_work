import json
import os
from pprint import pprint

import requests
from dotenv import load_dotenv

from api.job_search_api import JobSearchAPI

load_dotenv()
api_key = os.getenv('api_key')


class SuperJobAPI(JobSearchAPI):
    def __init__(self, filter_words):
        self._api_key = api_key
        self.filter_words = filter_words
        self.headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': self._api_key,
            'Authorisation': f'Bearer {self._api_key[3:]}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.params = {
            'keywords': self.filter_words
        }
        self.response = self.authenticate()

    def authenticate(self):
        return requests.get('https://api.superjob.ru/2.0/vacancies/', headers=self.headers, params=self.params).text

    def get_vacancies(self):
        vacancies = json.loads(self.response)
        formatted_vacancies = []

        for vacancy in vacancies["objects"]:
            city = "Не указано"
            address = vacancy.get('address')
            if address is not None:
                city_parts = address.split(',')
                if len(city_parts) > 0:
                    city = city_parts[0].strip()
            currency = vacancy.get("currency", "Не указано")
            payment_from = vacancy.get("payment_from", "Не указано")
            payment_to = vacancy.get("payment_to", "Не указано")

            formatted_salary = {
                "currency": currency,
                "from": payment_from,
                "to": payment_to
            }
            formatted_vacancy = {
                'name': vacancy.get('profession', 'Не указано'),
                'salary': formatted_salary,
                'description': vacancy.get('candidat', 'Не указано'),
                'city': city,
                'id': vacancy.get('id', 'Не указано'),
                'alternate_url': vacancy.get('link', 'Не указано'),
                'platform': 'SuperJob'
            }

            formatted_vacancies.append(formatted_vacancy)

        return pprint(formatted_vacancies)


# print(SuperJobAPI('образование').get_vacancies())