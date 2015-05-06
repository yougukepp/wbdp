#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

gHeadIndex = 0
gContentIndex = 1
gPageMaxKey = 'pages'

class WBDPJsoner:
    def __init__(self, jsonStr):
        self.mData = json.loads(jsonStr) 

    def GetPageMax(self):
        head = self.GetHead()
        pageMax = head[gPageMaxKey] 

        return pageMax 
    
    # TODO: 参数解析
    def ToDict(self, keyTuple, valueTuple):
        content = self.GetContent()

        keyTupleLen = len(keyTuple)
        for k in keyTuple:
            kLen = len(k)
            print(kLen)

    def GetHead(self):
        head = self.mData[gHeadIndex]
        return head

    def GetContent(self):
        content = self.mData[gContentIndex]
        return content

if __name__ == '__main__':
    spider = WBDPJsoner('')
