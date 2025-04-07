from typing import List, Dict


def save_to_file(users: List[Dict], filename: str) -> None:
    with open(filename, "w") as file:
        file.write(
                f"{'Id':<5}| {'First Name':<15}| {'Last name':<15}| {'Email':<40}| {'Latitude':<15}| {'Longitude'}\n"
            )
        file.write(
                f"{'-'*110}\n"
            )
        for user in users:
            file.write(
                f"{user['id']:<5}| {user['firstName']:<15}| {user['lastName']:<15}|{user['email']:<40}| {user["address"]["coordinates"]["lat"]:<15}| {user["address"]["coordinates"]["lng"]}\n"
            )
            
        #