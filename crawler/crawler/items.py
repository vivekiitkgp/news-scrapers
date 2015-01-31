# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    headline = scrapy.Field()
    author = scrapy.Field()
    publisher = scrapy.Field()
    summary = scrapy.Field()
    content = scrapy.Field()
    topics = scrapy.Field()
    metadata = scrapy.Field()
    additional = scrapy.Field()
