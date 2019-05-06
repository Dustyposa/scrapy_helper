# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import pymongo

from vic1.items import LianJiaItem


class MongoSavePipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_host=crawler.settings.get('MONGO_HOST'),
            mongo_port=crawler.settings.get('MONGO_PORT', 27017),
            mongo_col=crawler.settings.get('MONGO_COLLECTION'),
        )

    def process_item(self, item, spider):
        col = self.saver[f'{item["source"]}{datetime.date(datetime.now())}']
        if isinstance(item, LianJiaItem):
            if not col.find_one({"level_two_url": item["level_two_url"]}):
                col.insert_one(dict(item))  # save into database
        else:
            if not col.find_one({"source_url": item["source_url"]}):
                col.insert_one(dict(item))  # save into database
        return item

    def __init__(self, mongo_host, mongo_port, mongo_col):
        self.mongo_host = mongo_host
        self.mongo_port = mongo_port
        self.mongo_col = mongo_col

    def open_spider(self, spider):
        self.cli = pymongo.MongoClient(host=self.mongo_host, port=self.mongo_port)
        self.saver = self.cli[self.mongo_col]

    def close_spider(self, spider):
        self.cli.close()
