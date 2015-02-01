# -*- coding: utf-8 -*-

import scrapy

# Helper methods to aid serialization of data.
def trim(content):
    if isinstance(content, basestring):
        return content.strip()
    return map(lambda x: x.strip(), content)

def serialize_content(content):
    return "".join(trim(content))

class NewsItem(scrapy.Item):
    """ News Item object """

    url = scrapy.Field()
    headline = scrapy.Field(serializer=serialize_content)
    date = scrapy.Field(serializer=serialize_content)
    author = scrapy.Field(serializer=serialize_content)
    summary = scrapy.Field(serializer=serialize_content)
    content = scrapy.Field(serializer=serialize_content)
    topics = scrapy.Field(serializer=trim)
    location = scrapy.Field(serializer=serialize_content)
    additional = scrapy.Field()
    publisher = scrapy.Field()
