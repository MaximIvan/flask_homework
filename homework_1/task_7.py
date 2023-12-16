'''
Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через
контекст
'''

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def news():
    context = [
        {'title': 'yesterday',
         'short_description': 'Самые важные события недели',
         'date': '24.01.2024'},
        {'title': 'today',
         'short_description': 'На сколько поднимут пенсию',
         'date': '25.01.2024'},
        {'title': 'tomorrow',
         'short_description': 'Новинки в hitech',
         'date': '26.01.2024'},
    ]

    return render_template('news.html', news = context)

if __name__ == "__main__":
    app.run(debug=True)