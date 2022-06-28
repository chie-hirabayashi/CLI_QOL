
import os
import datetime
import logging
from dotenv import load_dotenv
from playhouse.db_url import connect
from peewee import Model, IntegerField, CharField, TimestampField

# CharFild : よく分からない。name
# IntegerField : age, TextField : name, TimestampField : 作成日時。デフォルトとして入れた方がいい

load_dotenv()  # .env読み込み(.env内にあるデータベースのURLを参照するため？)

# SQLのログ出力設定
logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


# データベースに接続
db = connect(os.environ.get("DATABASE"))  # 環境変数？？？

# 接続NGの場合、メッセージ表示
if not db.connect():
    print("接続できませんでした")
    exit()

# フィールド設定
# Model : テーブルのこと。エクセルで言うsheet


class Users(Model):
    """User Model"""

    id = IntegerField(primary_key=True)  # idが自動で追加される
    user_name = CharField()
    user_age = IntegerField()
    pub_date = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = db
        table_name = "users_data"


db.create_tables([Users])
