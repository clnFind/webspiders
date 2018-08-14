# -*- coding: utf-8 -*-
import datetime

import scrapy

from constant import ARCHIVE
from constant import NUMERIC
from constant import DATAS
from constant import ELEC_FILE
from constant import FILES
from webspiders.items import JsWebspidersItem


class JsSpider(scrapy.spiders.Spider):
    """
    爬取江苏政府网的关于档案类的采购公告信息
    """
    name = "jsweb"
    allowed_domains = ['www.ccgp-jiangsu.gov.cn']
    start_urls = [
     'http://www.ccgp-jiangsu.gov.cn/cgxx/cggg/index.html',
     'http://www.ccgp-jiangsu.gov.cn/cgxx/cggg/index_1.html',
     'http://www.ccgp-jiangsu.gov.cn/cgxx/cggg/index_2.html',
     'http://www.ccgp-jiangsu.gov.cn/cgxx/cggg/index_3.html',
     'http://www.ccgp-jiangsu.gov.cn/cgxx/cggg/index_4.html',
     'http://www.ccgp-jiangsu.gov.cn/cgxx/cggg/index_5.html',
     'http://www.ccgp-jiangsu.gov.cn/cgxx/cggg/index_6.html',

    ]

    def parse(self, response):

        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        url = "http://www.ccgp-jiangsu.gov.cn/cgxx/cggg"

        for sel in response.xpath('//div[@id="newsList"]/ul/li'):
            item = JsWebspidersItem()
            date_today = datetime.datetime.now().strftime('%Y-%m-%d')
            dates = sel.xpath('text()').re('\S+')[0]

            pattern = '\S+{archive}\S+|\S+{numeric}\S+|\S+{files}\S+|\S+{datas}\S+|\S+{elec_file}\S+'.format(
                archive=ARCHIVE, numeric=NUMERIC, files=FILES, datas=DATAS, elec_file=ELEC_FILE
            )

            contents = sel.xpath('a/text()').re(pattern)

            if dates == date_today and contents:
                print("######################_____  ", contents)
                item['dates'] = dates
                item['title'] = contents[0]
                item['link'] = url + sel.xpath('a/@href').extract()[0][1:]

                print("$$$$$$$$$______ links:  ", item['link'], type(item['link']))
                # print(title, link)
                yield item
