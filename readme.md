*__*This project will demonstrate how to scrape the website using python's scrapy framework.** 

##### 1. Create Scrapy Project 

`` scrapy startproject project_name ``

##### 2. Create a your spider python file inside the spider directory.

##### 3. Run your Spider File

`` scrapy crawl spider-name `` 

##### 4. To store the scraped data result

`` scrapy crawl spider-name -O quotes.json ``

> Note:
> "-O" - will overwrite the existing output file while "-o" will append the data.

#### Attributes and methods of the spider class:

-  name: It identifies the Spider and must be unique within a project.

- start_requests(): It must return an iterable of Requests (you can return a list of requests or write a generator function) which the Spider will begin to crawl from. Subsequent requests will be generated successively from these initial requests.

- parse(): A method that will be called to handle the response downloaded for each of the requests made. The response parameter is an instance of TextResponse that holds the page content and has further helpful methods to handle it.
The parse() method usually parses the response, extracting the scraped data as dicts and also finding new URLs to follow and creating new requests (Request) from them