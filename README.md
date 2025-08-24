Python QA Automation Project
Описание
Автоматизация тестирования веб-приложения и REST API:

UI: https://www.saucedemo.com (Selenium WebDriver с использованием паттерна Page Object)

API: https://jsonplaceholder.typicode.com (библиотека requests)

Проект включает:

10 UI-тестов для сайта Saucedemo, покрывающих авторизацию, работу с товарами, корзиной и оформлением заказа

30 API-тестов для JSONPlaceholder, покрывающих основные CRUD-операции для ресурсов пользователей, постов, комментариев, альбомов, фотографий и задач

Технологии
Python 3.x

Pytest - фреймворк для тестирования

Selenium WebDriver - автоматизация браузера

Requests - работа с HTTP-запросами

Allure - создание отчетов о тестировании

Jenkins - непрерывная интеграция (настройка описана ниже)

Структура проекта

project/

├── conftest.py          # Фикстуры Pytest

├── pytest.ini           # Конфигурация Pytest

├── requirements.txt     # Зависимости

├── pages/               # Page Object модели

│   ├── login_page.py

│   ├── inventory_page.py

│   ├── cart_page.py

│   └── checkout_page.py

└── tests/

    ├── ui/              # UI-тесты
    │   ├── test_login.py
    │   ├── test_inventory.py
    │   ├── test_cart.py
    │   └── test_checkout.py
    └── api/             # API-тесты
        ├── test_users.py
        ├── test_posts.py
        ├── test_comments.py
        ├── test_albums.py
        ├── test_todos.py
        └── test_photos.py
Установка и запуск
Клонируйте репозиторий:

bash
git clone <repository_url>
cd <project_directory>
Установите зависимости:

bash
pip install -r requirements.txt
Запустите тесты:

bash
# Все тесты
pytest tests/ --alluredir=allure-results

# Только UI-тесты
pytest tests/ui/ -m ui --alluredir=allure-results

# Только API-тесты
pytest tests/api/ -m api --alluredir=allure-results

# Параллельный запуск (4 потока)
pytest tests/ -n 4 --alluredir=allure-results
Просмотр отчета Allure:

bash
allure serve allure-results
Настройка Jenkins
Для настройки автоматического запуска тестов в Jenkins:

Установите Jenkins и необходимые плагины (Allure, Git, Python)

Создайте новый проект (Freestyle project)

Настройте источник кода (Git) и укажите URL вашего репозитория

Добавьте шаг сборки (Execute shell):

bash
pip install -r requirements.txt
pytest tests/ --alluredir=allure-results
Добавьте пост-обработку для генерации отчета Allure: укажите путь allure-results в настройках Allure Report

Сохраните и запустите сборку

Особенности реализации
Использование паттерна Page Object для UI-тестов

Параметризация тестов для покрытия различных сценариев

Интеграция с Allure для детальных отчетов с шагами и скриншотами

Возможность параллельного запуска тестов с помощью pytest-xdist

Настройка фикстур для инициализации и закрытия браузера