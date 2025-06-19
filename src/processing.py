def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению."""
    new_list = []
    for i in list_dict:
        if i["state"] == state:
            new_list.append(i)
    return new_list


def sort_by_date(list_dict: list[dict], sort_order: bool = True) -> list[dict]:
    """Функция сортировки по дате"""
    if sort_order is True:
        return sorted(list_dict, key=lambda x: x["date"], reverse=True)
    else:
        return sorted(list_dict, key=lambda x: x["date"])
