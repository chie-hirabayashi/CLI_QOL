# from collections import UserString
# from db_config import Users
import users_def

print("===== Welcome to CRM Application =====")
print("[S]how: Show all users info")
print("[A]dd: Add new user")
print("[Q]uit: Quit The Application")
print("======================================")

command = input("Yor command > ")
if command == "S":
    users_def.show_all_users()
elif command == "A":
    name = input("New user name > ")
    age = input("New user age > ")
    users_def.create_user(name, age)
    print(f"Add new user: {name}")
elif command == "Q":
    print("Bye!")
else:
    print(f"{command}: command not found")
