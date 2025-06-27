from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(numder_1_1: Union[int], numder_1_2: Union[int], numder_1_3: Union[int]):
    assert get_mask_card_number(numder_1_1) == "1111 22** **** 4444"
    assert get_mask_card_number(numder_1_2) == "Номер должен состоять из 16 цифр, а не меньше"
    assert get_mask_card_number(numder_1_3) == "Номер должен состоять из 16 цифр, а не больше"


@pytest.mark.parametrize(
    "value, expected",
    [
        (11111222223333344444, "**4444"),
        (12345, "Номер карты должен состоять из 20 цифр, а не меньше."),
        (1111122222333334444455555, "Номер карты должен состоять из 20 цифр, а не больше."),
    ],
)
def test_get_mask_account(value: Union[int], expected: Union[str]):
    assert get_mask_account(value) == expected
