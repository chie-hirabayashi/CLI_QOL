from db_config import Users

# users_data = User(user_name="Bob", user_age=50)
# users_data.save()


def create_user(name, age):  # 新しいユーザー登録
    Users.create(user_name=name, user_age=age)


def display_users():  # すべてのユーザーを表示
    for user in Users.select():
        print(user.id, user.user_name, user.user_age, user.pub_date)


def find_user(id):  # 1件のユーザーを表示
    user = Users.get(Users.id == id)
    print(user.id, user.user_name, user.user_age, user.pub_date)


def delete_user(id):  # 1件のユーザーを削除
    user = Users.get(Users.id == id)
    user.delete_instance()


def update_user(id, user_name, user_age):
    user = Users.get(Users.id == id)
    user.user_name = user_name
    user.user_age = user_age
    user.save()


if __name__ == "__main__":
    # main()

    # <すべてのデータを表示>
    display_users()

    # <新しいユーザー登録を表示>
    # name = "Ken"
    # age = 73
    # create_user(name, age)

    # <1件のユーザー情報を表示>
    # id = 1
    # find_user(id)

    # <1件のユーザーを削除>
    # id = 3
    # delete_user(id)

    # <1権のユーザー情報を上書き>
    # id = 2
    # user_name = "Tom"
    # user_age = 57
    # update_user(id, user_name, user_age)
