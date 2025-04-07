from typing import List, Dict
import requests


def get_all_users(batch_size: int) -> List[Dict[str, any]]:
    api_url = "https://dummyjson.com/users"
    users = []
    skip = 0
    payload = {"limit": batch_size, "skip": skip}

    while True:
        response = requests.get(api_url, params=payload)
        users_data = response.json() #wypakowanie

        
        if len(users_data["users"]) == 0:   
            break

        users.extend(users_data["users"]) 
        skip += batch_size
        payload = {"limit": batch_size, "skip": skip}

    return users
