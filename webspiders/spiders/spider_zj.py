# -*- coding: utf-8 -*-
import datetime
import json

import scrapy

from constant import ARCHIVE
from constant import NUMERIC
from constant import DATAS
from constant import ELEC_FILE
from constant import FILES
from webspiders.items import ZjWebspidersItem
from webspiders.utils import timestamp_eq_time


class ZjSpider(scrapy.spiders.Spider):
    """
    爬取浙江政府网关于档案类的采购公告信息
    """
    name = "zjweb"
    allowed_domains = ['www.zjzfcg.gov.cn']

    url = 'http://manager.zjzfcg.gov.cn/cms/api/cors/getRemoteResults?pageSize=15&pageNo={page}&' \
          'noticeType=0&url=http%3A%2F%2Fnotice.zcy.gov.cn%2Fnew%2FnoticeSearch'
    start_urls = []

    # 只爬取前20页的数据
    for i in range(1, 21):
        start_urls.append(url.format(page=i))


    # def start_requests(self):
    #     url = "http://www.zjzfcg.gov.cn/purchaseNotice/index.html"
    #     requests = []
    #     for i in range(1, 15):
    #         formdata = {
    #             "typeid": "18",
    #             "page": str(i),
    #         }
    #         request = FormRequest(url, callback=self.parse, formdata=formdata)
    #         requests.append(request)
    #     return requests

    def parse(self, response):

        datas = json.loads(response.text)['articles']
        date_today = datetime.datetime.now().strftime('%Y-%m-%d')

        for data in datas:
            item = ZjWebspidersItem()
            timestamp = data['pubDate']
            contents = data['title']
            if timestamp_eq_time(timestamp):
                if ARCHIVE in contents or NUMERIC in contents or DATAS in contents \
                        or ELEC_FILE in contents or FILES in contents:

                    item['dates'] = data['pubDate']
                    item['title'] = contents
                    item['link'] = data['url']

                    yield item

