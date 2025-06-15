def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению."""
    new_list = []
    for i in list_dict:
        if i["state"] == state:
            new_list.append(i)
        else:
            continue
    return new_list


def sort_by_date(list_dict: list, sort_: str = "True") -> list:
    """Функция сортировки по дате."""
    if sort_ == "True":
        return sorted(list_dict, key=lambda x: x["date"], reverse=True)
    else:
        return sorted(list_dict, key=lambda x: x["date"])
