# from collections import UserString
from db_config import Users
import users_def

print("===== Welcome to CRM Application =====")
print("[S]how: Show all users info")
print("[A]dd: Add new user")
print("[Q]uit: Quit The Application")
print("======================================")
users_l = []
for user in Users.select(): 
    users_l.append(user.user_name)

command = input("Your command > ")
if command == "S":
    users_def.show_all_users()

elif command == "A":
    new_name = input("New user name > ")
    age = input("New user age > ")
    if new_name in users_l:  # 重複不許可機能
        print(f"Duplicated user name {new_name}")
    else:
        users_def.create_user(new_name, age)
        print(f"Add new user: {new_name}")


elif command == "F":  # 検索機能
    research_name = input("User name > ")
    if research_name in users_l:
        users_def.find_name(research_name)
    else:
        print(f"Sorry, {research_name} is not found")

elif command == "D":  # 削除機能
    delete_name = input("User name > ")
    if delete_name in users_l:
        users_def.delete(delete_name)
    else:
        print(f"So, {delete_name} is not found")

elif command == "Q":
    print("Bye!")

else:
    print(f"{command.lower()}: command not found")
