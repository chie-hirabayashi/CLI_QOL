"""
データベースへの接続までの流れ
・osインポート
・環境変数PWDの読み込み(このパターンでは？？必須。PWDの働きは不明)
・.envを作成し、.gitignoreに登録(このバターンでは必須。.env内のURLに接続するため。公開しない情報はここに入れる)
・$poetry add python-dotenv
  dotenvをインストール(このパターンでは必須。.envの情報を伝達？？)
・$touch peewee_db.sqlite
  peeweeパッケージをインストール(必須。peeweeを利用してデータベースに接続する)
・envを呼び出してデータベースに接続
"""


import os
from dotenv import load_dotenv


print(os.environ.get("PWD"))  # 環境変数PWDの読み込み

load_dotenv()

print(os.environ["secret"])
