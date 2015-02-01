from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from crawler.items import NewsItem

class TheHinduSpider(CrawlSpider):
    """ Spider to crawl the webpage of popular Indian newspaper The Hindu."""

    name = "The Hindu"
    allowed_domains = ['thehindu.com']
    start_urls = ['http://www.thehindu.com']

    rules = (
        Rule(LinkExtractor(deny=('inter.html', 'apps', 'classifieds',
                                 'social', 'shine-jobs', 'in-school',
                                 'videos', 'ebooks')),
             callback='parse_items',
             follow='True',
             process_links='process_links'),
    )

    def parse_items(self, response):
        """ Parse news articles and extract useful information."""

        if response.url.endswith('/'):
            return None

        item = NewsItem()
        item['url'] = response.url
        item['headline'] = response.css('.detail-title::text').extract()
        item['location'] = response.xpath("//span[@class='dateline']/span/text()").extract()
        item['date'] = response.xpath("//span[@class='dateline']/text()").extract()
        item['author'] = response.css('.author::text').extract()
        item['summary'] = response.css('h2::text').extract()
        item['content'] = response.xpath("//div[@class='article-text']/p/text()").extract()
        item['topics'] = response.xpath("//div[@id='articleKeywords']/p/a/text()").extract()
        item['additional'] = response.xpath("//div[@class='article-text']/div[@class='text-embed']/img[@class='main-image']/@src").extract()
        item['publisher'] = 'The Hindu'

        return item
