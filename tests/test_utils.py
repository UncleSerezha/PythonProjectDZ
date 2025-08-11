import unittest
from unittest.mock import mock_open, patch

from src.utils import json_file, transaction_amount


class TestJsonFile(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data='[{"key": "value"}]')
    def test_correct_list(self, mock_file):
        result = json_file("dummy_path")
        self.assertEqual(result, [{"key": "value"}])


if __name__ == "__main__":
    unittest.main()


class TestTransactionAmount(unittest.TestCase):
    def test_rub_transaction(self):
        transaction = {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}
        result = transaction_amount(transaction)
        self.assertEqual(result, 1000.0)


if __name__ == "__main__":
    unittest.main()


# class TestTransactionAmount(unittest.TestCase):
@patch("requests.get")
def test_eur_transaction(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1754645105, "rate": 92.513769},
        "date": "2025-08-08",
        "result": 1000.11,
    }
    assert (
        transaction_amount(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == 1000.11
    )


if __name__ == "__main__":
    unittest.main()


@patch("requests.get")
def test_eur_transaction_400(mock_get):
    mock_get.return_value.status_code = 400
    assert transaction_amount(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    ) == ("Запрос содержит синтаксическую ошибку или неверные параметры.")


if __name__ == "__main__":
    unittest.main()


@patch("requests.get")
def test_eur_transaction_500(mock_get):
    mock_get.return_value.status_code = 500
    assert (
        transaction_amount(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == "На стороне сервера произошла непредвиденная ошибка, которая не позволила выполнить запрос."
    )


if __name__ == "__main__":
    unittest.main()
