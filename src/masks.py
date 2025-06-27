from typing import Union


def get_mask_card_number(number: Union[int]) -> str:
    """Маска номера по правилу XXXX XX** **** XXXX, где X - это цифра номера."""
    specified_number = str(number)
    mask_number = []
    if len(specified_number) == 16:
        for i in specified_number:
            mask_number.append(i)
    elif len(specified_number) <= 16:
        return "Номер должен состоять из 16 цифр, а не меньше"
    elif len(specified_number) >= 16:
        return "Номер должен состоять из 16 цифр, а не больше"
    return f"{''.join(mask_number[0:4])} {''.join(mask_number[4:6])}** **** {''.join(mask_number[-4:])}"


def get_mask_account(number: Union[int]) -> str:
    """Маска номера по правилу **XXXX, где X - это цифра номера."""
    specified_number = str(number)
    mask_number = []
    if len(specified_number) == 20:
        for i in specified_number:
            mask_number.append(i)
    elif len(specified_number) <= 20:
        return "Номер карты должен состоять из 20 цифр, а не меньше."
    elif len(specified_number) >= 20:
        return "Номер карты должен состоять из 20 цифр, а не больше."
    return f"**{''.join(mask_number[-4:])}"
