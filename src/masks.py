from typing import Union


def get_mask_card_number(number: Union[int]) -> str:
    """Маска номера по правилу XXXX XX** **** XXXX, где X - это цифра номера."""
    specified_number = str(number)
    mask_number = []
    for i in specified_number:
        mask_number.append(i)
    return f"{''.join(mask_number[0:4])} {''.join(mask_number[4:6])}** **** {''.join(mask_number[-4:])}"


def get_mask_account(number: Union[int]) -> str:
    """Маска номера по правилу **XXXX, где X - это цифра номера."""
    specified_number = str(number)
    mask_number = []
    for i in specified_number:
        mask_number.append(i)
    return f"**{''.join(mask_number[-4:])}"
