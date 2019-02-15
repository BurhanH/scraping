# code/spider.py
import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blog_spider'
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)

# how to run
# scrapy runspider spider.py
