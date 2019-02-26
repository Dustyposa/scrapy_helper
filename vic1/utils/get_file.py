import csv

from db_helper import MongoHelper


class SomeConfigs:
    LIANJIA_FIELDS = {"property_name": "楼盘名字", "price": "二手房单价", "sell_set": "在售二手房套数",
                      "renting_set": "在租套数", "plate_name": "所属板块名", "build_time": "建筑年代",
                      "buildings_num": "楼栋总数", "house_num": "房屋总数(户)", "address": "地址", "level_two_url": "原始地址"}
    CDXZL_FIELDS = {}
    FANGTIANXIA_FIELDS = {}

    HOURSE_NAME = "lianjia"


class FileHelper:
    def __init__(self):
        ...

    def __del__(self):
        ...

    def __repr__(self):
        ...

    def save_all_data_to_csv(self, file_name):
        ...

    def insert_into_csv(self, file_name):
        ...


if __name__ == '__main__':
    mon = MongoHelper()
    fler = FileHelper()
    data = mon.db_cli[SomeConfigs.HOURSE_NAME].find()
    file_name = f"{SomeConfigs.HOURSE_NAME}.csv"
    with open(file_name, "w", newline="", encoding="utf_8_sig") as f:
        writer = csv.DictWriter(f, SomeConfigs.LIANJIA_FIELDS.values())
        writer.writeheader()
        for i in data:
            writer.writerow({SomeConfigs.LIANJIA_FIELDS[k]: i[k] for k in SomeConfigs.LIANJIA_FIELDS})

    print("写入csv成功")
