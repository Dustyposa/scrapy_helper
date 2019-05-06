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
            next_url = single.css(".nlcd_name").xpath("./a/@href").extract_first()

            yield Request(url=next_url, callback=self.parse_two)

    def parse_two(self, response):
        next_url = response.css("#orginalNaviBox").xpath("./a[2]/@href")
        yield response.follow(next_url, callback=self.parse_three)

    def parse_three(self, response):
        item = FangTianXiaItem()
        property_name = response.css("h1 a::text").extract_first()  # 楼盘名
        price = response.css(".main-info-price em::text").re(r"\d+")  # 价格
        item["property_name"] = property_name.strip()
        item["price"] = price
        item["source"] = self.name
        item["source_url"] = response.url
        yield item
