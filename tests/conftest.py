import pytest


@pytest.fixture
def numder_1_1() -> int:
    return 1111222233334444


@pytest.fixture
def numder_1_2() -> int:
    return 111122223333


@pytest.fixture
def numder_1_3() -> int:
    return 11112222333344445555


@pytest.fixture
def widget_1_1() -> str:
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def widget_1_2() -> str:
    return "Счет 73654108430135874305"


@pytest.fixture
def processing_1_1() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def processing_1_2() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
