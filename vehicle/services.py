import requests
from rest_framework import status

from config import settings


def convert_currencies(rub_price):

    response = requests.get(
         f'https://api.currencyapi.com/v3/latest?apikey={settings.CURRENCY_API_KEY}&currencies=RUB'
    )

    if response.status_code == status.HTTP_200_OK:
        usd_rate = response.json()['data']['RUB']['value']

        usd_price = rub_price / usd_rate
        print(usd_price)

        return usd_price
