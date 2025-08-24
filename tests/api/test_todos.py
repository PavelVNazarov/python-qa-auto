# tests/api/test_todos.py
import requests
import pytest
import allure

BASE_URL = "https://jsonplaceholder.typicode.com"

@allure.feature("API")
@allure.story("Работа с задачами")
class TestTodos:
    @allure.title("Получение всех задач")
    @pytest.mark.api
    def test_get_all_todos(self):
        response = requests.get(f"{BASE_URL}/todos")
        assert response.status_code == 200
        assert len(response.json()) == 200

    @allure.title("Получение задач пользователя")
    @pytest.mark.api
    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_get_user_todos(self, user_id):
        response = requests.get(f"{BASE_URL}/todos?userId={user_id}")
        assert response.status_code == 200
        assert all(todo["userId"] == user_id for todo in response.json())

    @allure.title("Изменение статуса задачи")
    @pytest.mark.api
    @pytest.mark.parametrize("todo_id", [1, 2, 3])
    def test_update_todo_status(self, todo_id):
        payload = {"completed": True}
        response = requests.patch(f"{BASE_URL}/todos/{todo_id}", json=payload)
        assert response.status_code == 200
        assert response.json()["completed"] == True

