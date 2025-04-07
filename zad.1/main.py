from client import Client
from bank import Bank

def main():
    try:    
        bank = Bank()
        client1 = Client("Aga", 2000)
        client2 = Client("Adam", 3000)

        bank.add_client(client1)
        bank.add_client(client2)

        client1.depositing(200)
        client1.withdrawing(500)
        client2.depositing(100)
        client2.withdrawing(2000)

        print(bank.__repr__())

        client1.print_statement()
        client2.print_statement()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
