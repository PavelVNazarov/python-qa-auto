# tests/api/test_photos.py
import requests
import pytest
import allure

BASE_URL = "https://jsonplaceholder.typicode.com"

@allure.feature("API")
@allure.story("Работа с фотографиями")
class TestPhotos:
    @allure.title("Получение всех фотографий")
    @pytest.mark.api
    def test_get_all_photos(self):
        response = requests.get(f"{BASE_URL}/photos")
        assert response.status_code == 200
        assert len(response.json()) == 5000

    @allure.title("Получение конкретной фотографии")
    @pytest.mark.api
    @pytest.mark.parametrize("photo_id", [1, 100, 1000])
    def test_get_specific_photo(self, photo_id):
        response = requests.get(f"{BASE_URL}/photos/{photo_id}")
        assert response.status_code == 200
        assert response.json()["id"] == photo_id

