# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html




class QuotesSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').scrapy.Field()
            author = quote.xpath('.//*[@itemprop="author"]/text()').scrapy.Field()
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').scrapy.Field()
