# Python QA Automation Homework

## Описание
Автоматизация тестирования:
- UI: https://www.saucedemo.com (Selenium + PageObject)
- API: https://jsonplaceholder.typicode.com (requests)

## Запуск
```bash
pip install -r requirements.txt
pytest tests/ --alluredir=allure-results
allure serve allure-results