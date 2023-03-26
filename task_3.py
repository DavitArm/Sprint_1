files = {
    'cool_movie.avi': ['X'],
    'math_summary.docx': ['R', 'W'],
    'war_and_peace.txt': ['R', 'W', 'X']
}
operations = {
    'read': 'R',
    'write': 'W',
    'execute': 'X'
}


def file_action(action):
    splitted_action = action.split(' ')
    possible_action = files.get(splitted_action[1])
    wanted_action = operations.get(splitted_action[0])
    if possible_action is None:
        print('Non-existent action')
    elif wanted_action in possible_action:
        print('OK')
    else:
        print('Acces Denied')
