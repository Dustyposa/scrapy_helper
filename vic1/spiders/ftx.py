# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from vic1.items import FangTianXiaItem


class FtxSpider(scrapy.Spider):
    name = 'ftx'
    # start_urls = "https://cd.newhouse.fang.com/house/s/piduqu/?ctm=1.cd.xf_search.lpsearch_area.2"
    start_urls = "https://cd.newhouse.fang.com/house/s/doujiangyan1/?ctm=1.cd.xf_search.lpsearch_area.18"

    def start_requests(self):
        yield Request(url=self.start_urls, callback=self.parse_one)

    def parse_one(self, response):
        base = response.css(".nl_con.clearfix li .nlc_details")
        for single in base:
            next_url = single.css(".nlcd_name").xpath("./a/@href").extract_first()
            yield Request(url="https:" + next_url, callback=self.parse_two)

    def parse_two(self, response):
        next_url = response.css("#orginalNaviBox").xpath("./a[2]/@href")
        yield response.follow(next_url[0], callback=self.parse_three)

    def parse_three(self, response):
        item = FangTianXiaItem()
        property_name = response.css("h1 a::text").extract_first()  # 楼盘名
        price = response.css(".main-info-price em::text").extract_first()  # 价格
        property_time = ",".join([i.strip() for i in response.xpath(
            "//div[contains(text(), '产权年限') and @class='list-left']/following-sibling::div//text()").extract()])
        address = response.xpath(
            "//div[contains(text(), '楼盘地址') and @class='list-left']/following-sibling::div/text()").extract_first()

        delivery_time = response.xpath(
            '//*[@class="list clearfix"]/li/div[contains(text(), "交房时间")]/following-sibling::div/text()').extract_first()
        buildings_num = \
            response.xpath(
                '//*[@class="clearfix list"]/li/div[contains(text(), "楼栋总数")]/following-sibling::div/text()').extract_first()
        house_num = response.xpath('//*[@class="clearfix list"]/li/div[contains(text(), "户")]/text()').extract_first()

        item["property_name"] = property_name.strip()
        item["price"] = price.strip()
        item["address"] = address
        item["delivery_time"] = delivery_time
        item["house_num"] = house_num
        item["buildings_num"] = buildings_num
        item["property_time"] = property_time
        item["source"] = self.name
        item["source_url"] = response.url
        yield item
