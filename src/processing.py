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
