# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodreadsItem(scrapy.Item):
    # define the fields for your item here like:
    Text = scrapy.Field()
    Author_name = scrapy.Field()
    Tags = scrapy.Field()
    Author_link = scrapy.Field()
    Author_img = scrapy.Field()
    Nbr_likes = scrapy.Field()

