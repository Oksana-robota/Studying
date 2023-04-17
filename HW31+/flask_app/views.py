import os
from . import app, db
from random import sample, randrange
from flask import request, redirect, render_template, session, url_for, abort
import werkzeug.exceptions
from .models import User, Book, Purchase



app.secret_key = os.getenv('SECRET')


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



# HW34
@app.route('/users1')
def users1():
    if request.args.get('size'):
        all_users = User.query.limit(int(request.args.get('size')))
    else:
        all_users = User.query.all()
    dict_users = [{
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'age': user.age
    } for user in all_users]
    return dict_users


@app.route('/users1/<int:user_id>')
def users1_id(user_id):
    all_users = User.query.get(user_id)
    if all_users:
        user1 = [{
            'id': all_users.id,
            'first_name': all_users.first_name,
            'last_name': all_users.last_name,
            'age': all_users.age
            }]
        return user1
    return abort(404)


@app.route('/books1')
def books1():
    if request.args.get('size'):
        all_books = Book.query.limit(int(request.args.get('size')))
    else:
        all_books = Book.query.all()
    dict_books = [{
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'year': book.year,
        'price': book.price
    } for book in all_books]
    return dict_books


@app.route('/books1/<int:book_id>')
def books1_id(book_id):
    all_books = User.query.get(book_id)
    if all_books:
        book1 = [{
            'id': all_books.id,
            'title': all_books.title,
            'author': all_books.author,
            'year': all_books.year,
            'price': all_books.price
        }]
        return book1
    return abort(404)


@app.route('/purchase')
def purchase():
    if request.args.get('size'):
        all_purchase = Purchase.query.limit(int(request.args.get('size')))
    else:
        all_purchase = Purchase.query.all()
    dict_purchase = []
    for purchase_1 in all_purchase:
        purchase_2 = {
            'id': purchase_1.id,
            'user_id': purchase_1.user_id,
            'book_id': purchase_1.book_id,
            'date': purchase_1.date,
            'title': purchase.book.title,
            'first_name': purchase.user.first_name,
            'last_name': purchase.user.last_name
        }
        dict_purchase.append(purchase_2)
    return dict_purchase


@app.route('/purchase/<int:purchases_id>')
def purchase_id(purchases_id):
    all_purchase = Purchase.query.get(purchases_id)
    if all_purchase:
        purchase_1 = [{
            'id': all_purchase.id,
            'user_id': all_purchase.user_id,
            'book_id': all_purchase.book_id,
            'date': all_purchase.date,
            'title': purchase.book.title,
            'first_name': purchase.user.first_name,
            'last_name': purchase.user.last_name
        }]
        return purchase_1
    return abort(404)


@app.route('/users1', methods=['POST', ])
def create_user():
    user = User(
        first_name=request.json.get('first_name'),
        last_name=request.json.get('last_name'),
        age=request.json.get('age')
    )
    db.session.add(user)
    db.session.commit()
    return f'User {user.id} created', 201


@app.route('/books1', methods=['POST', ])
def create_book():
    book = Book(
        title=request.json.get('title'),
        author=request.json.get('author'),
        year=request.json.get('year'),
        price=request.json.get('price')
    )
    db.session.add(book)
    db.session.commit()
    return f'Book {book.id} created', 201


@app.route('/purchase', methods=['POST', ])
def create_purchase():
    purchase1 = Purchase(
        user_id=request.json.get('user_id'),
        book_id=request.json.get('book_id'),
        date=request.json.get('date')
    )
    book1 = Book.query.get(request.json.get('book_id'))
    user1 = User.query.get(request.json.get('user_id'))
    if book1 and user1:
        db.session.add(purchase1)
        db.session.commit()
        return f'Book {purchase1.id} created', 201
    else:
        if not book1:
            return "There is no such book_id"
        elif not user1:
            return "There is no such user_id"
        else:
            return "There is no such book_id and user_id"