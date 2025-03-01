import unittest
from unittest import TestCase

from functions import check_age


class TestMain(TestCase):
    def test_check_age(self):
        age = -1
        expected = 'Доступ запрещён'
        result = check_age(age)

        self.assertEqual(result, expected)

    def test_check_age_2(self):
        age = 0
        expected = 'Доступ запрещён'
        result = check_age(age)
        self.assertEqual(result, expected)

    def test_check_age_3(self):
        age = 19
        expected = 'Доступ разрешён'
        result = check_age(age)
        self.assertEqual(result, expected)

