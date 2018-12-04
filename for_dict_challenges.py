# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

counter = {}

for student in students:
    if student['first_name'] in counter:
        counter[student['first_name']] += 1
    else:
        counter[student['first_name']] = 1
for k, v in counter.items():
    print(f"{k}: {v}")

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
counter = {}

for student in students:
    if student['first_name'] in counter:
        counter[student['first_name']] += 1
    else:
        counter[student['first_name']] = 1

print(f"Самое частое имя среди учеников: {max(counter, key=counter.get)}")

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
count_list = []

for klas in school_students:
    counter = {}
    for student in klas:
        if student['first_name'] in counter:
            counter[student['first_name']] += 1
        else:
            counter[student['first_name']] = 1
    count_list.append(counter)

for c in count_list:
    print(f"Самое частое имя в классе {count_list.index(c)+1}: {max(c, key=c.get)}")

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

counter = []

for klas in school:
    counter_dic = {'class': klas['class'], 'female': 0, 'male': 0}
    for student in klas['students']:
        if is_male[student['first_name']]:
            counter_dic['male'] += 1
        else:
            counter_dic['female'] += 1
    counter.append(counter_dic)

for klas in counter:
    print(f"В классе {klas['class']} {klas['female']} девочки и {klas['male']} мальчика.")

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '3b', 'students': [{'first_name': 'Оля'}, {'first_name': 'Оля'}, {'first_name': 'Оля'}]},
    {'class': '2d', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
counter = []

for klas in school:
    counter_dic = {'class': klas['class'], 'female': 0, 'male': 0}
    for student in klas['students']:
        if is_male[student['first_name']]:
            counter_dic['male'] += 1
        else:
            counter_dic['female'] += 1
    counter.append(counter_dic)

fem_max = max(counter, key=lambda x: x['female'])
male_max = max(counter, key=lambda x: x['male'])

print(f"Больше всего мальчиков в классе {male_max['class']}")
print(f"Больше всего девочек в классе {fem_max['class']}")

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
