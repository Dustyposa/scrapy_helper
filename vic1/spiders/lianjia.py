# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from vic1.settings import CITY_AREAS_LIST
from vic1.items import LianJiaItem


class LjSpider(scrapy.Spider):
    name = 'lianjia'
    start_urls = 'https://cd.lianjia.com/xiaoqu/'
    page = 1
    flag = True
    # base_url = start_urls + CITY_AREAS_LIST[3] + "/pg{}"
    base_url = start_urls + "doujiangyan" + "/pg{}"

    def start_requests(self):

        yield Request(url=self.base_url.format(self.page), callback=self.parse_one)

    def parse_one(self, response):
        if self.flag:
            group_xpath = response.css(".clear.xiaoquListItem")
            if not group_xpath:
                self.flag = False
                yield
            for single in group_xpath:
                item = LianJiaItem()

                property_name = single.css(".info>.title>a::text").extract_first()  # 楼盘名称
                renting_set = single.css(".info>.houseInfo").xpath("./a[last()]/text()").extract_first()  # 在租套数
                price = single.css(".xiaoquListItemPrice>.totalPrice>span::text").extract_first()  # 在售均价
                sell_set = single.css(".xiaoquListItemSellCount>a>span::text").extract_first()  # 在售套数
                plate_name = " ".join(single.css(".positionInfo>a::text").extract())  # 板块名
                level_two_url = single.css(".info .title").xpath("./a/@href").extract_first()  # 板块名
                item["property_name"] = property_name
                item["renting_set"] = renting_set
                item["price"] = price
                item["sell_set"] = sell_set
                item["plate_name"] = plate_name
                item["level_two_url"] = level_two_url

                yield Request(level_two_url, callback=self.parse_detail, meta={"item": item})

            self.page += 1
            yield Request(url=self.base_url.format(self.page), callback=self.parse_one)
            # response.css(".clear.xiaoquListItem").css(".info .title").xpath("./a/@href").extract_first()

    def parse_detail(self, response):
        item = response.meta["item"]

        build_time = response.xpath('//span[contains(text(), "建筑年代")]/following-sibling::span/text()').extract_first()
        buildings_num = response.xpath('//span[contains(text(), "楼栋总数")]/following-sibling::span/text()').extract_first()  # 楼栋总数
        house_num = response.xpath('//span[contains(text(), "房屋总数")]/following-sibling::span/text()').extract_first()  # 房屋总数
        adress = response.css(".detailDesc::text").extract_first()  # 地址
        item["build_time"] = build_time
        item["buildings_num"] = buildings_num
        item["house_num"] = house_num
        item["address"] = adress
        item["source"] = self.name
        yield item

