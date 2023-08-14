from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    name = StringField('Имя:', validators=[DataRequired(), Length(min=2, max=120)])
    surname = StringField('Фамилия:', validators=[DataRequired(), Length(min=2, max=120)])
    patronymic = StringField('Отчество:', validators=[DataRequired(), Length(min=2, max=120)])

    submit = SubmitField('Зарегистрироваться')
