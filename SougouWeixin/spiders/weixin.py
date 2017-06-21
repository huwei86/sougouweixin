# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from SougouWeixin.items import SougouweixinItem
from SougouWeixin.items import Sougouaccount
from datetime import datetime
from SougouWeixin.settings import DATETIME_FORMAT
class WeixinSpider(scrapy.Spider):
    name = 'weixin'
    allowed_domains = ['sogou.com']
    
    def start_requests(self):

        for i in range(1,50):
            url = "http://weixin.sogou.com/pcindex/pc/pc_0/{}.html".format(i)
            yield scrapy.Request(url,callback=self.parse_item)




    def parse_item(self, response):
        lis=response.xpath('//div[@class="txt-box"]')
        for each in lis:
            item = SougouweixinItem()
            item["title"] = each.xpath('h3/a/text()').extract()[0]
            item["content"] = each.xpath('p/text()').extract()[0]
            content_url = each.xpath('h3/a/@href').extract()[0]
            if content_url:
                item["content_url"]=content_url
                
            item["account"]= each.xpath('div[@class="s-p"]/a/text()').extract()[0]
            account_url= each.xpath('div[@class="s-p"]/a/@href').extract()[0]

            if account_url:
                item["account_url"] = account_url

            else:
                item["account_url"]= ""
            publish_time=each.xpath('//div[@class="s-p"]/span/@t').extract()[0]
            item["publish_time"]=datetime.fromtimestamp(int(publish_time)).strftime(DATETIME_FORMAT)
            item["crawl_time"] = datetime.now()
            yield item



    
