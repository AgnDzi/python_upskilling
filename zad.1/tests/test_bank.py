import pytest
from bank import Bank
from client import Client


#@pytest.fixture
#   def bank():
#   return Bank()

def test_add_client():  #tutaj:test_add_client(bank) i usunac linijke z bankiem
    bank = Bank()
    client = Client("Aga", 1000)
    bank.add_client(client)
    assert len(bank.clients) == 1

def test_remove_client():
    bank = Bank()
    client = Client("Aga", 1000)
    bank.add_client(client)
    bank.remove(client.id)
    assert len(bank.clients) == 0

def test_get_client():
    bank = Bank()
    client = Client("Aga", 1000)
    bank.add_client(client)
    bank_client = bank.get_client(client.id)
    assert bank_client == client
