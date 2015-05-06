#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

from WBDPJsoner import WBDPJsoner

class WBDPSpider:
    def __init__(self, url):
        data = self.GetData(url)
        jsoner = WBDPJsoner(data)

        self.mPageMax = jsoner.GetPageMax()
        self.mPageIndex = 0
        self.mUrl = url

    def GetData(self, url):
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
        data = self.GetData(url)
        return data

    def __iter__(self):
        return self

if __name__ == '__main__':
    gUrl = r'http://api.worldbank.org/zh/countries/all/indicators/NY.GDP.MKTP.CD?format=json'
    spider = WBDPSpider(gUrl)

