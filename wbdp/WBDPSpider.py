#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import urllib.request

from WBDPDataer import WBDPDataer
from WBDPStorager import WBDPStorager

# per_page 使用默认值 50

class WBDPSpider:
    sBaseUrl = 'http://api.worldbank.org/'

    sLanguage ={
            '英文' : 'en',
            '中文' : 'zh',
            }

    sFormat = {
            'json' : 'format=json',
            }

    sDataName = {
            '指标' : 'indicators',
            '国家' : 'countries',
            'GDP'  : 'countries/all/indicators/NY.GDP.MKTP.CD'
            }

    #国家
    #http://api.worldbank.org/countries
    #指标
    #http://api.worldbank.org/indicators
    #gdp
    #http://api.worldbank.org/countries/all/indicators/NY.GDP.MKTP.CD
    #人口
    #http://api.worldbank.org/countries/all/indicators/SP.POP.TOTL

    def __init__(self):
        pass

    def GetAllGDPDict(self):
        return self.GetDataNameDict('GDP', ('date', ('country','value')), ('value'))

    def GetAllCountriesDict(self):
        return self.GetDataNameDict('国家', ('name'), ('id', 'iso2Code', 'capitalCity'))

    def GetDataNameDict(self, dataNameKey, jsonKeyName, jsonValueNameList):
        dataDict = {}
        pageMax = self.GetPageMax(dataNameKey)
        pageMax += 1 # range [min, max) 
        
        print('获取' + str(dataNameKey) + '列表...')
        for page in range(1, pageMax):
            url = self.MakeUrl(dataNameKey, page=page)
            data = self.GetData(url) 
            dataer = WBDPDataer(data)
            thisPageItems = dataer.Parse2List(jsonKeyName, jsonValueNameList)
            dataDict.update(thisPageItems)
            #print('%4.2f%%' % (100.0 * page / (pageMax - 1)))

        #print(dataDict)

        return dataDict

    def GetPageMax(self, dataNameKey):
        url = self.MakeUrl(dataNameKey)
        print(url)
        data = self.GetData(url)
        dataer = WBDPDataer(data)
        pageMax = dataer.GetPageMax()

        return pageMax

    def GetData(self, url):
        response = urllib.request.urlopen(url)
        buff = response.read()
        buff_utf8 = buff.decode('utf8')
        data = json.loads(buff_utf8) 

        return data

    def MakeUrl(self, dataNameKey, formatKey='json', languageKey='中文', page=1):
        url = self.sBaseUrl
        url += '' + self.GetLanguage(languageKey)
        url += '/' + self.GetDtaName(dataNameKey)
        url += '/?' + self.GetFormat(formatKey)
        url += '&page=' + str(page)

        return url

    def  GetLanguage(self, languageKey):
        return self.sLanguage[languageKey]

    def  GetFormat(self, formatKey):
        return self.sFormat[formatKey]

    def  GetDtaName(self, dataNameKey):
        return self.sDataName[dataNameKey]

if __name__ == '__main__':
    spider = WBDPSpider()
    storager = WBDPStorager()

    if storager.NeedUpdateIndexTable(): 
        data = spider.GetAllCountriesDict()
        storager.UpdateTable('国家', data)

    data = spider.GetAllGDPDict()
    storager.UpdateTable('国家', data)

