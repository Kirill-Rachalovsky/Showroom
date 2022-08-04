import pytest
from rest_framework.test import APIClient

from src.customer.models import Customer


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def auth_client():
    auth_client = APIClient()
    user = Customer.objects.create_user(username='kirill', password='kirill_password')
    auth_client.force_login(user)
    return auth_client


def _get_responses(client, url):
    return client.get(url).status_code


@pytest.fixture
def get_responses():
    return _get_responses


def _post_responses(client, url, payload):
    return client.post(url, payload)


@pytest.fixture
def post_responses():
    return _post_responses


def _details_responses(client, url, model, payload):
    username = payload["username"]
    data_id = str(model.objects.get(username=username).id)
    return client.get(url + data_id + "/").status_code


@pytest.fixture
def details_responses():
    return _details_responses


def _put_responses(client, url, model, payload, update_payload):
    name = payload["name"]
    data_id = str(model.objects.get(name=name).id)
    return client.put(url + data_id + "/", update_payload).status_code


@pytest.fixture
def put_responses():
    return _put_responses


def _delete_responses(client, url, model, payload):
    name = payload["name"]
    data_id = str(model.objects.get(name=name).id)
    return client.delete(url + data_id + "/").status_code


@pytest.fixture
def delete_responses():
    return _delete_responses

