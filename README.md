# Training Shop
## Интернет-магазин на Django

#### Technologies Used:
Python \
Django \
Django-debug-toolbar \
Django-jazzmin \
Poetry 


```bash
  * Frontend - Bootstrap 5
  * Backend - Django 4.2.10
  * DataBases - Sqlite 3
```
## Описание проекта.

*  В данном e-commerce решении используются приложения:
```bash
  - "core" - раздел (функционал) самого  магазина с категориями и товарами.
  - "userauths" - приложение для регистрации и аутентификации пользователей  
```

* Создать и перейти в директорию.
```bash
mkdir django-project
cd django-project
```
* Скопировать репозиторий на свой локальный компьютер
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

* Команда для регистрации статистических файлов приложения 
```bash
poetry run python manage.py makemigrations --noinput
```

* Команда создания миграций приложения для базы данных
```bash
poetry run python manage.py migrate --noinput
```

* Команда для регистрации суперпользователя базы данных  
```bash
poetry run python manage.py createsuperuser
```
### ИЛИ 

* Команда для регистрации суперпользователя базы данных \
  email - "admin@example.com" \
  password - "admin"
```bash
echo "from userauths.models import User; User.objects.filter(email='admin@example.com').exists() or User.objects.create_superuser('admin', 'admin@example.com','admin' )" | poetry run python manage.py shell
```
* Команда для запуска приложения:
```bash
poetry run python manage.py runserver
```
> Используйте адрес: http://localhost:8000 \
> Админ панель: http://localhost:8000/admin \
> Регистрация: http://localhost:8000/sign-up \
> Аутентификация: http://localhost:8000/sign-in

# Screenshots Site:

<div class="img-div">
  <img src="https://github.com/kolesnikovvitaliy/ecomprj/blob/main/docs/img/screenshot_site.png" width="800"/>
</div>

# Database Diagram

<div class="img-div">
  <img src="https://github.com/kolesnikovvitaliy/ecomprj/blob/main/docs/img/db.png" width="800"/>
</div>


# Screenshots Admin:

<div class="img-div">
  <img src="https://github.com/kolesnikovvitaliy/ecomprj/blob/main/docs/img/screenshot_admin_.png" width="800"/>
</div>

# Screenshots Sign-up

<div class="img-div">
  <img src="https://github.com/kolesnikovvitaliy/ecomprj/blob/main/docs/img/screenshot_sign-up_.png" width="800"/>
</div>

# Screenshots Sign-in

<div class="img-div">
  <img src="https://github.com/kolesnikovvitaliy/ecomprj/blob/main/docs/img/screenshot_sign-in_.png" width="800"/>
</div>