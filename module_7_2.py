# import io
from pprint import pprint

strings_positions = {}

def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
        # первый рабочий вариант цикла (меньше кода):
    for row in strings:
        bb = file.tell()
        file.write(row+'\n')
        strings_positions[(strings.index(row)+1, bb)] = row

        # второй рабочий вариант цикла:
    # for row in range(len(strings)):
    #     bb = file.tell()
    #     file.write(strings[row]+'\n')
    #     strings_positions[(row+1, bb)] = strings[row]
    file.close()
    return strings_positions

info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!',
        'Happy life!',
        'Разрушители мифов',
        '20.12.2014']


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)