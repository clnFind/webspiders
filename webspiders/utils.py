# -*- coding: utf-8 -*-

import datetime
import time
import requests
import re


def timestamp_eq_time(timestamp_str):
    """
    判断时间戳是否与当天零点时间戳相等
    :param timestamp_str:
    :return:
    """
    timestamp = timestamp_str[:10]
    now = datetime.datetime.now()
    today_zero = now.strftime("%Y-%m-%d 00:00:00")
    date_zero = datetime.datetime.strptime(today_zero, '%Y-%m-%d %H:%M:%S')
    zero_timestamp = time.mktime(date_zero.timetuple())

    if timestamp == str(zero_timestamp)[:10]:
        return True
    return False


def get_ah_page_num():
    """
    从安徽政府网 获取当天 采购公告的table 总共页数
    :return:
    """

    date_today = datetime.datetime.now().strftime('%Y-%m-%d')
    url = "http://www.ahzfcg.gov.cn/cmsNewsController/getCgggNewsList.do?channelCode=cggg&dist_code=340000&" \
          "pubDateStart={dates}&pubDateEnd={dates}&pProviceCode=340000&areacode_prov=340000".format(dates=date_today)

    r = requests.get(url=url).text
    # print(r)

    numbers = re.findall(r'<label><span>\s+\S+显示(.*?) 页</span></label>', r, re.S)
    # print(numbers[0])
    return numbers[0].split()[-1]

if __name__ == '__main__':

    # timestamp_str = '1532361600000'
    # t = timestamp_eq_time(timestamp_str)
    # print(t)

    n = get_ah_page_num()
    print(n)



