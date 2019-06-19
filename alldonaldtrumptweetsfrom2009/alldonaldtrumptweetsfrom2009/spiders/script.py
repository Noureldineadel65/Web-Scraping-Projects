from scrapy import Spider
import json

class Tweets(Spider):
    name = 'tweets'
    allowed_domains = ['www.trumptwitterarchive.com']
    start_urls = ['http://www.trumptwitterarchive.com/data/realdonaldtrump/2009.json',
    'http://www.trumptwitterarchive.com/data/realdonaldtrump/2010.json',
    'http://www.trumptwitterarchive.com/data/realdonaldtrump/2011.json',
    'http://www.trumptwitterarchive.com/data/realdonaldtrump/2012.json',
    'http://www.trumptwitterarchive.com/data/realdonaldtrump/2013.json',
    'http://www.trumptwitterarchive.com/data/realdonaldtrump/2014.json',
    'http://www.trumptwitterarchive.com/data/realdonaldtrump/2015.json',
    'http://www.trumptwitterarchive.com/data/realdonaldtrump/2016.json',
    'http://www.trumptwitterarchive.com/data/realdonaldtrump/2017.json',
    'http://www.trumptwitterarchive.com/data/realdonaldtrump/2018.json',
    'http://www.trumptwitterarchive.com/data/realdonaldtrump/2019.json']

    def parse(self, response):
        jsonresponse = json.loads(response.body)
        for tweet in jsonresponse:
            yield {
            "text": tweet['text'],
            "created_at": tweet['created_at'],
            "retweet_count": tweet['retweet_count'],
            "in_reply_to_user_id_str": tweet['in_reply_to_user_id_str'],
            "favorite_count": tweet['favorite_count'],
            "is_retweet": tweet['is_retweet']
            }