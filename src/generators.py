from typing import Union


def filter_by_currency(transactions: list[dict], currency: Union[str]):
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор,который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    result = [x for x in transactions if x["operationAmount"]["currency"]["code"] == currency]
    x = 0
    while True:
        yield result[x]
        x += 1


def transaction_descriptions(transactions: list[dict]) :
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    result = [x["description"] for x in transactions]
    x = 0
    while True:
        yield result[x]
        x += 1


def card_number_generator(start: Union[int], stop: Union[int]) -> Union[str]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    result_numb = []
    if start < stop:
        if stop > 9999999999999999:
            return "Максимальная длинна номера 16."
        else:
            result = [x for x in range(start, stop + 1) if 1 <= x <= 9999999999999999]
            for resul in result:
                quantity_0 = 16 - int(len(str(resul)))
                final_number = quantity_0 * "0" + str(resul)
                semiresult = ""
                semiresult += final_number[:4] + " "
                semiresult += final_number[4:8] + " "
                semiresult += final_number[8:12] + " "
                semiresult += final_number[12:]
                result_numb.append(semiresult)
    elif start > stop:
        return "Диапазон должен задаваться от меньшего числа к большему, а не наоборот."
    return "\n".join(result_numb)
