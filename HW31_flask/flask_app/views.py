from app import app
from random import sample, randrange
from flask import request, redirect
from markupsafe import escape
import werkzeug.exceptions


@app.route('/hello')
def index():
    app.logger.info("This INFO request")
    app.logger.error("This ERROR request")
    return "Hello, world!"


# 1
@app.route('/users')
def users():
    lst_names = ["Савва", "Савелий", "Святослав", "Севастьян", "Семен", "Сергей", "Сидор", "Станислав",
                 "Степан", "Тамаз", "Тарас", "Тигран", "Тимофей",
                 "Тимур", "Тихон", "Томас", "Федор", "Федот", "Феликс",
                 "Филипп", "Фома", "Фред", "Фридрих", "Харитон", "Чарльз",
                 "Чеслав", "Шамиль", "Эдгар", "Эдуард", "Александра", "Алена",
                 "Алина", "Алиса", "Алла", "Алсу", "Альба", "Альбина", "Аля", "Амалия",
                 "Амина", "Анастасия", "Ангелина", "Анжела", "Анжелика", "Анисья",
                 "Анна", "Антонина", "Аполлинария", "Арина", "Астрид", "Белла", "Берта", "Валентина"]
    if request.args:
        lst2 = sample(lst_names, k=int(request.args.get('count')))
    else:
        amnt_nm = randrange(1, len(lst_names))
        lst2 = sample(lst_names, k=amnt_nm)
    return f'<div>{lst2}</div>'


@app.route('/books')
def books():
    lst_books = ["Мастер и Маргарита", "Собачье сердце", "Двенадцать стульев", "Мёртвые души",
                 "Граф Монте-Кристо", "Золотой теленок", "Три товарища", "Отверженные",
                 "Преступление и наказание", "Евгений Онегин", "Война и мир", "Повести Белкина",
                 "Ревизор", "Село Степанчиково и его обитатели", "Отцы и дети", "Палата № 6",
                 "Три мушкетера", "Братья Карамазовы", "Идиот", "Собака Баскервилей", "Рудин",
                 "Приключения Шерлока Холмса", "Дубровский", "Горе от ума", "Драма на охоте",
                 "Капитанская дочка", "Униженные и оскорблённые", "Воскресение", "Дворянское гнездо",
                 "Рассказы", "Триумфальная арка", "Подросток", "Старик и море"]
    if request.args:
        lst3 = sample(lst_books, k=int(request.args.get('count')))
    else:
        amnt_nm = randrange(1, len(lst_books))
        lst3 = sample(lst_books, k=amnt_nm)
    res = '<ul>'
    for i in lst3:
        res += f'<li>{i}</li>'
    res += '</ul>'
    return f"<div>{res}</div>"


# 2
@app.route('/users/<int:n>')
def users_id(n):
    if n % 2 == 0:
        return f'{n / 2}'
    return 'Not Found', 404


@app.route('/books/<string:n>')
def books_title(n):
    return f'{n.title()}'


# 3
@app.get('/params')
def params():
    res = '''<table>
                    <tr>
                        <th>parameter</th>
                        <th style="border-left: 1px solid;">value</th>
                    </tr>'''
    for key, value in request.args.items():
        res += f'<tr><td>{escape(key)}</td>' \
               f'<td style="border-left: 1px solid;">{escape(value)}</td></tr>'
    res += '</table>'
    return f"<div>{res}</div>"


# 4
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        html_form = """
        <form method=POST action='/login'>
            <input type='string' name='login' value="" />
            <input type='password' name='password' value="" />
            <button type='submit'>Send form</button>
        </form>
        """
        return html_form, 200
    elif request.method == 'POST':
        if request.form.get('login') and request.form.get('password'):
            if len(request.form.get('login')) >= 5:
                if len(request.form.get('password')) >= 8 and any(map(str.isdigit, request.form.get('password')))\
                        and any(map(str.isupper, request.form.get('password'))):
                    return redirect('/users')
                else:
                    return "Password should contain at least 8 symbols, 1 number and 1 title letter"
            else:
                return "Login should contain at least 5 symbols"
        else:
            return 'Data is absent', 400


# 5
@app.errorhandler(werkzeug.exceptions.NotFound)
def default_404(e):
    return "<div>Opps!!! Not found such page</div>"


@app.errorhandler(werkzeug.exceptions.InternalServerError)
def default_500(e):
    return "<div>You are facing Internal Server Error!!!</div>"


# 6
@app.route('/')
def main_page():
    return f'''<div><a href='/login'>login</a><div>
                <div><a href='/users'>users</a></div>
                <div><a href='/books'>books</a></div>
                <div><a href='/params'>params</a></div>'''
