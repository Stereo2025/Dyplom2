import pytest
from rest_framework.test import APIClient
from django.urls import reverse, NoReverseMatch
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def user_data():
    return {
        'email': 'test@mail.com',
        'first_name': 'Test',
        'last_name': 'User',
        'phone': '1234567890',
        'password': 'Complex#Pass1234',
        're_password': 'Complex#Pass1234',
    }


@pytest.fixture
def create_user(db, user_data):
    user_data_copy = user_data.copy()
    del user_data_copy['re_password']
    user = User.objects.create_user(**user_data_copy)
    return user


@pytest.fixture
def api_client():
    return APIClient()


def authenticate_user(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def authenticated_client(api_client, create_user):
    return authenticate_user(api_client, create_user)


def test_create_user(api_client, user_data, db):
    url = reverse('users-list')
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    }
    response = api_client.post(url, user_data, headers=headers)
    print(response.data)
    assert response.status_code == 201
    assert User.objects.filter(email=user_data['email']).exists()


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_list_users(authenticated_client, user_data, db):
    # Обеспечим уникальность email каждого теста
    user_data['email'] = 'unique_test@mail.com'
    url = reverse('user-list')
    response = authenticated_client.post(url, data=user_data)
    print(response.data)
    # Проверка статус-кода и данных ответа
    assert response.status_code == 201
    assert response.data['email'] == user_data['email']
    assert response.data['first_name'] == user_data['first_name']
    assert response.data['last_name'] == user_data['last_name']
    assert response.data['phone'] == user_data['phone']

    # Проверка, что база данных очищена,
    # Один пользователь, который используется для аутентификации, и один вновь созданный
    assert User.objects.count() == 2


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_retrieve_user(authenticated_client, create_user):
    url = reverse('user-detail', args=[create_user.id])
    response = authenticated_client.get(url)
    print(response.data)
    assert response.status_code == 200
    assert response.data['email'] == create_user.email
    assert response.data['first_name'] == create_user.first_name
    assert response.data['last_name'] == create_user.last_name
    assert response.data['phone'] == create_user.phone


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_update_user(authenticated_client, create_user, user_data):
    url = reverse('user-detail', args=[create_user.id])
    updated_data = user_data.copy()
    updated_data['first_name'] = "Updated"
    response = authenticated_client.put(url, updated_data, format='json')
    assert response.status_code == 200
    create_user.refresh_from_db()
    assert create_user.first_name == "Updated"


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_delete_user(authenticated_client, create_user):
    url = reverse('user-me')

    data = {
        'current_password': 'Complex#Pass1234'
    }
    response = authenticated_client.delete(url, data=data, format='json')
    print(response.data)
    assert response.status_code == 204, f"Ошибка при выполнении запроса DELETE. Статус код: {response.status_code}"

    user_exists = User.objects.filter(id=create_user.id).exists()
    assert not user_exists, "Пользователь не был удален."
