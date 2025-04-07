import pytest
from transaction import Transaction
from datetime import datetime
from trans_enum import TransType
from enum import Enum
from dataclasses import dataclass

# def test_creation():
#     transaction = Transaction("123","Alice", "deposit", 100)
#     assert transaction.client_id == "123"
#     assert transaction.client_name == "Alice"
#     assert transaction.transaction_type == "deposit"
#     assert transaction.transaction_amount == 100

def test_creation():
    transaction = Transaction("123","Alice", TransType.DEPOSIT, 100.0, datetime.now())
    assert transaction.client_id == "123"
    assert transaction.client_name == "Alice"
    assert transaction.transaction_type == TransType.DEPOSIT
    assert transaction.transaction_amount == 100
    assert isinstance(transaction.transaction_date, datetime)