import scrapy
from wikipedia.items import wikipediaItem

class mySpider(scrapy.Spider):
    name = "myspider"
	
	
	start_urls = [
		'https://en.wikipedia.org/wiki/Godzilla',
	]
		
	
    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'wikipedia-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)