# tests/api/test_comments.py
import requests
import pytest
import allure

BASE_URL = "https://jsonplaceholder.typicode.com"

@allure.feature("API")
@allure.story("Работа с комментариями")
class TestComments:
    @allure.title("Получение комментариев к посту")
    @pytest.mark.api
    @pytest.mark.parametrize("post_id", [1, 2, 3])
    def test_get_post_comments(self, post_id):
        response = requests.get(f"{BASE_URL}/posts/{post_id}/comments")
        assert response.status_code == 200
        assert all(comment["postId"] == post_id for comment in response.json())

    @allure.title("Создание комментария")
    @pytest.mark.api
    def test_create_comment(self):
        payload = {
            "postId": 1,
            "name": "Test Comment",
            "email": "test@example.com",
            "body": "This is a test comment"
        }
        response = requests.post(f"{BASE_URL}/comments", json=payload)
        assert response.status_code == 201
        assert response.json()["name"] == "Test Comment"

