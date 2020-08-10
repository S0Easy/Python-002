# -*- coding: utf-8 -*-
import scrapy
from spider_maoyan.items import SpiderMaoyanItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass
    # def start_requests(self):
    #     url = 'https://maoyan.com/films?showType=3'
    #     yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        item = SpiderMaoyanItem()  
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')[:10]
        for movie in movies:
            Title = movie.xpath('./div[1]/span[1]/text()').get()
            Type = movie.xpath('./div[2]/text()')[-1].get().strip()
            Release_Date = movie.xpath('./div[4]/text()')[-1].get().strip()
            print("&"*100,  Title)
            print("*"*100,  Type)
            print("^"*100,  Release_Date)
            item["Title"] = Title
            item["Type"] = Type
            item["Release_Date"] = Release_Date
            yield item

            



