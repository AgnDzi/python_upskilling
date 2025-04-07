import uuid
from transaction import Transaction
from trans_enum import TransType
from datetime import datetime

class Client:
    def __init__(self, name, balance=0.0):
        self.id = uuid.uuid4()
        self.name = name
        self.balance = balance
        self.transactions = []

    def depositing(self, amount):
        if amount <=0:
            raise ValueError("Deposit amount must be higher than 0")
        else:
            self.balance += amount
            transaction = Transaction(self.id, self.name, TransType.DEPOSIT, amount, datetime.now())
            self.transactions.append(transaction)

    def withdrawing(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be higher than 0")
        if amount <= self.balance:
            self.balance -= amount
            transaction = Transaction(self.id, self.name, TransType.WITHDRAW, amount, datetime.now())
            self.transactions.append(transaction)
        else:
            print(f"The amount {amount} is higher thane the balance {self.balance}")

    def print_statement(self):
        for transaction in self.transactions:
            print(transaction.__str__())

    def __repr__(self):
        return "Client ({}, {}, {})".format(self.id, self.name, self.balance)