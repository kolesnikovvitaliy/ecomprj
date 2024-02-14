# Training Shop
## Интернет-магазин на Django

#### Technologies Used:
Python
Django
Django-debug-toolbar
Django-jazzmin
Poetry
#### Проект является интернет-магазином:
#### Использовалось в проекте:
```bash
  * Frontend - Bootstrap 5
  * Backend - Django 5.0.2
  * DataBases - Sqlite 3
```
## Описание проекта.

*  В данном e-comerce решении используются 9 приложений:
```bash
  - "core" - раздел (функционал) самого  магазина с категориями и товарами.  
#   - "cart" - корзина для покупок товара.
#   - "orders" - оформление заказов, запись их в БД.
#   - "users" - регистрация и авторизация пользователе(возможность востановить пароль или изменить наомер ntktajyf)
#   - "cupons" - применение скидок и акций
#   - "foto_gallery" - добавление фотографий на сайт с сохранением в БД
#   - "contact_form" - заказа обратного звонка с записью в БД
#   - "feedback" - форма обратной связи с БД и почтовой рассылкой 
#   - "payment" - приложение электронной оплаты картой или яндекс деньгами в данном случае настроина но отключенна
#  ``` 
# Через админ панель можно:
#   - Добавлять, удалять товары и категории а так же 
# описание к ним.
#   - Просматривать и отмечать заказы.
#   - Добавлять и удалять купоны на скидки.
#   - Просматривать пользователей и их профили.
#   - Просматривать базу контаков и сообщений обратной связи пользователей,
#   - Наполнять фотогалерею.
#   - Вывести заказы в CSV файл.

# Пользователи могут:
#   - Выбирать категории товаров,
#   - Выбирать товары, 
#   - Добавлять в корзину, 
#   - Применять купоны на скидки, 
#   - Оформлять заказы,
#   - Просматривать фотогалерею,
#   - Заполнять формы обратной связи. 

# После оформления заказа присылается сообщение по электронной почте, с деталями заказа а так же PDF файл. 

# Реализованна регистрация и 
# авторизация пользователей.

# Профиль пользователя с возможностью просмотра заказов.

# В форме обратной связи пользователь может отправить свое сообщение

## Документация по проекту.

### Для запуска проекта необходимо:

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
# python manage.py collectstatic
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

# Screenshots :

<div class="img-div">
  <img src="https://github.com/kolesnikovvitaliy/ecomprj/blob/main/docs/img/scrin_site.png" width="800"/>
</div>

#

<div class="img-div">
  <img src="https://github.com/kolesnikovvitaliy/ecomprj/blob/main/docs/img/scrin_admin.png" width="800"/>
</div>

