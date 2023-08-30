# habit_tracker_spa_web_application


## Описание

Проект представляет собой backend часть веб-приложения трекер полезных привычек (SPA). Реализовано API с помощью Django REST
Framework.

## Технологии:

- Python, Django, Django REST Framework
- Django ORM
- Docker
- PostgreSQL
- Celery, Redis
- PyTelegramBotAPI

## Функциональность

- Регистрация и аутентификация пользователей
- CRUD операции с привычками через API
- Публичные и приватные привычки
- Поля: место, время, действие, периодичность и др.
- Валидация данных в сериализаторах
- Фильтрация и пагинация списка привычек
- Напоминания о привычках через Telegram бота

## Данные

**Основные сущности данных:**

- Пользователи
- Привычки (Приятные, полезные)


## API

**Основные endpoint's:**

- /habits/ - CRUD привычек
- /users/ - CRUD пользователей


#### Документация доступна в Swagger/Redoс.

## Запуск проекта

1. #### Клонировать репозиторий, перейти в папку проекта.

2. #### Создать и активировать виртуальное окружение.

3. #### Установить зависимости:

```
pip install -r requirements.txt
```

4.  #### Установить и настроить сервисы:

- PostgreSQL
- Redis

5. #### Выполнить миграции:

```
python manage.py migrate
```

6. #### Загрузка данных

- Для загрузки начальных данных в БД:

```
python manage.py loaddata db.json
```

7. #### Запустить dev-сервер:

```
python manage.py runserver
```

- Доступно по адресу http://localhost:8000

8. #### Создание периодической задачи на проверку статуса платежей

```
python manage.py add_tasks
```

9. #### Запуск Celery

```
celery -A config worker -l INFO -P eventlet
```

10. #### Запуск celery-beat

```
celery -A config worker --loglevel=info
```

## Тестирование

- Для запуска тестов:

```
python manage.py test
```

## Покрытие кода тестами

- Запуск:

```
coverage run --source='.' manage.py test
```

```
coverage report
```

## Документация

### Документация доступна по адресам:

```bash
http://localhost:8000 /redoc/ или /swagger/
```
## Docker
- для начала создайте отдельный файл `.env.docker` и пропишите там свои настройки. Смотрите шаблон `.env.sample`:

### Сборка образа и запуск в фоне после успешной сборки
```
docker-compose up -d —build
```
- для остановки
```
docker-compose down