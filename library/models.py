from datetime import datetime
from library import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Reader.query.get(int(user_id))


class Reader(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    surname = db.Column(db.String(120), nullable=False)
    patronymic = db.Column(db.String(120), nullable=False)
    card = db.relationship('Card', uselist=False, backref='reader')

    def __repr__(self):
        return f"Читатель('{self.surname}' '{self.name}' '{self.patronymic}')"


book_author = db.Table(
    'book_author',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id')),
)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    surname = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Автор('{self.surname}' '{self.name}')"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.relationship('Author', secondary=book_author)
    card = db.relationship('Card', uselist=False, backref='book')
    library = db.relationship('Library', uselist=False, backref='book')

    def __repr__(self):
        return f"Книга('{self.title}')"


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reader_id = db.Column(db.Integer, db.ForeignKey('reader.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    dt_created = db.Column(db.DateTime, default=datetime.utcnow, server_default=db.func.now())
    dt_hand_over = db.Column(db.DateTime, nullable=True)
    hidden = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"Читатель '{self.reader_id}' взял книгу '{self.book_id}'"


class Library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    amount = db.Column(db.Integer)

    def __repr__(self):
        return f"Книга '{self.book_id}', количество '{self.amount}'"
