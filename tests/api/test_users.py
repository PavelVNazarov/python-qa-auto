# tests/api/test_users.py
import requests
import pytest
import allure


@allure.feature("Users")
@allure.title("Получение списка пользователей")
@pytest.mark.api
def test_get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    assert len(response.json()) == 10


@allure.feature("Users")
@allure.title("Создание пользователя")
@pytest.mark.api
def test_create_user():
    payload = {"name": "John Doe", "email": "john@example.com"}
    response = requests.post("https://jsonplaceholder.typicode.com/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"