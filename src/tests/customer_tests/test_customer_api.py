import pytest

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
update_payload = dict(
    username="HarryPotter",
    first_name="Harry",
    last_name="Potter",
    email="harry.potter@hogwarts.com",
    password="sovabesit"
)
payload1 = dict(
    username="redhair",
    first_name="Ron",
    last_name="Weasley",
    email="weaslwy@hogwarts.com",
    password="redWeasley"
)
update_payload1 = dict(
    username="RedHair_Ron",
    first_name="Ron",
    last_name="Weasley",
    email="ronweaslwy@hogwarts.com",
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
@pytest.mark.parametrize("payload, payload1", [
    (payload, payload1),
    (payload1, payload),
])
def test_customer_post(payload, payload1, client, auth_client, post_responses):
    """
    Ensure that anybody can create a Customer.
    Ensure that only authenticated users can get a detail information of Customers.
    """
    assert post_responses(client=client, url=detail_url, payload=payload).status_code == 403
    assert post_responses(client=auth_client, url=detail_url, payload=payload).status_code == 201
    assert post_responses(client=auth_client, url=detail_url, payload=payload1).data["username"] == payload1["username"]


@pytest.mark.django_db
def test_customer_details_get(client, auth_client, customer, details_responses, post_responses):
    """
    Ensure that only user and admin can get detail info about this user.
    """
    customer = customer(payload)

    assert details_responses(client=client, url=url, model=Customer, payload=payload) == 200
    assert details_responses(client=client, url=detail_url, model=Customer, payload=payload) == 403
    assert details_responses(client=auth_client, url=detail_url, model=Customer, payload=payload) == 403
    assert details_responses(client=customer, url=detail_url, model=Customer, payload=payload) == 200


@pytest.mark.django_db
def test_customer_delete(client, auth_client, customer, delete_responses, post_responses):
    """
    Ensure that only page owner adn admin can delete a Customer.
    """
    customer = customer(payload)

    assert delete_responses(client=client, url=detail_url, model=Customer, payload=payload) == 403
    assert delete_responses(client=auth_client, url=detail_url, model=Customer, payload=payload) == 403
    assert delete_responses(client=customer, url=detail_url, model=Customer, payload=payload) == 204


@pytest.mark.django_db
@pytest.mark.parametrize("payload, update_payload", [
    (payload, update_payload),
    (payload1, update_payload1)
])
def test_customer_put(payload, update_payload, client, auth_client, customer, put_responses, post_responses):
    """
    Ensure that only authorized user can update a Customer.
    """

    customer = customer(payload)

    assert put_responses(client=client,
                         url=detail_url,
                         model=Customer,
                         payload=payload,
                         update_payload=update_payload) == 403
    assert put_responses(client=auth_client,
                         url=detail_url,
                         model=Customer,
                         payload=payload,
                         update_payload=update_payload) == 403
    assert put_responses(client=customer,
                         url=detail_url,
                         model=Customer,
                         payload=payload,
                         update_payload=update_payload) == 200
