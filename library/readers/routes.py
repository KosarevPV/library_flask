from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user
from library import db
from library.models import Reader
from library.readers.forms import RegistrationForm

readers = Blueprint('readers', __name__)


@readers.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        reader = Reader.query.filter_by(name=form.name.data, surname=form.surname.data,
                                        patronymic=form.patronymic.data).first()
        if reader:
            flash('Данный читатель существует. Пожалуйста, выберите другое имя.', 'error')
            return redirect(url_for('readers.register'))
        reader = Reader(name=form.name.data, surname=form.surname.data, patronymic=form.patronymic.data)
        db.session.add(reader)
        db.session.commit()
        flash('Ваша учетная запись была создана!'
              ' Теперь вы можете войти в систему', 'success')
        return redirect(url_for('readers.login'))
    return render_template('register.html', title='Register', form=form)


@readers.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    if request.method == 'GET':
        return render_template('login.html', readers=Reader.query.all())

    if request.method == 'POST':
        reader = Reader.query.filter_by(id=request.form['id']).first()
        login_user(reader)
        return redirect(url_for('main.home'))


@readers.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))
