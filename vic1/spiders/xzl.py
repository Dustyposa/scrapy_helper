# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from vic1.items import FangTianXiaItem, XZLItem


class XzlSpider(scrapy.Spider):
    name = 'xzl'
    start_url = "http://info.028office.com/building/{}/"
    areas = ["pixian"]

    def start_requests(self):
        for area in self.areas:
            yield Request(url=self.start_url.format(area), callback=self.parse_one, meta={"area": area})

    def parse_one(self, response):
        base = response.css(".c .p>a")
        for single in base:
            yield response.follow(single, callback=self.parse_three, meta={"area": response.meta["area"]})
        href = response.xpath('//a[contains(text(),"下一页")]/@href')
        if href:
            yield response.follow(href[0], callback=self.parse_one, meta={"area": response.meta["area"]})

    def parse_three(self, response):
        print(response.url)
        item = XZLItem()
        office_building_name = response.css("li.t h1::text").extract_first()  # 楼盘名
        rent_way = response.xpath(
            "//td/b[contains(text(),'租售形式')]/parent::td/following-sibling::td/text()").extract_first()
        property_level = response.xpath(
            "//td/b[contains(text(),'物业级别')]/parent::td/following-sibling::td/text()").extract_first()
        rent_price = response.xpath(
            "//td/b[contains(text(),'参考租金')]/parent::td/following-sibling::td//text()").extract_first()
        sell_price = response.xpath(
            "//td/b[contains(text(),'参考售价')]/parent::td/following-sibling::td/text()").extract_first()
        building_time = response.xpath(
            "//td/b[contains(text(),'建成时间')]/parent::td/following-sibling::td/text()").extract_first()
        total_floors = response.xpath(
            "//td/b[contains(text(),'总楼层数')]/parent::td/following-sibling::td/text()").extract_first()
        total_build_area = response.xpath(
            "//td/b[contains(text(),'总建筑面积')]/parent::td/following-sibling::td/text()").extract_first()
        standard_floor_area = response.xpath(
            "//td/b[contains(text(),'标准层面积')]/parent::td/following-sibling::td/text()").extract_first()
        property_management_fees = response.xpath(
            "//td/b[contains(text(),'物管费')]/parent::td/following-sibling::td/text()").extract_first()
        address = response.css("#mainaddress li").xpath("./text()").extract_first()

        item["office_building_name"] = office_building_name
        item["rent_way"] = rent_way
        item["property_level"] = property_level
        item["rent_price"] = rent_price
        item["sell_price"] = sell_price
        item["building_time"] = building_time
        item["address"] = address
        item["total_floors"] = total_floors
        item["standard_floor_area"] = standard_floor_area
        item["property_management_fees"] = property_management_fees
        item["total_build_area"] = total_build_area

        item["area"] = response.meta["area"]
        item["source"] = self.name
        item["source_url"] = response.url

        yield item

