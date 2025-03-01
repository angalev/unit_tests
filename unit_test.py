import os
import requests as r
import unittest
from unittest import TestCase
from dotenv import load_dotenv
from functions import check_age, check_month, check_email, create_folder_yd


class TestMain(TestCase):
    def test_age_with_params(self):
        for i, (age, expected) in enumerate((
                (-19, 'Доступ запрещён'),
                (0, 'Доступ запрещён'),
                (17, 'Доступ запрещён'),
                (18, 'Доступ разрешён'),
                (3000, 'Доступ разрешён')
        )):
            with self.subTest(i):
                result = check_age(age)
                self.assertEqual(expected, result)

    def test_check_month_params(self):
        for i, (month, expected) in enumerate((
                (0, 'Некорректный номер месяца'),
                (-1, 'Некорректный номер месяца'),
                (1, 'Зима'),
                (12, 'Зима'),
                (7, 'Лето'),
                (13, 'Некорректный номер месяца'),
        )):
            with self.subTest(i):
                result = check_month(month)
                self.assertEqual(expected, result)

    @unittest.expectedFailure
    def test_check_email(self):
        for i, (email, expected) in enumerate((
                ('aaa@bbb.ccc', True),
                ('.@com.ru', False),
                ('x.y@z', False),
                ('!#$%@.com', False)
        )):
            with self.subTest(i):
                result = check_email(email)
                self.assertEqual(expected, result)

    def test_create_folder_yd(self):
        response = create_folder_yd().status_code // 100
        self.assertEqual(response, 2)

    def test_folder_exists(self):
        load_dotenv()
        ytoken = os.getenv("YTOKEN")
        yadi_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Authorization': f'OAuth {ytoken}'}
        params = {'path': f'new_folder'}
        response = r.get(yadi_url, headers=headers, params=params)
        self.assertEqual(response.status_code, 200)

    def test_request_failure(self):
        response = create_folder_yd().status_code // 100
        self.assertEqual(response, 4)

