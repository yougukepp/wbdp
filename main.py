#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from WBDPJsoner import WBDPJsoner
from WBDPSpider import WBDPSpider
from WBDPStorager import WBDPStorager

gDbFile = r'storage.db'
gUrl = r'http://api.worldbank.org/zh/countries/all/indicators/NY.GDP.MKTP.CD?format=json&per_page=1'

if __name__ == '__main__':
    spider = WBDPSpider(gUrl)
    db = WBDPStorager(gDbFile)

    i = 0
    iMax = len(spider)

    for item in spider:
        i += 1
        jsoner = WBDPJsoner(item)

        keyTuple = (('country', 'value',), ('indicator', 'id',), ('data',))
        valueTuple = (('data',),)

        jsoner.ToDict(keyTuple, valueTuple)

        #print(jsoner.GetContent())
        #db.update(jsoner)
        #print('%4.2f%%' % (100.0 * i / iMax))
    
