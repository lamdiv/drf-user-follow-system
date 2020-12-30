$ python -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
$ cd cottage/
$ python manage.py migrate
$ python manage.py makemigrations
$ python manage.py runserver
