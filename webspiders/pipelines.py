# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class WebspidersPipeline(object):

    def __init__(self):
        self.file = open('spider_result.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):

        # if spider.name == 'jsweb':
        #     line = json.dumps(dict(item)) + '\n'
        #     self.file.write(line)
        # elif spider.name == 'zjweb':

        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item
