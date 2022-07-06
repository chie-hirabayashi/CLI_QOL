# from curses import KEY_CREATE
# from asyncio.windows_events import NULL
# from contextlib import nullcontext
# from curses import KEY_NEXT
# from curses.ascii import NUL
# from http.cookiejar import MozillaCookieJar
# from multiprocessing import managers
from db_config import Users
import datetime

# users_data = User(user_name="Bob", user_age=50)
# users_data.save()

# 以下、user_dataで使う関数


def find_name(name):  # 1件のユーザーのNane,Ageを表示(name検索)
    user = Users.get(Users.user_name == name)
    print(f"Name: {user.user_name} Age: {user.user_age}")


def show_all_users():
    for user in Users.select():  # すべてのユーザーのName,Ageを表示
        print(f"Name: {user.user_name} Age: {user.user_age}")


def create_user(name, age):  # 新しいユーザー登録
    Users.create(user_name=name, user_age=age)


def delete(name):  # 1件のユーザーを削除
    user = Users.get(Users.user_name == name)
    user.delete_instance()
    print(f"User {name} is deleted")


def edit(user_name, edit_name, edit_age):  # 1件のユーザー情報を上書き
    user = Users.get(Users.user_name == user_name)
    user.user_name = edit_name
    user.user_age = edit_age
    user.save()


# 以下、users_dataで使わない関数


def display_users():  # すべてのユーザーを表示
    for user in Users.select():
        print(user.id, user.user_name, user.user_age, user.pub_date)


def find_user(id):  # 1件のユーザーを表示
    user = Users.get(Users.id == id)
    print(user.id, user.user_name, user.user_age, user.pub_date)


def delete_user(id):  # 1件のユーザーを削除
    user = Users.get(Users.id == id)
    user.delete_instance()


def delete_user_all():  # すべてのユーザーを削除(無限ループ処理)
    for user in Users.select():
        user.delete_instance()


def updata_user(id, user_name, user_age):  # 1件のユーザー情報を上書き
    user = Users.get(Users.id == id)
    user.user_name = user_name
    user.user_age = user_age
    user.save()


def find_id(id):  # 1件のユーザーのNane,Ageを表示(id検索)
    user = Users.get(Users.id == id)
    print(f"Name: {user.user_name} Age: {user.user_age}")


# 準備
user = Users.get(Users.id == 1)
print(f"Name: {user.user_name} Age: {user.user_age}")
List = [f"{user.user_name}", f"{user.user_age}", f"{user.pub_date}"]
print(List)
print(type(List))
print(List[0])
print(type(List[0]))
print(type(List[1]))

tstr = List[2]
tdatetime = datetime.datetime.strptime(tstr, "%Y-%m-%d %H:%M:%S")
tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)
print(tdate)
print(type(tdate))

oneday = "1900/01/01"
oneday_time1 = datetime.datetime.strptime(oneday, "%Y/%m/%d")
print(oneday_time1)

oneday = "2022-7-1"
oneday_time2 = datetime.datetime.strptime(oneday, "%Y-%m-%d")
print(oneday_time2)

day = oneday_time1 - oneday_time2
print(day.days)
print(type(day.days))

i = 365 / day.days
print(i)

list = []
for user in Users.select():  # すべてのユーザーのName,Ageを表示
    list.append(f"Name: {user.user_name} Age: {user.user_age}")
print(list)




"""
id = 1
user = Users.get(Users.id == id)
print(f"{user.user_name}")
list = [f"{user.user_name}",  f"{user.user_age}"]
# print(f"Name: {user.user_name} Age: {user.user_age}")
"""


if __name__ == "__main__":
    # main()
    show_all_users()

    # id = 1
    # find_id(id)

    # name = "Bob"
    # find_name(name)

    # <すべてのデータを表示>
    # display_users()

    # <新しいユーザー登録を表示>
    # name = "Ken"
    # age = 30
    # create_user(name, age)

    # <1件のユーザー情報を表示>
    # id = 1
    # find_user(id)

    # <複数のユーザーを削除>
    # for id in range(4, 8):
    # id = 8
    # delete_user(id)

    # <すべてのユーザーを削除>
    # delete_user_all()

    # <ユーザー情報の上書き(1)>
    # id = 2
    # user_name = "Tom"
    # user_age = 57
    # updata_user(id, user_name, user_age)

    # <ユーザー情報の上書き(2)>
    # user_name = "Tom"
    # user_age = 99
    # updata(user_name, user_age)
