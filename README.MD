install requirements: 
`pip install -r requirements.txt`

run project:
`python manage.py runserver`

run django-extensions console: 
`python manage.py shell_plus --ipython`

###работа с БД

Создаем миграцию: 
`python manage.py makemigrations`

Применяем миграцию к БД, знакомой командой: 
`python manage.py migrate`