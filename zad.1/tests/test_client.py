import pytest
from client import Client

def test_depositing():
    client = Client("Aga", 1000)
    client.depositing(200)
    assert client.balance == 1200

def test_withdrawing():
    client = Client("Aga", 1000)
    client.withdrawing(200)
    assert client.balance == 800

def test_withdrawing_negativ_amount():
    client = Client("Aga", 1000)
    with pytest.raises(ValueError):
        client.withdrawing(-100)

def test_depositing_negative_amount():
    client = Client("Aga", 1000)
    with pytest.raises(ValueError):
        client.depositing(-100)