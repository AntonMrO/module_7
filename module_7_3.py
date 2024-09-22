import io
from pprint import pprint

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                words = []
                punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for line in file:
                    for znak in punct:
                        line = line.replace(znak, '')       #убираем знаки пунктуации по списку punct из строки
                    line = line.lower().split()
                    for word in line:
                        words.append(word)
                    all_words[file_name] = words
        return all_words

        # метод find возвращает словарь, где ключ - название файла,
        # значение - позиция первого такого слова в списке слов этого файла
    def find(self, word):
        find_dict = {}
        for name, words in self.get_all_words().items():
            for find_word in words :
                if find_word == word.lower():
                    find_dict[name] = words.index(find_word)+1
        return find_dict

        #  метод count возвращает словарь, где ключ - название файла,
        #  значение - количество слова word в списке слов этого файла.
    def count(self, word):
        count_dict = {}
        for name, words in self.get_all_words().items():
            a = 0
            for find_word in words:
                if find_word == word.lower():
                    a += 1
                count_dict[name] = a
        return count_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.file_names)
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

#проверка 3 большими файлами
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))