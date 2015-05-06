#!/usr/bin/env python3
# -*- coding: utf-8 -*-

gHeadIndex = 0
gContentIndex = 1
gPageMaxKey = 'pages'

class WBDPDataer: 
    def __init__(self, data):
        self.mData = data

    def GetPageMax(self):
        head = self.GetHead()
        return head[gPageMaxKey] 
    
    def Parse2List(self, keyName, valueKeyTuple):
        rstDict = {}
        content = self.GetContent()

        keyList = []
        for k in keyName:
            keyList.append(k)
        print(keyList)

        for item in content:
            if item[keyName]:
                v = []
                k = item[keyName]
                for valueKey in valueKeyTuple:
                    v.append(item[valueKey])
                rstDict[k] = v
                #print(rstDict)

        return rstDict

    def Show(self):
        head = self.GetHead()
        content = self.GetContent()
        print('头部:')
        print(head)

        print('内容:')
        """
        for item in content:
            if item['name']:
                print(item['name'])
        """

    def GetHead(self):
        return self.mData[gHeadIndex]

    def GetContent(self):
        return self.mData[gContentIndex]

if __name__ == '__main__':
    dataer = WBDPDataer(None)
    print('Use WBDPSpider test me.')
    dataer.print()

