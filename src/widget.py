from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(line_with_number: Union[str]) -> Union[str]:
    """Маска номера по правилу XXXX XX** **** XXXX или **XXXX, где X - это цифра номера."""
    mask_number = []
    x = line_with_number.split()
    if x[0] == "Счет":
        for i in x:
            if i.isalpha():
                mask_number.append(i)
            elif i.isnumeric():
                mask_number.append(get_mask_account(i))
            else:
                continue
    else:
        for i in x:
            if i.isalpha():
                mask_number.append(i)
            elif i.isnumeric():
                mask_number.append(get_mask_card_number(i))
            else:
                continue
    return " ".join(mask_number)


def get_date(date: Union[str]) -> str:
    """строка с датой в формате ДД.ММ.ГГГГ"""
    x = date.split("-")
    return f"{x[2][0:2]}.{x[1]}.{x[0]}"
