# -*- coding: utf-8 -*-
import datetime

import scrapy

from constant import ARCHIVE
from constant import NUMERIC
from constant import DATAS
from constant import ELEC_FILE
from constant import FILES
from webspiders.items import JsWebspidersItem
from webspiders.utils import get_ah_page_num


class AhSpider(scrapy.spiders.Spider):
    """
    爬取安徽政府网的关于档案类的采购公告信息
    """
    name = "ahweb"
    allowed_domains = ['www.ahzfcg.gov.cn']

    date_today = datetime.datetime.now().strftime('%Y-%m-%d')
    start_urls = []
    page_num = int(get_ah_page_num())

    url = "http://www.ahzfcg.gov.cn/cmsNewsController/getCgggNewsList.do?" \
          "dist_code=340000&pubDateStart={dates}&pubDateEnd={dates}&pProviceCode=340000&pageNum={page}"

    for i in range(1, page_num+1):
        start_urls.append(url.format(dates=date_today, page=i))

    def parse(self, response):

        for sel in response.xpath('//table/tr'):

            item = JsWebspidersItem()

            pattern = '\S+{archive}\S+|\S+{numeric}\S+|\S+{files}\S+|\S+{datas}\S+|\S+{elec_file}\S+'.format(
                archive=ARCHIVE, numeric=NUMERIC, files=FILES, datas=DATAS, elec_file=ELEC_FILE
            )
            contents = sel.xpath('td[@width]/a/@title').re(pattern)

            if contents:
                print("############________ :  ", contents)
                item['dates'] = self.date_today
                item['title'] = contents[0]
                item['link'] = "http://www.ahzfcg.gov.cn" + sel.xpath('td[@width]/a/@href').extract()[0]

                yield item
