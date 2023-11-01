import json


class JSONSaver:
    def __init__(self):
        self.file_name = "vacancies.json"
        self.vacancies = []
        self.load_from_json()
        self.current_id = 1

    def __str__(self):
        return f"JSONSaver for {self.file_name}"

    def add_vacancy(self, vacancy):
        """
        Добавляет вакансию в список.

        :param vacancy: Экземпляр вакансии
        :return: None
        """
        self.vacancies.append(vars(vacancy))
        self.save_to_json()

    def read_vacancy(self, vacancy_id):
        """
        Возвращает информацию о вакансии по идентификатору.

        :param vacancy_id: Идентификатор вакансии
        :return: Информация о вакансии в виде словаря
        """
        for vacancy in self.vacancies:
            if vacancy.get('id') == vacancy_id:
                return vacancy
        return None

    def update_vacancy(self, vacancy_id, name=None, url=None, salary=None, description=None):
        """
        Обновляет информацию о вакансии.

        :param vacancy_id: Идентификатор вакансии
        :param name: Новое название вакансии (опционально)
        :param url: Новая ссылка (опционально)
        :param salary: Новая зарплата (опционально)
        :param description: Новое описание (опционально)
        :return: Информация о вакансии после обновления
        """
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
        """
        Удаляет вакансию из списка.

        :param vacancy: Экземпляр вакансии
        :return: None
        """
        self.vacancies.remove(vars(vacancy))
        self.save_to_json()

    def get_vacancies_by_salary(self, salary_range):
        """
        Возвращает список вакансий с указанным диапазоном зарплат.

        :param salary_range: Диапазон зарплат (например, "100 000-150 000 руб.")
        :return: Список вакансий
        """
        filtered_vacancies = [v for v in self.vacancies if v['salary'] == salary_range]
        return filtered_vacancies

    def parse_salary(self, salary_str):
        """
        Разбирает строку с информацией о зарплате и возвращает словарь.

        :param salary_str: Строка с информацией о зарплате
        :return: Словарь с информацией о зарплате
        """
        parts = salary_str.split(' - ')
        if len(parts) == 2:
            currency = "rub"
            from_salary = int(parts[0].replace(' ', ''))
            to_salary = int(parts[1].replace(' ', ''))
            return {"currency": currency, "from": from_salary, "to": to_salary}
        return None

    def save_to_json(self):
        """
        Сохраняет вакансии в формате JSON.

        :return: None
        """
        with open(self.file_name, 'w') as file:
            json.dump(self.vacancies, file)

    def load_from_json(self):
        """
        Загружает вакансии из JSON
        """
        try:
            with open(self.file_name, 'r') as file:
                self.vacancies = json.load(file)
        except FileNotFoundError:
            self.vacancies = []
