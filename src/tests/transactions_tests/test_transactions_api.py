import pytest

showroom_deals_url = "/api/v1/deals/dealer_showroom/"
customer_deals_url = "/api/v1/deals/showroom_customer/"


@pytest.mark.django_db
def test_showroom_deals_get(client, auth_client, admin_customer, get_responses):
    """
    Ensure that anybody can get a list of Dealers.
    """
    admin_customer = admin_customer()

    assert get_responses(client=client, url=showroom_deals_url) == 200
    assert get_responses(client=auth_client, url=showroom_deals_url) == 200
    assert get_responses(client=admin_customer, url=showroom_deals_url) == 200


@pytest.mark.django_db
def test_customer_deals_get(client, auth_client, admin_customer, get_responses):
    """
    Ensure that anybody can get a list of Dealers.
    """
    admin_customer = admin_customer()

    assert get_responses(client=client, url=customer_deals_url) == 200
    assert get_responses(client=auth_client, url=customer_deals_url) == 200
    assert get_responses(client=admin_customer, url=customer_deals_url) == 200



