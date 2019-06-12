# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy import Request


class JobsSpider(CrawlSpider):
    name = 'jobs'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://newyork.craigslist.org/search/egr/']

    def parse(self, response):
        jobs = response.css(".result-info")
        for job in jobs:
            Dates = response.css(".result-date::text").extract_first()
            Titles = job.css('.hdrlnk::text').extract_first()
            address = job.css(".result-hood::text").extract_first()
            relative_url = job.css(".hdrlnk::attr('href')").extract_first()
            yield Request(relative_url, callback=self.parse_page, meta={'URL': relative_url, 'Dates':Dates, 'Title': Titles, 'Address':address})


        url = response.xpath('//*[@id="searchform"]/div[5]/div[3]/span[2]/a[3]/@href').extract_first()
        absurl = response.urljoin(url)
        if url:

            yield Request(url=absurl, callback=self.parse)
        else:
            print("No next page found")

    def parse_page(self,response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        address = response.meta.get('Address')
        description = "".join(line for line in response.xpath('//*[@id="postingbody"]/text()').extract())
        description = description.strip()
        compensation = response.xpath('//p[@class="attrgroup"]/span[1]/b/text()').extract_first()
        employment_type = response.xpath('//p[@class="attrgroup"]/span[2]/b/text()').extract_first()

        yield{'URL': url, 'Title': title, 'Address':address, 'Description':description, 'Compensation':compensation, 'Employment Type':employment_type}
 
