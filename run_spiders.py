# -*- coding: utf-8 -*-

import os

# 必须先加载项目settings配置
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'webspiders.settings')

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


process = CrawlerProcess(get_project_settings())

# 指定多个spider
# process.crawl("jsweb")
# process.crawl("zjweb")

# 执行所有 spider
for spider_name in process.spider_loader.list():
    process.crawl(spider_name)

process.start()

# print("&&&&&&&&#######@@@@@______  ", process.spider_loader.list())



