# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class SougouweixinPipeline(object):
    def process_item(self, item, spider):
        con = pymysql.connect(host="127.0.0.1", user="root", passwd="229801", db="weixin", charset="utf8")
        cur = con.cursor()
        sql = (
        "insert into souguoweixin(title,content,content_url,account,account_url,publish_time,crawl_time)"
        "VALUES (%s,%s,%s,%s,%s,%s,%s)")
        lis = (item["title"], item["content"], item["content_url"], item["account"], item["account_url"],item["publish_time"],item["crawl_time"])
        cur.execute(sql, lis)
        con.commit()
        cur.close()
        con.close()

        return item
# class SougouaccountPipeline(object):
#     def process_item(self, item, spider):
#         con = pymysql.connect(host="127.0.0.1", user="root", passwd="229801", db="weixin", charset="utf8")
#         cur = con.cursor()
#         sql = (
#         "insert into account(nickname,account,desc_value,label,title,publish_time,crawl_time)"
#         "VALUES (%s,%s,%s,%s,%s,%s,%s)")
#         lis = (item["nickname"], item["account"], item["desc_value"], item["label"], item["title"],item["publish_time"],item["crawl_time"])
#         cur.execute(sql, lis)
#         con.commit()
#         cur.close()
#         con.close()
#
#         return item