from flask import render_template, Blueprint, flash,  redirect, url_for
from flask_login import login_required, current_user

from library.models import Library, Card, Author, Book
from library.library.forms import CardBooksForm, CardBooksFormDelete, BooksCreate
from library import db

library = Blueprint('library', __name__)


@library.route("/library", methods=['GET', 'POST'])
@login_required
def allbooks():
    form = CardBooksForm()
    if form.validate_on_submit():
        book = Library.query.get_or_404(form.id.data)
        if book.amount == 0:
            flash('К сожалению, данной книги нет в наличии. Попробуйте позже.', 'error')
            return redirect(url_for('library.allbooks'))
        elif Card.query.filter_by(reader_id=current_user.id, book_id=form.id.data, hidden=False).count():
            flash('К сожалению, у вас уже есть такая книга.', 'warning')
            return redirect(url_for('library.allbooks'))
        else:
            book.amount -= 1
            cardbook = Card(reader_id=current_user.id, book_id=form.id.data)
            db.session.add(cardbook)
            db.session.commit()
            flash('Книга успешно взята!', 'success')
            return redirect(url_for('library.allbooks'))

    books = Library.query.all()
    return render_template('allbooks.html', books=books, form=form)


@library.route("/library/new_book", methods=['GET', 'POST'])
@login_required
def books_create():
    form = BooksCreate()
    form.author.choices = [(a.id, f'{a.name} {a.surname}') for a in Author.query.all()]

    if form.validate_on_submit():
        authors = []
        for auth in form.author.data:
            author = Author.query.get_or_404(auth)
            authors.append(author)
        book_in_library = Book.query.filter_by(title=form.title.data)
        if book_in_library.count() and any(i.author == authors for i in book_in_library):
            flash('К сожалению такая книга уже есть', 'error')
            return redirect(url_for('library.allbooks'))
        else:
            book = Book(title=form.title.data, author=authors)
            db.session.add(book)
            db.session.commit()
            book_in_library = Library(book_id=book.id, amount=form.amount.data)
            db.session.add(book_in_library)
            db.session.commit()

            flash('Книга успешно создана!', 'success')
            return redirect(url_for('library.allbooks'))

    return render_template('create_book.html', form=form)


@library.route("/library/cardbooks")
@login_required
def cardbooks():
    books = Card.query.all()
    return render_template('cardbooks.html', books=books)


@library.route("/library/cardbooks/delete", methods=['GET', 'POST'])
@login_required
def cardbooks_del():
    form = CardBooksFormDelete()
    if form.validate_on_submit():
        book = Library.query.get_or_404(form.id.data)
        book.amount += 1
#
        card_book = Card.query.filter_by(reader_id=current_user.id, book_id=form.id.data, hidden=False).first()
        if not card_book:
            flash('У вас нет такой книги!', 'warning')
            return redirect(url_for('library.cardbooks_del'))
        card_book.hidden = True
        card_book.dt_hand_over = db.func.now()
        db.session.commit()
        flash('Книга успешно возвращена в библиотеку!', 'success')
        return redirect(url_for('library.cardbooks_del'))

    books = Card.query.filter_by(reader_id=current_user.id)
    return render_template('reader_allbooks.html', books=books, form=form, legend='Взять книгу:')
