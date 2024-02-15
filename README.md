# Training Shop
## Интернет-магазин на Django

#### Technologies Used:
Python \
Django \
Django-debug-toolbar \
Django-jazzmin \
Poetry \
#### Проект является интернет-магазином:
#### Использовалось в проекте:
```bash
  * Frontend - Bootstrap 5
  * Backend - Django 5.0.2
  * DataBases - Sqlite 3
```
## Описание проекта.

*  В данном e-commerce решении используются приложения:
```bash
  - "core" - раздел (функционал) самого  магазина с категориями и товарами.  
```

* Создать и перейти в директорию, которую будет скопирован проект.
```bash
mkdir django-project
cd django-project
```
* Скопировать репозиторий себе на локальный компьютер
```bash
git clone https://github.com/kolesnikovvitaliy/ecomprj.git
```
* Перейти в директорию ecomprj
```bash
cd ecomprj
```

* Установить зависимости:
```bash
poetry install
```

* Активировать виртуальное окружение 
```bash
source .venv/bin/activate 
```

### Выполнить следующие команды:

* Команда создания миграций приложения для базы данных
```bash
poetry run python manage.py migrate --noinput
```
* Команда для регистрации статистических файлов приложения 
```bash
poetry run python manage.py makemigrations --noinput
```
* Команда для регистрации суперпользователя базы данных - "admin". Можете заменить на желаемое.
```bash
echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', '','admin' )" | poetry run python manage.py shell
```
* Команда для запуска приложения:
```bash
poetry run python manage.py runserver
```
> Используйте адрес: http://localhost:8000
> Админ панель: http://localhost:8000

# Screenshots Site:

<div class="img-div">
  <img src="https://github.com/kolesnikovvitaliy/ecomprj/blob/main/docs/img/scrin_site.png" width="800"/>
</div>

# Screenshots Admin:

<div class="img-div">
  <img src="https://github.com/kolesnikovvitaliy/ecomprj/blob/main/docs/img/scrin_admin.png" width="800"/>
</div>

