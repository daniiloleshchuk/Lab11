# Лабораторна 11
- Напишіть код лабораторної роботи №3 на мові Python
- При написанні коду його слід організувати по папках 
- Слід дотримуватись code conventions для мови Python
- Код слід залити в окремий репозиторій 
- Робити поля приватними непотрібно!
- Реалізувати покриття основної логіки коду тестами (методів пошуку і сортування)

# Лабораторна 12
Реалізувати REST-сервіс (операції GET/POST/PUT/DELETE) для одного з класу з лабораторної роботи 11 з використанням засобів мови Python:
Nginx-1.12.2
uWSGI-2.0.16
Flask
Python 3.x
2. Реалізувати збереження об'єкту класу з лабораторної роботи 11 в базі даних з використанням наступного технологічного стеку 
SQLAlchemy-1.1.15
MySQL-5.7 / MySQL-8.0 (в залежності від того, яку базу даних було обрано в 8-й роботі)
Важливо: обраний клас для збереження має відрізнятись від класу, який використовувався в 8-й роботі

Інструкція по Flask доступна за посиланням: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

PIP installation: https://pip.pypa.io/en/latest/installing/

Flask: https://ru.wikibooks.org/wiki/Flask


Перед виконанням роботи слід пересвідчитись що на вашому комп’ютері встановлено Python 3 та налаштовані змінні середовища, як описано в першій презентації по мові Python

1. Для створення віртуального середовища необхідно запустити команду: 
python3 -m venv venv (Unix/Linux/Mac) or py instead python for Windows

2. Встановлення Pipenv
Pipenv - це система управління залежностями для мови Python. На відміну від мови Java системи управління maven, в мові Python використовується концепція віртуальних середовищ. Віртуальне середовище - це фактично налаштована робоча машина під потреби конкретного проекту. Але є одне але: Pipenv дозволить розробляти проекти, які вимагають різні версії Python. Для використання різних версій мови Java застосовуються плагіни (maven-compiler-plugin) та змінні середовища. 
Встановлення:
pip install --user pipenv
Або pip3 install --user pipenv 

3. Встановлення virtualenv
Virtualenv - це інструмент для створення ізольованих середовищ Python. virtualenv створює папку, яка містить всі необхідні виконувані файли, щоб використовувати пакети, необхідні для проекту на мові Python.
pip install virtualenv
4. Активізуйте ваше віртуальне середовище з використанням команди: 
source my_project/bin/activate 
#source project/venv/bin/activate
or venv\Scripts\activate.batv for Windows

5. Встановіть фласк виконавши команду: pip3 install flask


MySQL driver for python: https://dev..mysql.com/downloads/connector/python/
Connect String: mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
Mysqldriver installation: 

pip install mysql-connector 
or 
pip3 install mysql-connector

  509  pip3 install flask
  544  pip3 install flask_sqlalchemy
  551  pip3 install mysql-connectorpip3 install mysql-connector
  622  pip3 install flask_marshmallow


HOWTO: https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12
