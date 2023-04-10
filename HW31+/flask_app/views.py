from . import app
from random import sample, randrange
from flask import request, redirect, render_template, session, url_for, abort
import werkzeug.exceptions

app.secret_key = 'secret'


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
    if session.get('user'):
        if 'count' in request.args:
            if request.args.get('count').isdigit():
                lst2 = sample(lst_names, k=int(request.args.get('count')))
            else:
                return "Value 'count' should be a number"
        else:
            amnt_nm = randrange(1, len(lst_names))
            lst2 = sample(lst_names, k=amnt_nm)
        res = {
            'user': f'Hello {session.get("user")}',
            'lst2': lst2
        }
        return render_template('users.html', **res)
    else:
        return redirect(url_for('login'))


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
    if session.get('user'):
        if 'count' in request.args:
            if request.args.get('count').isdigit():
                lst3 = sample(lst_books, k=int(request.args.get('count')))
            else:
                return "Value 'count' should be a number"
        else:
            amnt_nm = randrange(1, len(lst_books))
            lst3 = sample(lst_books, k=amnt_nm)
        res = {
            'user': f'Hello {session.get("user")}',
            'lst3': lst3
        }
        return render_template('books.html', **res)
    else:
        return redirect(url_for('login'))


# 2
@app.route('/users/<int:n>')
def users_id(n):
    if session.get('user'):
        res = {
            'user': f'Hello {session.get("user")}',
            'n': n
        }
        if n % 2 == 0:
            return render_template('users_id.html', **res)
        else:
            return abort(404)
    else:
        return redirect(url_for('login'))


@app.route('/books/<string:n>')
def books_title(n):
    if session.get('user'):
        res = {
            'user': f'Hello {session.get("user")}',
            'n': n
        }
        return render_template('books_id.html', **res)
    else:
        return redirect(url_for('login'))


# 3
@app.get('/params')
def params():
    if session.get('user'):
        n = request.args.items()
        res = {
            'user': f'Hello {session.get("user")}',
            'n': n
        }
        return render_template('params.html', **res)
    else:
        return redirect(url_for('login'))


# 4
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if request.form.get('login') and request.form.get('password'):
            if len(request.form.get('login')) >= 5:
                if len(request.form.get('password')) >= 8 and any(map(str.isdigit, request.form.get('password'))) \
                        and any(map(str.isupper, request.form.get('password'))):
                    session['user'] = request.form.get('login')
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
    return render_template('main.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')
