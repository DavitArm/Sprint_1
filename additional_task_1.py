tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

t = []
new_tickets = {}
tickets_by_type = {}


def del_list_dubl():
    for key, value in tickets.items():
        new_tickets[key] = [x for x in value if x not in t]
        t.extend(value)
    return new_tickets


def new_tickets_by_type(_types,_new_tickets):
    for key in _types:
        tickets_by_type[_types[key]] = new_tickets[key]
    return tickets_by_type
