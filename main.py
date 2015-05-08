#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from WBDPJsoner import WBDPJsoner
from WBDPSpider import WBDPSpider
from WBDPStorager import WBDPStorager
from WBDPConfiger import WBDPConfiger

# 初始化
def InitData():
    configer = WBDPConfiger()

    if configer.HasInitted():
        #print('初始化完成 无需初始化')
        return

    print('初始化...')

    spider = WBDPSpider()
    storager = WBDPStorager()

    i = 0
    iMax = len(spider)

    print('下载 & 初始化数据库...')
    for item in spider:
        i += 1
        jsoner = WBDPJsoner(item)
        storager.Update(jsoner)

        print('%4.2f%%' % (100.0 * i / iMax), end='\r')

    print('完成       ') # 不留空格会有干扰

    # 设置初始化完成标记
    configer.SetInitFlag()

if __name__ == '__main__':
    InitData() 
    
    # TODO： 正常情况从WBDPStorager中获取数据



