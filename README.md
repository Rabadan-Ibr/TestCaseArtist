# TestCaseArtist
Тестовая работа
```
Соберите с помощью Django Rest Framework каталог исполнителей и их альбомов с песнями такой структуры:

Исполнитель

-Название

Альбом

-Исполнитель
-Год выпуска

Песня

-Название

Порядковый номер в альбоме
Одна и та же песня может быть включена в несколько альбомов, но под разными порядковыми номерами.
```
#### Инструкция по развертыванию в контейнере.
Должен быть установлен Docker\
Скачать репозиторий.\
Выполнить команды из каталога с docker-compose.yml:

Создать образы и развернуть контейнеры.
```commandline
docker-compose up -d
```
Выполнить миграции.
```commandline
docker-compose exec web python manage.py migrate
```
При желании загрузить дамп с данными для проверки.
```commandline
docker-compose exec web python manage.py loaddata db.json
```
Для админки:\
Логин: admin\
Пароль: admin

Документация: http://127.0.0.1/docs/

Получить исполнителей с альбомами: http://127.0.0.1/api/v1/artists/

Получить альбомы: http://127.0.0.1/api/v1/albums/

Получить список песен: http://127.0.0.1/api/v1/songs/

Создание сущностей, POST запросы на эти же ендпоинты. Есть возможность создавать через админку.