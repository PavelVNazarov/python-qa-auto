# tests/api/test_albums.py
import requests
import pytest
import allure

BASE_URL = "https://jsonplaceholder.typicode.com"

@allure.feature("API")
@allure.story("Работа с альбомами")
class TestAlbums:
    @allure.title("Получение всех альбомов")
    @pytest.mark.api
    def test_get_all_albums(self):
        response = requests.get(f"{BASE_URL}/albums")
        assert response.status_code == 200
        assert len(response.json()) == 100

    @allure.title("Получение конкретного альбома")
    @pytest.mark.api
    @pytest.mark.parametrize("album_id", [1, 25, 50])
    def test_get_specific_album(self, album_id):
        response = requests.get(f"{BASE_URL}/albums/{album_id}")
        assert response.status_code == 200
        assert response.json()["id"] == album_id

    @allure.title("Получение фото в альбоме")
    @pytest.mark.api
    @pytest.mark.parametrize("album_id", [1, 2, 3])
    def test_get_album_photos(self, album_id):
        response = requests.get(f"{BASE_URL}/albums/{album_id}/photos")
        assert response.status_code == 200
        assert all(photo["albumId"] == album_id for photo in response.json())
