# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FedreserveItem(scrapy.Item):
    # define the fields for your item here like:
    Country = scrapy.Field()
    Monetary_Unit = scrapy.Field()
    Date = scrapy.Field()
    Rate = scrapy.Field()
