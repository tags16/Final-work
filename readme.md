#### Final-work
###### Требования
```
Python >= 3.8
python-venv >= 3.8
PostgreSQL >= 13
```

###### Файл конфигурации `.env`
```
# Настройки подключения к БД
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',                      
        'USER': 'tags16',
        'PASSWORD': '******',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

###### Установка и запуск `Final-work`
1. Выполнить для скачивания проекта: `gh repo clone tags16/Final-work`
2. Создать окружение: `python -m venv venv`
3. Активировать окружение: `source venv/bin/activate`
4. Установить зависимости: `pip install -r requirements.txt`
5. Создать файл с миграцией`python manage.py makemigrations todo`
6. Выполнить миграцию `python manage.py migrate`
7. Создать супер пользователя `python3 manage.py createsuperuser`
5. Запустить проект `python manage.py runserver`
- Для остановки программы нажать: `ctrl + c`
- Деактивировать окружение: `deactivate`

###### Примечание
После запуска программы будут доступны методы: 
- Веб интерфейс Администратора `http://127.0.0.1:8000/admin/`
- Веб интерфейс приложения `http://127.0.0.1:8000/`
- API - `http://127.0.0.1:8000/api`

###### Методы API:
- GET /api/tasks - получть список всех задач
- GET /api/tasks/{id} - получть одну конкретную задачу
- POST /api/tasks - создать задачу
- PUT (или PATCH) /api/tasks/{id} - отредактировать существующую задачу
- DELETE /api/tasks/{id} - удалить одну задачу