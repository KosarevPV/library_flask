from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField, SelectMultipleField
from wtforms.validators import DataRequired, Length


class CardBooksForm(FlaskForm):
    id = IntegerField('Код книги', validators=[DataRequired()])
    submit = SubmitField('Взять книгу')


class CardBooksFormDelete(FlaskForm):
    id = IntegerField('Код книги', validators=[DataRequired()])
    submit = SubmitField('Вернуть книгу')


class BooksCreate(FlaskForm):

    title = StringField('Название книги:', validators=[DataRequired(), Length(min=2, max=120)])
    author = SelectMultipleField('Авторы', choices=[], coerce=int)
    amount = IntegerField('Передать в библиотеку, шт.', validators=[DataRequired()])

    submit = SubmitField('Создать книгу')
