import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def json_file(way: str) -> list[dict]:
    """функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о
    финансовых транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(way, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            return []
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


def transaction_amount(transaction: dict):
    """функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения
    текущего курса валют и конвертации суммы операции в рубли."""
    if transaction == {}:
        return "Нет транзакции!"
    else:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            return float(transaction["operationAmount"]["amount"])
        elif (
            transaction["operationAmount"]["currency"]["code"] == "USD"
            or transaction["operationAmount"]["currency"]["code"] == "EUR"
        ):
            value = float(transaction["operationAmount"]["amount"])
            if transaction["operationAmount"]["currency"]["code"] == "EUR":
                url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={value}"
            elif transaction["operationAmount"]["currency"]["code"] == "USD":
                url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={value}"
            payload = {}
            headers = {"apikey": f"{API_KEY}"}
            response = requests.get(url, headers=headers, data=payload)
            status_code = response.status_code
            if status_code == 200:
                convert_amount = response.json()
                result = convert_amount["result"]
                return result
            elif status_code == 400:
                return "Запрос содержит синтаксическую ошибку или неверные параметры."
            elif status_code == 500:
                return "На стороне сервера произошла непредвиденная ошибка, которая не позволила выполнить запрос."
