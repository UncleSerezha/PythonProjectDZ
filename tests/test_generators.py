from typing import Union

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(generators_1_1: list[dict]) -> None:
    generator = filter_by_currency(generators_1_1, "USD")
    assert next(generator) == {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
    assert next(filter_by_currency(generators_1_1, "RUB")) =={
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        }


def test_transaction_descriptions(generators_1_1: list[dict]) -> None:
    generator = transaction_descriptions(generators_1_1)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_card_number_generator(
    generators_1_2: Union[int], generators_1_3: Union[int], generators_1_4: Union[int], generators_1_5: Union[int]
) -> None:
    assert card_number_generator(generators_1_2, 5) == (
        "0000 0000 0000 0003\n0000 0000 0000 0004\n" "0000 0000 0000 0005"
    )
    assert card_number_generator(generators_1_3, 101) == ("0000 0000 0000 0100\n0000 0000 0000 0101")
    assert card_number_generator(generators_1_4, 99999999999999999) == "Максимальная длинна номера 16."
    assert card_number_generator(generators_1_5, 9) == (
        "Диапазон должен задаваться от меньшего числа к большему," " а не наоборот."
    )
