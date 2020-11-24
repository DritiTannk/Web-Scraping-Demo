import scrapy
import csv


class TagsSpider(scrapy.Spider):
    name = 'tags'

    def start_requests(self):
        with open('tags.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                tag_name = row[1]
                yield scrapy.Request(f'http://quotes.toscrape.com/tag/{tag_name}/page/1/')

    def parse(self, response):
        quotes_list = response.css('div.quote')
        for quote in quotes_list:
            text = quote.css("span.text::text").get()  # Extracts quote
            author = quote.css("small.author::text").get()  # Extracts author
            tags = quote.css("div.tags a.tag::text").getall()  # Extracts tags associated with it
            page_no = response.url.split('/')[-2]  # Extracts page number
            searched_tag = response.url.split('/')[-4]  # Extracts tag name from url for which quotes have been searched
            yield {
                'text': text,
                'author': author,
                'tags': tags,
                'page_no': page_no,
                'searched_tag': searched_tag
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)  # Creates a new url by appending the page number.
            yield scrapy.Request(next_page, callback=self.parse)

