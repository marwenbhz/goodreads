# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from goodreads.items import GoodreadsItem


class GoodreadsspiderSpider(scrapy.Spider):
    name = 'goodreadsspider'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/quotes?page=1']
    #custom_settings = {
    #'LOG_FILE': 'logs/goodreads.log',
    #'LOG_LEVEL':'ERROR'
    # }


    def parse(self, response):
        print('PROCESSING...' + response.url)

	quotes = response.css('div.quote')
	for quote in quotes:

	    item = GoodreadsItem()

	    try:
		item['Text'] = quote.css('div.quoteText::text').extract_first().replace(";", " ")
	    except:
		print('ERROR TEXT PARSE...' + response.url)
	    try:
		item['Author_name'] = quote.css('span.authorOrTitle::text').extract_first().strip()
	    except:
		print('ERROR AUTHOR NAME PARSE...' + response.url)
	    try:
		item['Tags'] = quote.css('div.greyText > a::text').extract()
	    except:
		print('ERROR TAGS PARSE...' + response.url)
	    try:
		item['Author_link'] = response.urljoin(quote.css('a.leftAlignedImage::attr(href)').extract_first())
	    except:
		print('ERRO AUTHOR LINK PARSE...' + response.url)
	    try:
		item['Author_img'] = quote.css('a.leftAlignedImage > img::attr(src)').extract_first()
	    except:
		print('ERROR AUTHOR IMG PARSE...' + response.url)
	    try:
		item['Nbr_likes'] = quote.css('a.smallText::text').extract_first()
	    except:
		print('ERRO NBR LIKES PARSE...' + response.url)

	    yield item

	relative_next_url = response.css('a.next_page::attr(href)').extract_first()
	if relative_next_url is not None:
	    absolute_next_url = response.urljoin(relative_next_url)
	    yield Request(absolute_next_url, callback=self.parse)
