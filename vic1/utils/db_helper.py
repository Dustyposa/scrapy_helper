import pymongo

from configs import (MONGO_PORT,
                     MONGO_HOST,
                     MONGO_DB_NAME)


class MongoHelper:
    def __init__(self, host=MONGO_HOST, port=MONGO_PORT, db_name=MONGO_DB_NAME):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.cli = self.connect_to_mongo()
        self.db_cli = self.cli[MONGO_DB_NAME]

    def __del__(self):
        self.cli.close()

    def connect_to_mongo(self):
        try:
            mongo_cli = pymongo.MongoClient(host=self.host, port=self.port)
        except Exception as e:
            raise EOFError(f"连接数据库失败:{e.args}")
        return mongo_cli
