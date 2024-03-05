# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
print("Вася:", students.count({'first_name': 'Вася'}))
print("Маша:", students.count({'first_name': 'Маша'}))
print("Петя:", students.count({'first_name': 'Петя'}))


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

print(" ")
print(" * *" * 10)
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
count_dict = dict()
for name in students:
    count_dict[name["first_name"]] = students.count(name)
print("Самое частое имя среди учеников:", max(count_dict, key=count_dict.get))


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print(" ")
print(" * *" * 10)
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
def popular_name(students):
    count_dict = dict()
    for name in students:
        count_dict[name["first_name"]] = students.count(name)
    return max(count_dict, key=count_dict.get)
for students in school_students:
    print(f"Самое частое имя в классе {school_students.index(students) + 1}: {popular_name(students)}.")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

print(" ")
print(" * *" * 10)
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for class_num in school:
    boys = 0
    girls = 0
    for name in class_num["students"]:
        if is_male[name["first_name"]]:
            boys += 1
        else:
            girls += 1
    print(f"Класс {class_num['class']}: девочки {girls}, мальчики {boys}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

print(" ")
print(" * *" * 10)
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
for class_num in school:
    boys = 0
    girls = 0
    for name in class_num["students"]:
        if is_male[name["first_name"]]:
            boys += 1
        else:
            girls += 1
    if boys > girls:
        print("Бошьше всего мальчиков в классе", class_num['class'])
    else:
        print("Больше всего девочек в классе", class_num['class'])

