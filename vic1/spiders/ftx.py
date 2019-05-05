# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from vic1.items import FangTianXiaItem


class FtxSpider(scrapy.Spider):
    name = 'ftx'
    start_urls = "https://cd.newhouse.fang.com/house/s/qingyang/?ctm=1.cd.xf_search.lpsearch_area.2"

    def start_requests(self):
        yield Request(url=self.start_urls, callback=self.parse_one)

    def parse_one(self, response):
        base = response.css(".nl_con.clearfix li .nlc_details")
        for single in base:
            item = FangTianXiaItem()
            property_name = single.css(".nlcd_name a::text").extract_first()  # 楼盘名
            price = single.css(".nhouse_price span::text").extract_first()
            print(property_name, "pro")
            item["property_name"] = property_name.strip()
            item["price"] = price
            item["source"] = self.name
            item["source_url"] = response.url
            yield item
