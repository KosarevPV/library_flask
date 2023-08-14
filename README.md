# Тестовое задание на позицию начинающий программист/стажёр в 1AK-GROUP
### Косарев Павел
___
Для запуска проекта в ОС должен быть установлен python 3.11 и Git.

Далее необходимо выполнить следующие команды:
+ git clone https://github.com/KosarevPV/library_flask.git
+ py -3.11 library_flask\run.py
+ library_flask\venvLIB\Scripts\activate
+ python -m pip install -r library_flask\requirements.txt
+ python library_flask\app.py

___
### Технологический стек
python 3.11, Flask 2.3.2

Все зависимости в файле requirements.txt
___

### Краткое описание работы с системой
На главной странице в верхнем правом углу две кнопки "Войти" и "Зарегистрироваться". При переходе по кнопке "Войти" на странице появляется список читателей библиотеки. Читатель входит в систему, нажимая на кнопку рядом с ФИО из списка. Если читателя нет в списке, он может добавить свои данные в систему через кнопку "Зарегистрироваться". Далее читатель использую сервис, может выбрать одно из двух действий: посмотреть список доступных книг или сдать книгу. При выборе первого пункта, читатель, получает список книг с кодами на остатках в библиотеке. Он может взять книгу используя код книги, добавить книгу в библиотеку или посмотреть какие книги выданы читателям. При выборе «сдать книгу» читатель указывает код взятой книги, и система возвращает ее на остатки. Действия по взятию книг и возврату книг фиксируются в системе.
___
### Выгрузка базы данных, с указанием используемой БД
Используемая БД - SQLite

Экземпляр БД находится в директории instance