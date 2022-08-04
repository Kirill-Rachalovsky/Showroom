import pytest
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from src.customer.models import Customer

url = "/api/v1/customer/list/"
detail_url = "/api/v1/customer/detail/"

payload = dict(
    username="harryPovar",
    first_name="Harry",
    last_name="Potter",
    email="h.potter@hogwarts.com",
    password="sovabesit"
)
payload2 = dict(
    username="redhair",
    first_name="Ron",
    last_name="Weasley",
    email="weaslwy@hogwarts.com",
    password="redWeasley"
)


@pytest.mark.django_db
def test_customer_get(client, auth_client, get_responses):
    """
    Ensure that anybody can get a list of Customers.
    Ensure that only authenticated users can get a detail list of Customers.
    """
    assert get_responses(client=client, url=url) == 200
    assert get_responses(client=auth_client, url=detail_url) == 200
    assert get_responses(client=client, url=detail_url) == 403


@pytest.mark.django_db
@pytest.mark.parametrize("payload, payload2", [
    (payload, payload2),
    (payload2, payload),
])
def test_customer_post(payload, payload2, client, auth_client, post_responses):
    """
    Ensure that only authorized user can create a Customer.
    """
    assert post_responses(client=client, url=detail_url, payload=payload).status_code == 403
    assert post_responses(client=auth_client, url=detail_url, payload=payload).status_code == 201
    assert post_responses(client=auth_client, url=detail_url, payload=payload2).data["username"] == payload2["username"]


@pytest.mark.django_db
def test_customer_details(client, auth_client, details_responses, post_responses):
    """
    Ensure that anybody can get info about separate Customer.
    """
    post_responses(client=auth_client, url=detail_url, payload=payload)
    assert details_responses(client=client, url=url, model=Customer, payload=payload) == 200
    assert details_responses(client=client, url=detail_url, model=Customer, payload=payload) == 403
    assert details_responses(client=auth_client, url=detail_url, model=Customer, payload=payload) == 200




