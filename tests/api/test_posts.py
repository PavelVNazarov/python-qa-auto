# tests/api/test_posts.py
import requests
import pytest
import allure

BASE_URL = "https://jsonplaceholder.typicode.com"

@allure.feature("API")
@allure.story("Работа с постами")
class TestPosts:
    @allure.title("Получение всех постов")
    @pytest.mark.api
    def test_get_all_posts(self):
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200
        assert len(response.json()) > 0

    @allure.title("Получение конкретного поста")
    @pytest.mark.api
    @pytest.mark.parametrize("post_id", [1, 5, 10])
    def test_get_specific_post(self, post_id):
        response = requests.get(f"{BASE_URL}/posts/{post_id}")
        assert response.status_code == 200
        assert response.json()["id"] == post_id

    @allure.title("Создание нового поста")
    @pytest.mark.api
    def test_create_post(self):
        payload = {"title": "Test Post", "body": "This is a test post", "userId": 1}
        response = requests.post(f"{BASE_URL}/posts", json=payload)
        assert response.status_code == 201
        assert response.json()["title"] == "Test Post"

    @allure.title("Обновление поста")
    @pytest.mark.api
    @pytest.mark.parametrize("post_id", [1, 2, 3])
    def test_update_post(self, post_id):
        payload = {"title": "Updated Post", "body": "This post has been updated", "userId": 1}
        response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)
        assert response.status_code == 200
        assert response.json()["title"] == "Updated Post"

    @allure.title("Удаление поста")
    @pytest.mark.api
    @pytest.mark.parametrize("post_id", [1, 2, 3])
    def test_delete_post(self, post_id):
        response = requests.delete(f"{BASE_URL}/posts/{post_id}")
        assert response.status_code == 200

