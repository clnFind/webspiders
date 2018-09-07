# webspiders
* Crawling for tender data from government websites by scrapy。
* Detailed usage， please see https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html

### Note info
* webspiders  -- 包含爬虫的配置、实现具体爬虫的脚本
* constant.py -- 常量配置文件，包括爬虫提取信息包含的关键词、邮箱服务配置
* run.sh -- 执行脚本，包含爬虫和邮箱发送爬虫结果
* run_spiders.py  -- 执行所有爬虫的异步脚本
* run_utils.py -- 邮箱发送爬虫结果的实现
* spider_result.json -- 爬虫结果保存文件
