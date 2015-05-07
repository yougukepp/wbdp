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

    def __ParseAContent__(self, content, keyTuple):
        rstTuple = []
        # 一个值
        for aKeyTuple in keyTuple:
            v = self.__ParseAValueInCotent__(content, aKeyTuple)
            if None == v: # 空值不处理
                return None
            rstTuple.append(v)

        return rstTuple

    def __ParseAValueInCotent__(self, content, aKeyTuple):
        """
        content 为一项数据项目
        aKeyTuple 为某个值的键值的Tuple
        例如:

        content 为 {'date': '1962', 
                    'country': {'id': '1A', 'value': '阿拉伯联盟国家'}, 
                    'indicator': {'id': 'NY.GDP.MKTP.CD', 
                    'value': 'GDP（现价美元）'}, 
                    'decimal': '1',
                    'value': None}
        
        aKeyTuple 为 ('country', 'value')

        那么返回:阿拉伯联盟国家
        """
        #print(content)
        #print(aKeyTuple)

        v = content
        for aKey in aKeyTuple: # 一级级找
            v = v[aKey]
            #print(aKey)
            #print(v)
            #print()
            #break
        #print(v)
        return v

    # 实现 len 函数
    def __len__(self):
        return len(self.mContent)

    # TODO: 参数解析
    # __next__ __iter__ 用于支持迭代操作 for item in WBDPSpider
    def __next__(self): # 返回 内容
        if self.mContentIndexMax == self.mContentIndex:
            raise StopIteration
        content = self.mContent[self.mContentIndex]

        configer = WBDPConfiger()
        keyTuple = configer.GetKeyTuple()

        k = self.__ParseAContent__(content, keyTuple)
        #print(k)

        keyTuple = configer.GetValueTuple()
        v = self.__ParseAContent__(content, keyTuple)
        #print(v)
        #print()

        self.mContentIndex+= 1

        # 空值不处理
        if None == k or None == v:
            return None
        else: 
            rstDict = {}
            k = tuple(k)
            rstDict[k] = v
            return rstDict

    def __iter__(self):
        return self

if __name__ == '__main__':
    spider = WBDPJsoner('')

