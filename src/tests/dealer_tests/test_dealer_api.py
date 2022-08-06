import pytest

from src.dealer.models import Dealer

url = "/api/v1/dealer/list/"
detail_url = "/api/v1/dealer/detail/"

payload = dict(
    name="BMW dealer center",
    description="Drive your dream",
    country="DE",
    start_year="2000"
)
update_payload = dict(
    name="BMW dealer center",
    description="Drive your dream, but be careful",
    country="BY",
    start_year="2017"
)

payload1 = dict(
    name="Tesla",
    description="Fast and quiet",
    country="US",
    start_year="2012"
)
update_payload1 = dict(
    name="Tesla",
    description="Fast and quiet. Elon make it",
    country="US",
    start_year="2008"
)


@pytest.mark.django_db
def test_dealer_get(client, auth_client, admin_customer, get_responses):
    """
    Ensure that anybody can get a list of Dealers.
    """
    admin_customer = admin_customer()

    assert get_responses(client=client, url=url) == 200
    assert get_responses(client=auth_client, url=url) == 200
    assert get_responses(client=auth_client, url=detail_url) == 403
    assert get_responses(client=admin_customer, url=detail_url) == 200


@pytest.mark.django_db
@pytest.mark.parametrize("payload, payload1", [
    (payload, payload1),
    (payload1, payload)
])
def test_shipper_post(payload, payload1, client, auth_client, admin_customer, post_responses):
    """
    Ensure that only authorized user can create a Dealer.
    """
    admin_customer = admin_customer()

    assert post_responses(client=client, url=detail_url, payload=payload).status_code == 403
    assert post_responses(client=auth_client, url=detail_url, payload=payload).status_code == 403
    assert post_responses(client=admin_customer, url=detail_url, payload=payload).status_code == 201
    assert post_responses(client=admin_customer, url=detail_url, payload=payload1).data["name"] == payload1["name"]


@pytest.mark.django_db
def test_dealer_details(client, auth_client, admin_customer, details_responses, post_responses):
    """
    Ensure that only admin can get detail info about separate Dealer.
    """

    admin_customer = admin_customer()
    post_responses(client=admin_customer, url=detail_url, payload=payload)

    assert details_responses(client=client, url=url, model=Dealer, payload=payload) == 200
    assert details_responses(client=auth_client, url=url, model=Dealer, payload=payload) == 200
    assert details_responses(client=auth_client, url=detail_url, model=Dealer, payload=payload) == 403
    assert details_responses(client=admin_customer, url=detail_url, model=Dealer, payload=payload) == 200


@pytest.mark.django_db
def test_dealer_delete(client, auth_client, admin_customer, delete_responses, post_responses):
    """
    Ensure that only admin can delete a Dealer.
    """

    admin_customer = admin_customer()
    post_responses(client=admin_customer, url=detail_url, payload=payload)

    assert delete_responses(client=client, url=detail_url, model=Dealer, payload=payload) == 403
    assert delete_responses(client=auth_client, url=detail_url, model=Dealer, payload=payload) == 403
    assert delete_responses(client=admin_customer, url=detail_url, model=Dealer, payload=payload) == 204


@pytest.mark.django_db
@pytest.mark.parametrize("payload, update_payload", [
    (payload, update_payload),
    (payload1, update_payload1)
])
def test_customer_put(payload, update_payload, auth_client, admin_customer, put_responses, post_responses):
    """
    Ensure that only admin can update a Dealer.
    """

    admin_customer = admin_customer()
    post_responses(client=admin_customer, url=detail_url, payload=payload)

    assert put_responses(
        client=auth_client,
        url=url,
        model=Dealer,
        payload=payload,
        update_payload=update_payload
    ) == 403

    assert put_responses(
        client=auth_client,
        url=detail_url,
        model=Dealer,
        payload=payload,
        update_payload=update_payload
    ) == 403

    assert put_responses(
        client=admin_customer,
        url=detail_url,
        model=Dealer,
        payload=payload,
        update_payload=update_payload
    ) == 200
