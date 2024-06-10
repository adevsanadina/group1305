from pywebio.input import input as input_pw
from pywebio.input import NUMBER, TEXT
from pywebio.output import put_text,put_image
from pywebio import start_server

user_name = input_pw('Доброго дня,введіть свій псевдонім:')
def quiz():
    total_score = 0

    # questuion 1
    q1 = input_pw("Скільки буде 2 + 2?", type=NUMBER, required=True)
    if q1 == 4:
        total_score += 1

    # questuion 2
    q2 = input_pw("Скільки хромосом у здорової людини?", type=NUMBER, required=True)
    if q2 == 46:
        total_score += 1

    # questuion 3
    q3= input_pw("Скільки областей в Україні?", type=NUMBER, required=True)
    if q3 == 24:
        total_score += 1

    # questuion 4
    q4 = input_pw("Яка національна страва в Україні?", type=TEXT, required=True)
    if q4 == "Борщ":
        total_score += 1

    # questuion 5
    q5 = input_pw("Назвіть символ України:", type=TEXT, required=True)
    if q5 == "Тризуб":
        total_score += 1

    put_text(f"{user_name}, ваш результат: {total_score}/5 балів.")

    if total_score == 5:
        img = open('five_stars.jpeg', 'rb').read()
        put_image(img, width="700px")

if __name__ == '__main__':
    start_server(quiz() ,port=11000)