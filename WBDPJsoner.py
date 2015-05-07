#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from WBDPConfiger import WBDPConfiger

class WBDPJsoner:
    def __init__(self, jsonStr):
        # 初始化 顺序不可变
        self.mData = json.loads(jsonStr) 
        self.mContent = self.__GetContent__()
        self.mContentIndex = 0
        self.mContentIndexMax = len(self.mContent) - 1

    def __GetPageMax__(self):
        configer = WBDPConfiger()
        pageMaxKey = configer.GetPageMaxKey()

        head = self.__GetHead__()
        pageMax = head[pageMaxKey] 

        return pageMax 

    def __GetHead__(self):
        configer = WBDPConfiger()
        headIndex = configer.GetHeadIndex()

        head = self.mData[headIndex]
        return head

    def __GetContent__(self):
        configer = WBDPConfiger()
        contentIndex = configer.GetContentIndex()

        content = self.mData[contentIndex]
        return content

    def __ParseKeyInContent__(self):
        configer = WBDPConfiger()
        content = self.mContent

        keyTuple = configer.GetKeyTuple()
        print(keyTuple)

    def __ParseValueInContent__(self):
        configer = WBDPConfiger()
        content = self.mContent

        valueTuple = configer.GetValueTuple()

    # 实现 len 函数
    def __len__(self):
        return len(self.mContent)

    # TODO: 参数解析
    # __next__ __iter__ 用于支持迭代操作 for item in WBDPSpider
    def __next__(self): # 返回 内容
        if self.mContentIndexMax == self.mContentIndex:
            raise StopIteration
        self.mContentIndex+= 1

        k = self.__ParseKeyInContent__()
        v = self.__ParseValueInContent__()

        rst = {}
        rst[k] = v

        return rst

    def __iter__(self):
        return self

if __name__ == '__main__':
    spider = WBDPJsoner('')

