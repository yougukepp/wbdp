#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from WBDPJsoner import WBDPJsoner
from WBDPSpider import WBDPSpider
from WBDPStorager import WBDPStorager
#from WBDPConfiger import WBDPConfiger

# TODO： 正常情况从WBDPStorager中获取数据

# 初始化
if __name__ == '__main__':
    spider = WBDPSpider()
    storager = WBDPStorager()

    i = 0
    iMax = len(spider)

    for item in spider:
        i += 1
        jsoner = WBDPJsoner(item)
        storager.Update(jsoner)

        print('%4.2f%%' % (100.0 * i / iMax))
        break

