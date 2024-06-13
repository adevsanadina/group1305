from pywebio.input import textarea, select, checkbox, radio, input as input_pw, slider
from pywebio.output import put_success, put_text, put_html
from pywebio.session import run_js
from pywebio import start_server

options_of_genres = ['Жахи', 'Фентезі', 'Комедія', 'Драма', 'Бойовик', 'Детектив', 'Містика']
emotions = ['Офігенний', 'Не сподобався']

reviews_info = []


def review():
    put_html('<h1>Відгук про фільм</h1>')
    name = input_pw('Введіть своє імя:')
    title_of_film = input_pw('Введіть назву фільма:')
    genres_of_film = select('Оберіть жанр фільму:', options=options_of_genres)
    short_review = textarea('Дайте короткий відгук про фільм:')
    rating_of_film = slider('Рейтинг', min_value=1, max_value=10)
    if rating_of_film > 7:
        put_success('Дякую за відгук! Ви високо оцінили цей фільм.')
    else:
        put_text('Дякую за відгук!')
    your_emotions = checkbox('Які емоції викликав у вас цей фільм?', options=emotions)
    recommendations = radio('Чи рекомендуєте ви цей фільм?', options=['Так', 'Ні'])

    reviews_info.append([name, title_of_film, genres_of_film, short_review, rating_of_film, your_emotions, recommendations])
    run_js('setTimeout(function(){location.reload();},4000')


if __name__ == '__main__':
    start_server(review, port=18000)

