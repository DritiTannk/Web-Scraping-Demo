import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        quotes_list = response.css('div.quote')
        for quote in quotes_list:
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag").getall()
            page_no = response.url.split('/')[-2]
            yield {
                'text': text,
                'author': author,
                'tags': tags,
                'page_no': page_no,
            }

