class Bank:
    def __init__(self):
        self.clients = []
    
    def add_client(self, client):
        self.clients.append(client)
    
    def remove(self,client_id):
        self.clients = [client for client in self.clients
                       if client.id != client_id]

    def get_client(self, client_id):
        for client in self.clients:
            if client.id == client_id:
                return client
        return None

    def print_balance(self):
        for client in self.clients:
            print(f"{client.name}:{client.balance}")

    def __repr__(self):
        return f"Bank(Clients:{self.clients})"
