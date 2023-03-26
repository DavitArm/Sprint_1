word_list = []
marks_list = []
CONST_MARKS = ',', '!', '.', '?'


def fills_lists(string):
    splitted_string = string.split()
    for meaning in splitted_string:
        if meaning[-1] in CONST_MARKS:
            print(meaning[-1])
            if meaning[-1] not in marks_list:
                marks_list.append(meaning[-1])
            if meaning[:-1] not in word_list:
                word_list.append(meaning[:-1])
        elif meaning not in word_list:
            word_list.append(meaning)

    print(word_list)
    print(marks_list)


fills_lists('Мне не грозит опасность, Скайлер, я сам опасность! Кто-то откроет дверь и схватит пулю. Думаешь, им '
            'буду я? Нет. Это я постучу в дверь.')
