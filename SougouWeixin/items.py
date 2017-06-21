# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SougouweixinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    content=scrapy.Field()
    content_url=scrapy.Field()
    account=scrapy.Field()
    account_url=scrapy.Field()
    publish_time=scrapy.Field()
    crawl_time=scrapy.Field()
class Sougouaccount(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()


    rich_media_title=scrapy.Field()




