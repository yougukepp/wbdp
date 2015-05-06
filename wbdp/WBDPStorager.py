#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import time

gTableTypeInSqliteMaster = 0
gTableNameInSqliteMaster = 1

gCountriesTableName = 'countries_table'

# 表名 year年
# 举例 year_2013_table

gStorageName = 'wbdp.db'
gStartYear = 1960

gCmdHeadCreateTable = "CREATE TABLE " 

gYearTableFormat = """ (ID INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL,
                       COUNTRIES_NAME     TEXT                NOT NULL,
                       INDICATORS_ID      TEXT                NOT NULL,
                       VALUAE             REAL                NOT NULL);"""

gCountriesTableFormat = """ (COUNTRIES_NAME TEXT PRIMARY KEY NOT NULL UNIQUE);"""

gCountriesTableFormatLite = """(COUNTRIES_NAME)"""

# not use
#gIndicatorsTableFormat= """ (ID INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL,
#                             INDICATORS_ID      TEXT                NOT NULL UNIQUE);"""

class WBDPStorager:
    def __init__(self): 
        self.conn = sqlite3.connect(gStorageName)
        #
        # 新建数据库
        # 
        tableList = self.GetTableList()

        if 0 == len(tableList): # 未建表 则建表
            print('开始建数据库表...')
            # 国家表
            cmdCreateTable = gCmdHeadCreateTable + gCountriesTableName + gCountriesTableFormat
            self.conn.execute(cmdCreateTable) 
            # 指标表 not use
            #cmdCreateTable = gCmdHeadCreateTable + 'indicators_table' + gIndicatorsTableFormat
            #conn.execute(cmdCreateTable)

            # 年表
            tableNameList = []

            nowYear = time.strftime("%Y", time.gmtime())

            index = 1
            size = int(nowYear) - gStartYear 
            for year in range(gStartYear, int(nowYear)):
                cmdCreateTable = gCmdHeadCreateTable + 'year_' + str(year) + '_table' + gYearTableFormat
                self.conn.execute(cmdCreateTable)
                #print(cmdCreateTable)
                #print('%4.2f%%' % (100.0 * index / size))
                index += 1

    def NeedUpdateIndexTable(self): 
        """
        如果新建的国家表
        就不需要重新生成了
        """ 
        if self.ShowTable(gCountriesTableName): # gCountriesTableName 表中有国家 不重复插入
            return False
        else:
            return True

    def GetTableList(self):
        rst  = []
        data = self.ShowTable('sqlite_master')
        for item in data:
            typeStr = item[gTableTypeInSqliteMaster]
            nameStr = item[gTableNameInSqliteMaster]
            if 'table' == typeStr:
                #rst.append((typeStr, nameStr))
                rst.append(nameStr)

        return rst
    
    def ShowTable(self, tableName):
        cmdStr = 'select * from ' + tableName
        cursor = self.conn.execute(cmdStr) 
        data = cursor.fetchall() 

        return data 

    def UpdateTable(self, dataName, dataList):
        tableName = ''
        if '国家' == dataName: 
            tableName = gCountriesTableName
            tableFormat = gCountriesTableFormatLite
        else:
            print(dataName)
            print('WBDPStorager.UpdateTable 未实现!')
            return

        i = 0
        print('写入' + dataName + '到数据库...')
        size = len(dataList)
        for v in dataList:
            values = "'" + v  + "'"
            cmdStr = 'INSERT INTO ' + tableName + tableFormat + ' VALUES (' + values + ')'
            #print(cmdStr)
            cursor = self.conn.execute(cmdStr)
            #print('%4.2f%%' % (100.0 * i / (size)))
            i += 1
        self.conn.commit()

if __name__ == '__main__':
    db = WBDPStorager()
    data = db.ShowTable(gCountriesTableName)
    print (data) 
    
    tableList = db.GetTableList()
    print(tableList)

    print('WBDPStorage 测试!')

