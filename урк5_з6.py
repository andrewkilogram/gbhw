lesson = 'Урок 5, задание 6 \n'

print(lesson)
print('Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.\n')

with open("text_6.txt", encoding="utf-8") as text_file:
    for line in text_file.readlines():
        my_line = "".join((i if i in "0123456789" else " ") for i in line).split()
        sum_line = sum([int(i) for i in my_line])
        print(line.split()[0], sum_line)

# Код из разбора дз, мне показался самым логичным и читаемым.
# Переписал его, попутно изучая что и как работает, узнал пару интересных приёмов.

# Извиняюсь что в этом задании без своего кода, если бы у меня была неделя времени
# на это задание, я бы конечно что-то еле работающее накарябал, но если не сдавать дз
# вовремя, то времени на другие задания вообще не останется.
