#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from WBDPJsoner import WBDPJsoner
from WBDPSpider import WBDPSpider
from WBDPStorager import WBDPStorager

gDbFile = r'storage.db'
gUrl = r'http://api.worldbank.org/zh/countries/all/indicators/NY.GDP.MKTP.CD?format=json'

if __name__ == '__main__':
    spider = WBDPSpider(gUrl)
    db = WBDPStorager(gDbFile)

    """
    # 显示进度
    for item in spider:
        jsoner = WBDPJsoner(item)
        db.update(jsoner)
    """
    
