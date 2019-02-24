# -*- coding: utf-8 -*-
import scrapy


class FtxSpider(scrapy.Spider):
    name = 'ftx'
    allowed_domains = ['ftx.com']
    start_urls = ['http://ftx.com/']

    def parse(self, response):
        pass
