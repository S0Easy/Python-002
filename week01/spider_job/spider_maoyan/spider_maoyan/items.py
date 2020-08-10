# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderMaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    Title = scrapy.Field()
    Type = scrapy.Field()
    Release_Date = scrapy.Field()