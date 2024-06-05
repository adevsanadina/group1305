from pywebio.output import put_html, put_text, put_image
from pywebio.input import input as input_pw

put_html('<h1> Вітаю із закінченням навчального року,бажаю чудових канікул та насолоди від літньої пори!</h1>')
put_text("""✿ ✿ ✿ Літо, літо золоте,
        Скільки сонця, скільки світла!
        Нас в дорозі день не втомить,
        Сонце грає, сміється привітно ✿ ✿ ✿!""")


plans_for_the_summer = input_pw('Напишіть про ваші плани на це спекотне літо:')

put_text(f'Кількість символів: {len(plans_for_the_summer)}')

img = open('65124271.jpg', 'rb') .read()
put_image(img,width='500px')

