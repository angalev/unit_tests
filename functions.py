import os
import requests as r
from dotenv import load_dotenv


def check_age(age: int):

    if age >= 18: # Введите условие для проверки возраста
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'

    return result

def check_month(month: int):

    if month in [3, 4, 5]:
        result = 'Весна'
    elif month in [6, 7, 8]:
        result = 'Лето'
    elif month in [9, 10, 11]:
        result = 'Осень'
    elif month in [12, 1, 2]:
        result = 'Зима'
    else:
        result = 'Некорректный номер месяца'
    return result

def check_email(email: str) -> bool:

    if ' ' in email:
        return False
    elif '@' in email and '.' in email:
        return True
    else:
        return False

def create_folder_yd():
    load_dotenv()
    ytoken = os.getenv("YTOKEN")
    yadi_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': f'OAuth {ytoken}'}
    params = {'path': f'new_folder'}
    response = r.put(yadi_url, headers=headers, params=params)
    print(response)
    return response
