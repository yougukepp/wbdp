#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class WBDPConfiger: 
    def __init__(self): 
        # 整体配置
        self.mDbFileName = r'storage.db'
        self.mUrl = r'http://api.worldbank.org/zh/countries/all/indicators/NY.GDP.MKTP.CD?format=json&per_page=10'
        
        # storager配置
        self.mTableName = 'value '
        self.mTableFormat = """(COUNTRY         TEXT                NOT NULL,
                    YEAR            INTEGER             NOT NULL,
                    INDICATOR       TEXT                NOT NULL,
                    VALUAE          REAL                NOT NULL,
                    CONSTRAINT CI   PRIMARY KEY         (COUNTRY, YEAR, INDICATOR)
                    );"""
        self.mConditions = ('COUNTRY', 'YEAR', 'INDICATOR')

        # jsoner配置
        self.mHeadIndex = 0
        self.mContentIndex = 1
        self.mPageMaxKey = 'pages'

        # 世行gdp数据格式
        # 双层Tuple结构
        self.mKeyTuple = (('country', 'value',), ('date',), ('indicator', 'id',))
        self.mValueTuple = (('value',),)

    def GetDbFileName(self):
        return self.mDbFileName

    def GetTableName(self):
        return self.mTableName

    def GetTableFormat(self):
        return self.mTableFormat

    def GetConditions(self):
        return self.mConditions

    def GetUrl(self):
        return self.mUrl

    def GetHeadIndex(self):
        return self.mHeadIndex

    def GetContentIndex(self):
        return self.mContentIndex

    def GetPageMaxKey(self):
        return self.mPageMaxKey

    def GetKeyTuple(self):
        return self.mKeyTuple

    def GetValueTuple(self):
        return self.mValueTuple

    def Show(self):
        print('DbFile:'       + self.mDbFileName)
        print('Url:'          + self.mUrl)
        print('TableName:'    + self.mTableName)
        print('TableFormat:'  + self.mTableFormat)
        print('HeadIndex:'    + str(self.mHeadIndex))
        print('ContentIndex:' + str(self.mContentIndex))
        print('PageMaxKey:'   + self.mPageMaxKey)
        print('KeyTuple:'     + str(self.mKeyTuple))
        print('ValueTuple:'   + str(self.mValueTuple))

if __name__ == '__main__':
    configer = WBDPConfiger()
    configer.Show()

