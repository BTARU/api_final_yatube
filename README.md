# Учебный Проект «API для Yatube»
Проект содержит обработку запросов к блогу «Yatube». Обработав запрос, 
отправляется ответ api в формате JSON, который может обрабатывать frontend приложение.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/BTARU/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов к API:

Получить список постов (GET):

```
http://127.0.0.1:8000/api/v1/posts/
```

Получить комментарии к посту (GET):

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Получить список сообществ (GET):

```
http://127.0.0.1:8000/api/v1/groups/
```

### Полная документация по запросам:

Запустите сервер и перейдите по ссылке:

```
http://127.0.0.1:8000/redoc/
```
