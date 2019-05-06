# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Vic1Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LianJiaItem(Item):
    # date = datetime.now()
    # base
    crawl_date = Field()  # 抓取日期
    city = Field()
    area = Field()
    source = Field()

    # level_one
    property_name = Field()  # 楼盘名
    price = Field()  # 在售均价
    sell_set = Field()  # 在售套数
    renting_set = Field()  # 在租套数
    plate_name = Field()  # 板块名
    level_one_page_data = Field()
    level_one_url = Field()
    level_two_url = Field()

    # level_two
    build_time = Field()  # 建筑年代
    buildings_num = Field()  # 楼栋总数
    house_num = Field()  # 房屋总数
    address = Field()  # 地址
    level_two_page_data = Field()


class FangTianXiaItem(Item):
    property_name = Field()  # 楼盘名字
    price = Field()  # 新房单价
    property_time = Field()  # 产权年限
    address = Field()  # 楼盘地址
    delivery_time = Field()  # 交房时间
    house_num = Field()  # 总户数
    buildings_num = Field()  # 楼栋总数
    # base
    crawl_date = Field()  # 抓取日期
    city = Field()
    area = Field()
    source = Field()

    # url
    level_one_url = Field()
    source_url = Field()

    # else data
    source_data = Field()


class XZLItem(Item):
    office_building_name = Field()
    property_level = Field()
    building_time = Field()
    rent_price = Field()
    address = Field()
    rent_way = Field()
    sell_price = Field()
    total_floors = Field()  # 总楼层数
    total_build_area = Field()  # 总楼层数
    standard_floor_area = Field()  # 标准层面积
    property_management_fees = Field()  # 物管费

    # base
    crawl_date = Field()  # 抓取日期
    city = Field()
    area = Field()
    source = Field()

    source_url = Field()

    # else data
    source_data = Field()
