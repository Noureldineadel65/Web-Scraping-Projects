# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BestnbaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Position = scrapy.Field()
    Upvotes = scrapy.Field()
    Downvotes = scrapy.Field()
    Player_name = scrapy.Field()
    Team = scrapy.Field()

