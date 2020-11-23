import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        quotes_list = response.css('div.quote')
        for quote in quotes_list:
            text = quote.css("span.text::text").get()  # Extracts quote
            author = quote.css("small.author::text").get()  # Extracts author
            tags = quote.css("div.tags a.tag").getall()  # Extracts tags associated with it
            page_no = response.url.split('/')[-2]
            yield {
                'text': text,
                'author': author,
                'tags': tags,
                'page_no': page_no
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)  # Creates a new url by appending the page number.
            yield scrapy.Request(next_page, callback=self.parse)

