from get_users_batch import get_all_users
from save_file import save_to_file
from db import save_to_db, get_user


def main():
    users = get_all_users(50)
    save_to_file(users, "users.txt")
    save_to_db(users)
    user_from_db = get_user(1)
    print(user_from_db)

if __name__ == "__main__":
    main()
