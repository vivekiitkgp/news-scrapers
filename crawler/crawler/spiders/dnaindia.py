from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from crawler.items import NewsItem

class TheHinduSpider(CrawlSpider):
    """ Spider to crawl the webpage of popular e-paper DNA India."""

    name = "DNA India"
    allowed_domains = ['dnaindia.com']
    start_urls = ['http://www.dnaindia.com']

    rules = (
        Rule(LinkExtractor(deny=('gallery', 'film-reviews', 'games',
                                 'analysis', 'entertainment', 'cartoon',
                                 'videos', 'lifestyle', 'contact', 'careers')),
             callback='parse_items',
             follow='True',
             process_links='process_links'),
    )

    def parse_items(self, response):
        """ Parse news articles and extract useful information."""

        item = NewsItem()
        item['headline'] = response.css('.pageheading::text').extract()

        # Early return in case bogus hits are obtained
        if response.url.endswith('/') and not item['headline']:
            return None

        # TODO: Regex to avoid try-except block
        try:
            publine = response.css('.pubdate::text').extract()[0].split('|')
            item['location'] = publine[1].replace('Place:', '')
            item['date'] = publine[0]
            item['author'] = publine[2].replace('Agency:', '')
        except IndexError:
            return None

        item['url'] = response.url
        item['summary'] = response.css('.slug::text').extract()
        item['content'] = response.xpath("//div[@class='content-story']/p/text()").extract()
        item['topics'] = response.xpath("//div[@class='story-tags']/a/text()").extract()
        item['publisher'] = u'DNA India'

        return item
