from pprint import pprint
student_grades_9a = {
    "Олександр Іванович Петров": 85,
    "Марія Сергіївна Іванова": 90,
    "Дмитро Олександрович Сидоров": 78
}

student_grades_9b = {
    "Катерина Петрівна Коваленко": 88,
    "Іван Дмитрович Кузьменко": 92,
    "Ольга Вікторівна Литвиненко": 80
}

student_grades_9 = {**student_grades_9a, **student_grades_9b}

pprint(student_grades_9)

