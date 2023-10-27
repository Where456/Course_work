import json
from pprint import pprint

import requests

from api.job_search_api import JobSearchAPI
from models.vacancy import Vacancy

api_key = "v3.r.137899498.4a842559739b24559f0afc94b6f0300c26d4cd70.04e66d11930307f72907f40fa7524aade14c0814"

headers = {'Host': 'api.superjob.ru',
           'X-Api-App-Id': api_key,
           'Authorisation': f'Bearer {api_key[3:]}',
           'Content-Type': 'application/x-www-form-urlencoded'}


class SuperJobAPI(JobSearchAPI):
    def __init__(self):
        self._auth = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers)
        self.response = self._auth.text

    def get_vacancies(self):
        vacancies = json.loads(self.response)
        formatted_vacancies = []

        for vacancy in vacancies["objects"]:
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
                'salary': Vacancy('', '', '', '').parse_salary(formatted_salary),
                'description': vacancy.get('candidat', 'Не указано'),
                'id': vacancy.get('id', 'Не указано'),
                'alternate_url': vacancy.get('link', 'Не указано'),
                'platform': 'SuperJob'
            }

            formatted_vacancies.append(formatted_vacancy)

        return formatted_vacancies



