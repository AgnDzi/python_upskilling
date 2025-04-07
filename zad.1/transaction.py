from datetime import datetime 

# class Transaction:
#     def __init__(self, client_id, client_name, transaction_type, transaction_amount):
#         self.client_id = client_id
#         self.client_name = client_name
#         self.transaction_type = transaction_type
#         self.transaction_amount = transaction_amount
#         self.trancaction_date = datetime.now()

#     def __repr__(self):
#         return "Transaction({}, {}, {}, {}, {})".format(self.client_id, self.client_name, self.transaction_type, self.transaction_amount, self.trancaction_date)


#     def __str__(self):
#         return "Client: {}, name: {}, type: {}, amount: {}, date: {}".format(self.client_id, self.client_name, self.transaction_type, self.transaction_amount, self.trancaction_date)

from dataclasses import dataclass
from trans_enum import TransType

@dataclass
class Transaction:
  client_id: str 
  client_name: str
  transaction_type: TransType
  transaction_amount: float
  transaction_date: datetime.now()

def __str__(self):
         return "Client: {}, name: {}, type: {}, amount: {}, date: {}".format(self.client_id, self.client_name, self.transaction_type, self.transaction_amount, self.trancaction_date)
