students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
    'Олексій Іванов': {
         'Пошта': 'olexii@gmail.com',
         'Вік': 25,
         'Номер телефону': '+380985551221',
         'Середній бал': 85
      },
}

print("Список студентів із середнім балом більше 90:")
for name, data in students.items():
    if data['Середній бал'] > 90:
        print(f"{name}: Середній бал = {data['Середній бал']}")


total_score = sum(student['Середній бал'] for student in students.values())
average_score = total_score / len(students)
print(f"Середній бал по групі: {average_score:}")


for name, data in students.items():
    if data['Номер телефону'] is None:
        data['Номер телефону'] = '+380981231234'


print("Оновлена інформація про студентів:")
for name, data in students.items():
    print(f"Ім'я: {name}, Вік: {data['Вік']}, Пошта: {data['Пошта']}, Номер телефону: {data['Номер телефону']}, Середній бал: {data['Середній бал']}")

