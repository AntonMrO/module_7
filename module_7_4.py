# print('Привет, ' + 'мир!')
# print('Меня зовут %(name)s, мне %(year)s' % {'name': 'Денис', 'year' :14})
# print('Я учусь в {title}{postfix}'.format(title='Урбан', postfix='-university'))
# print(f'{"Urban"} - это лучший университет!')
    # Домашнее задание по теме "Форматирование строк"

class Team:
    def __init__(self, team_name, team_num, score, team_time):
        self.team_name = team_name
        self.team_num = int(team_num)
        self.score = int(score)
        self.team_time = float(team_time)

    def __str__(self):
        return ('В команде %(t_name)s участников: %(t_num)s'           #пример Использование %
              % {'t_name': self.team_name, 't_num': self.team_num})    #пример Использование %

    def team_score(self):                                               #пример использования .format(...)
        return ('Команда {name} решила {score} задач'.format(name=self.team_name, score=self.score))

    def team_time_rezult(self):                                               #пример использования .format(...)
        return ('{name} решили задачи за {time} c'.format(name=self.team_name, time=self.team_time))

class Сompetitions(Team):
    def __init__(self):
        self.result = {}
        print('___Приветствуем участников соревнований, а также зрителей и болельщиков!___')

    def patisipants(self, *patisipants_team):
        tuple_team = {}
        for pat in patisipants_team:
            tuple_team[pat.team_name] = pat.team_num
        return tuple_team

    def result_2(self, t1, t2):
        if t1.score > t2.score or t1.score == t2.score and t1.team_time < t2.team_time:
            result = f'Результат битвы: Победа команды {t1.team_name}!'                        # Использование f-строк:
        elif t1.score < t2.score or t1.score == t2.score and t1.team_time > t2.team_time:
            result = f'Результат битвы: Победа команды {t2.team_name}!'                        # Использование f-строк:
        else:
            result = 'Результат битвы: Ничья!'
        return result

    def score_team2(self, t1, t2):
        score_rez = f'Команды решили {t1.score} и {t2.score} задач.'
        return score_rez

    def total_2(self, t1, t2):
        tasks_total = t1.score+t2.score
        time_avg = round((t1.team_time + t2.team_time) / tasks_total, 1)
        return f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!'


t1 = Team('Мастера кода', 5, 40, 1552.512)
t2 = Team('Волшебники данных', 6, 42, 2153.31451)

challenge_1 = Сompetitions()
    # вариант 1 применение %
cp1 = challenge_1.patisipants(t1,t2)
print('Итого сегодня в командах участников: %(Мастера кода)s и %(Волшебники данных)s' % cp1)
    # вариант 2 применение %
print('Итого сегодня в командах участников: %(t1_num)s и %(t2_num)s' % {'t1_num': t1.team_num, 't2_num': t2.team_num})


print(t1)                     #пример Использование %
print(t2)                     #пример Использование % 
print(t1.team_score())               #пример использования .format(...)
print(t2.team_score())                 #пример использования .format(...)
print(t1.team_time_rezult())             #пример использования .format(...)
print(t2.team_time_rezult())             #пример использования .format(...) 

print(challenge_1.score_team2(t1,t2))                            # Использование f-строк:
print(challenge_1.result_2(t1,t2))                               # Использование f-строк:
print(challenge_1.total_2(t1,t2))                               # Использование f-строк:


