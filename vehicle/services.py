import json

import requests
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from rest_framework import status

from config import settings
from datetime import datetime, timedelta


def convert_currencies(rub_price):

    response = requests.get(
         f'https://api.currencyapi.com/v3/latest?apikey={settings.CURRENCY_API_KEY}&currencies=RUB'
    )

    if response.status_code == status.HTTP_200_OK:
        usd_rate = response.json()['data']['RUB']['value']

        usd_price = rub_price / usd_rate
        print(usd_price)

        return usd_price


# def set_schedule(*args, **kwargs):
#     """
#     Задаем параметры задач
#     """
#     # Создаем интервал для повтора
#     schedule, created = IntervalSchedule.objects.get_or_create(
#         every=10,
#         period=IntervalSchedule.SECONDS,
#     )
#
#     # Создаем задачу для повторения
#     PeriodicTask.objects.create(
#         interval=schedule,
#         name='Importing contacts',
#         task='proj.tasks.import_contacts',
#         args=json.dumps(['arg1', 'arg2']),
#         kwargs=json.dumps({
#             'be_careful': True,
#         }),
#         expires=datetime.utcnow() + timedelta(seconds=30)
#     )
