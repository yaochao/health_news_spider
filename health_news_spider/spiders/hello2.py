# -*- coding: utf-8 -*-
import scrapy


class Hello2Spider(scrapy.Spider):
    name = 'hello2'
    allowed_domains = ['hello2.com']
    start_urls = ['http://hello2.com/']

    def parse(self, response):
        pass
