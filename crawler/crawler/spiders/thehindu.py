import scrapy

class TheHinduSpider(scrapy.Spider):
    name = "The Hindu"
    allowed_domains = ['thehindu.com']
    start_urls = [ 'http://thehindu.com' ]

    def parse(self, response):

