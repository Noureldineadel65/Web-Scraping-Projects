# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy import Request


class MoviesSpider(CrawlSpider):
    name = 'movies'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/chart/top?ref_=nv_mv_250_6/']

    def parse(self, response):
        movies = response.css("tr")
        for movie in movies:
            rank = movie.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr/td[2]/text()').extract_first()
            ranks = rank.split()
            titles = movie.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr/td[2]/a/text()').extract_first()
            links = movie.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr/td[2]/a/@href').extract()
            for link in links:
                absolutelink = "http://www.imdb.com"+link
                yield Request(absolutelink, callback=self.parse_page)

    def parse_page(self,response):
        RANKS = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[1]/div[1]/div[1]/strong/span/text()').extract_first()
        TITLES = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/h1/text()').extract_first()
        RATINGS = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[1]/div[1]/div[1]/strong/span/text()').extract_first()
        YEARS = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/div/a[2]/text()').extract_first()
        GENRES = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/div/a[1]/text()').extract_first()
        BOXOFFICE = response.xpath('//*[@id="titleDetails"]/div[7]/text()').extract()
        BOXOFFICE ="".join(BOXOFFICE)
        DURATION = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/div/time/text()').extract_first()
        DURATION = DURATION.strip()
        DESCRIPTIONS = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[1]/text()').extract_first()
        ACTORS = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[4]/a/text()').extract()
        if ACTORS:
            ACTORS.pop()
            ACTORS = ",".join(ACTORS)
        else: 
            ACTORS = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div[1]/div[4]/a/text()').extract()
            ACTORS.pop()
            ACTORS = ",".join(ACTORS)
        if DESCRIPTIONS:
            DESCRIPTIONS = DESCRIPTIONS.strip()
        else:
            DESCRIPTIONS = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div[1]/div[1]/text()').extract_first()
            DESCRIPTIONS = DESCRIPTIONS.strip()
        yield {"RANK": RANKS, "TITLE": TITLES, "RATING": RATINGS, "YEAR": YEARS, "GENRE": GENRES, "DESCRIPTION": DESCRIPTIONS, "ACTORS": ACTORS, "DURATION": DURATION, "BOXOFFICE": BOXOFFICE}
        


