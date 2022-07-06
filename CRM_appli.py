from db_config import Users
import users_def


def command_a():
    new_name = input("New user name > ")
    age = input("New user age > ")
    if new_name in users_l:  # 重複不許可機能
        print(f"Duplicated user name {new_name}")
    else:  # 文字数制限
        if len(new_name) < 1:
            print("User name can't be blank")
        elif 20 < len(new_name):
            print("User name is too long(maximun is 20 characters)")
        else:
            if not age.isdecimal():
                print("Age is not positive integer")
            elif int(age) < 0:
                print("Age can't be blank")
            elif 120 < int(age):
                print("Age is grater than 120")
            else:
                users_def.create_user(new_name, age)
                print(f"Add new user: {new_name}")


def command_f():
    research_name = input("User name > ")
    if research_name in users_l:
        users_def.find_name(research_name)
    else:
        print(f"Sorry, {research_name} is not found")


def command_d():
    delete_name = input("User name > ")
    if delete_name in users_l:
        users_def.delete(delete_name)
    else:
        print(f"Sorry, {delete_name} is not found")


def command_e():
    your_name = input("User name > ")
    if your_name in users_l:
        your_info = Users.get(Users.user_name == your_name)
        edit_name = input(f"New your name ({your_name}) > ")
        edit_age = input(f"New your age ({your_info.user_age}) > ")
        if not edit_age.isdecimal():
            print("Age is not positive integer")
        else:
            users_def.edit(your_name, edit_name, edit_age)
            print(f"Update user: {edit_name}")
    else:
        print(f"Sorry, {your_name} is not found")


if __name__ == "__main__":

    users_l = []  # 追加機能用にユーザー名リスト作成
    for user in Users.select():
        users_l.append(user.user_name)

    print("===== Welcome to CRM Application =====")
    print("[S]how: Show all users info")
    print("[A]dd: Add new user")
    print("[Q]uit: Quit The Application")
    print("[F]ind: Find user")
    print("[D]elete: Delete user")
    print("[E]dit: Edit user")
    print("======================================")

    command = ""
    while command != "Q":
        input_command = input("Your command > ")
        command = input_command.upper()  # 大文字小文字区別なし

        if command in ["S", "A", "F", "D", "E", "Q"]:
            if command == "S":
                users_def.show_all_users()
            if command == "A":
                command_a()
            if command == "F":  # 検索機能
                command_f()
            if command == "D":  # 削除機能
                command_d()
            if command == "E":  # 編集機能
                command_e()
            if command == "Q":
                print("Bye!")
        else:
            print(f"{command.lower()}: command not found")

