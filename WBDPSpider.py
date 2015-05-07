#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

from WBDPJsoner import WBDPJsoner
from WBDPConfiger import WBDPConfiger

class WBDPSpider:
    def __init__(self): 
        configer = WBDPConfiger()
        self.mUrl = configer.GetUrl()
        data = self.__GetData__(self.mUrl)
        jsoner = WBDPJsoner(data)
        self.mPageMax = jsoner.__GetPageMax__()
        self.mPageIndex = 0

    def __GetData__(self, url):
        response = urllib.request.urlopen(url)
        buff = response.read()
        buff_utf8 = buff.decode('utf8')
        return buff_utf8

    # 实现 len 函数
    def __len__(self):
        return self.mPageMax

    # __next__ __iter__ 用于支持迭代操作 for item in WBDPSpider
    def __next__(self): # 返回 内容
        self.mPageIndex += 1
        if self.mPageIndex > self.mPageMax:
            raise StopIteration

        url = self.mUrl + '&page=' + str(self.mPageIndex)
        data = self.__GetData__(url)
        return data

    def __iter__(self):
        return self

if __name__ == '__main__':
    gUrl = r'http://api.worldbank.org/zh/countries/all/indicators/NY.GDP.MKTP.CD?format=json'
    spider = WBDPSpider(gUrl)

