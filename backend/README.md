# Бекенд проекта MoviesToWatch

## Стек технологий
 - Фреймворк: Django
 - Среда разработки: Pycharm Pro
 - База данных: postgresql
 - Тесты: pytest 

## Запуск
Для успешной работы необходимо создать базу данных. Она описана в файле mycourse/settings.py.

```
python manage.py runserver 127.0.0.1:8000
```

## Запуск тестов
(Необходимо наличие библиотек: pytest_django, pytest_bdd, pytest_mock)

```
pytest
```

### Установка зависимостей 

(К сожалению не все зависимости описаны в файле, смотри установку зависимостей в gitlab-ci)

```
pip3 install -r requirements.txt
```

### Создание миграции 

Создание таблиц базы данных

```
python3 ./manage.py makemigrations
python3 ./manage.py migrate
```

### Создание суперпользователя

```
python3 ./manage.py createsuperuser
```

### Заполнение базы данных 

```
ptyhon3 ./manage.py fillDB
```