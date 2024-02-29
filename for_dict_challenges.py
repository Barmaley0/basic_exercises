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
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
lists = []
for values in students:
    lists.append(values['first_name'])
for item in lists:
    if lists.count(item) > 1:
        print(f"Частое имя среди учеников: {item}.")
        break


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

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
CLASS_NUM_1 = 0
CLASS_NUM_2 = 1
CLASS_NUM_3 = 2

def class_number(school_student, num_class):
    list1 = []
    for item1 in range(len(school_student[num_class])):
        list1.append(school_students[num_class][item1]['first_name'])
    for value1 in list1:
        if list1.count(value1) > 1:
            print(f"Частое имя в классе {num_class + 1}: {value1}.")
            break

class_number(school_students, CLASS_NUM_1)
class_number(school_students, CLASS_NUM_2)
class_number(school_students, CLASS_NUM_3)


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

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
CLASS_2A = 0
CLASS_2B = 1
CLASS_2V = 2

def name_list(school1, class_num, is_mal):
    boys = 0
    girls = 0
    name = school1[class_num]["students"]
    for val in name:
        if is_mal[val["first_name"]] is False:
            girls += 1
        elif is_mal[val["first_name"]] is True:
            boys += 1
    print(f"Класс {school1[class_num]['class']}: девочки {girls}, мальчики {boys}")

name_list(school,CLASS_2A, is_male)
name_list(school,CLASS_2B, is_male)
name_list(school,CLASS_2V, is_male)

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

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
CLASS_2A = 0
CLASS_3C = 1

def class_list(school2, class_numb, is_males):
    boys = 0
    girls = 0
    name = school2[class_numb]["students"]
    for val in name:
        if is_males[val["first_name"]] is False:
            girls += 1
        elif is_males[val["first_name"]] is True:
            boys += 1
    if girls > boys:
        print(f"Больше всего девочек в классе {school2[class_numb]['class']}")
    elif boys > girls:
        print(f"Больше всего мальчиков в классе {school2[class_numb]['class']}")

class_list(school, CLASS_2A, is_male)
class_list(school, CLASS_3C, is_male)

