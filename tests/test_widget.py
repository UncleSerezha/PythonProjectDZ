from typing import Union

import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(widget_1_1: Union[str], widget_1_2: Union[str]) -> None:
    assert mask_account_card(widget_1_1) == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card(widget_1_2) == "Счет **4305"


@pytest.mark.parametrize(
    "value_2, expected_2",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2021-04-12T02:26:18.671407", "12.04.2021"),
        ("2020-01-22T02:2", "22.01.2020"),
    ],
)
def test_get_date(value_2: Union[str], expected_2: Union[str]) -> None:
    assert get_date(value_2) == expected_2
