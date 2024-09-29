import os, time

directory = '.'
print(os.getcwd())

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file) # Полный путь к файлу
        # if not os.path.exists(filepath): # Проверка на существование файла
        #     continue
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, '
              f'Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')