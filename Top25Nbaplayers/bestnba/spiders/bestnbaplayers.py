# -*- coding: utf-8 -*-
from scrapy import Spider


class BestnbaplayersSpider(Spider):
    name = 'bestnbaplayers'
    allowed_domains = ['www.ranker.com/crowdranked-list/top-10-current-nba-players']
    start_urls = ['http://www.ranker.com/crowdranked-list/top-10-current-nba-players/']

    def parse(self, response):
        #Get the Rank
        Position  = response.xpath("/html/body/article[@id='list']/div[@class='listItem listItem__h2 listItem__h2--grid listItem__h2--popUp pointer flex relative robotoC']/strong[@class='listItem__rank block center instapaper_ignore']/text()").extract()
        #Get the number of Upvotes
        Upvotes = response.xpath("/html/body/article[@id='list']/div[@class='listItem listItem__h2 listItem__h2--grid listItem__h2--popUp pointer flex relative robotoC']/div[@class='listItem__vote instapaper_ignore']/span[@class='listItem__voteCount listItem__voteCount--up relative float inlineBlock center grey default']/text()").extract()
        #Get the number of DOwnvotes
        Downvotes  = response.xpath("/html/body/article[@id='list']/div[@class='listItem listItem__h2 listItem__h2--grid listItem__h2--popUp pointer flex relative robotoC']/div[@class='listItem__vote instapaper_ignore']/span[@class='listItem__voteCount listItem__voteCount--down relative float inlineBlock center grey default']/text()").extract()
        #Get the name of the player
        Player_name  = response.xpath("/html/body/article[@id='list']/div[@class='listItem listItem__h2 listItem__h2--grid listItem__h2--popUp pointer flex relative robotoC']/div[@class='listItem__data']/a[@class='listItem__title listItem__title--link black']/text()").extract()
        #Gets the team the player is in
        Team  = response.xpath("/html/body/article[@id='list']/div[@class='listItem listItem__h2 listItem__h2--grid listItem__h2--popUp pointer flex relative robotoC']/div[@class='listItem__data']/span[@class='listItem__props block']/span[@class='listItem__properties black default']/text()").extract()
        for (p,u,d,pn,t) in zip(Position, Upvotes, Downvotes, Player_name, Team):
            yield {
                "Rank": p,
                "Upvotes": u,
                "Downvotes": d,
                "Player_name": pn,
                "Team": t
            }
        