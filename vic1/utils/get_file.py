import csv

from db_helper import MongoHelper


class SomeConfigs:
    LIANJIA_FIELDS = {"property_name": "楼盘名字", "price": "二手房单价", "sell_set": "在售二手房套数",
                      "renting_set": "在租套数", "plate_name": "所属板块名", "build_time": "建筑年代",
                      "buildings_num": "楼栋总数", "house_num": "房屋总数(户)", "address": "地址", "level_two_url": "原始地址"}
    CDXZL_FIELDS = {"office_building_name": "写字楼名字", "property_level": "物业等级", "area": "地区",
                    "property_management_fees": "物管费", "rent_way": "租售形式", "building_time": "建筑年代",
                    "sell_price": "出售价格", "standard_floor_area": "标准层面积", "address": "地址", "source_url": "原始地址",
                    "total_build_area": "总建筑面积", "total_floors": "总层数"}
    FANGTIANXIA_FIELDS = {"property_name": "楼盘名字", "price": "新房单价",
                          "delivery_time": "交房时间",
                          "buildings_num": "楼栋总数", "house_num": "房屋总数(户)", "address": "地址", "source_url": "原始地址",
                          "property_time": "产权年限"}

    HOURSE_NAME = {"xzl": CDXZL_FIELDS, "lianjia": LIANJIA_FIELDS, "ftx": FANGTIANXIA_FIELDS}


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
    c_name = "ftx"

    data = mon.db_cli[c_name].find()
    file_name = f"{c_name}.csv"
    with open(file_name, "w", newline="", encoding="utf_8_sig") as f:
        field = SomeConfigs.HOURSE_NAME[c_name]
        writer = csv.DictWriter(f, field.values())
        writer.writeheader()
        for i in data:
            writer.writerow({field[k]: i[k] for k in field})

    print("写入csv成功")
