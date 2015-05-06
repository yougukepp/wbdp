#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import time

gTableTypeInSqliteMaster = 0
gTableNameInSqliteMaster = 1

gCmdHeadCreateTable = 'CREATE TABLE '
gTableName = 'value '

gTableFormat = """(COUNTRY         TEXT                NOT NULL,
                    YEAR            INTEGER             NOT NULL,
                    INDICATOR       TEXT                NOT NULL,
                    VALUAE          REAL                NOT NULL,
                    CONSTRAINT CI   PRIMARY KEY         (COUNTRY, YEAR, INDICATOR)
                    );"""

class WBDPStorager:
    def __init__(self, dbFileName): 
        self.mConn = sqlite3.connect(dbFileName)
        tableList = self.GetTableList()

        if 0 == len(tableList): # 未建表 则建表
            print('建' + gTableName + '表...') 
            cmdCreateTable = gCmdHeadCreateTable + gTableName + gTableFormat
            #print(cmdCreateTable)
            self.mConn.execute(cmdCreateTable)

    def GetTableList(self):
        rst  = []
        data = self.ShowTable('sqlite_master')
        for item in data:
            typeStr = item[gTableTypeInSqliteMaster]
            nameStr = item[gTableNameInSqliteMaster]
            if 'table' == typeStr: # 仅显示表
                rst.append(nameStr)

        return rst

    def ShowTable(self, tableName):
        cmdStr = 'select * from ' + tableName
        cursor = self.mConn.execute(cmdStr) 
        data = cursor.fetchall() 

        return data 

    def UpdateTable(self, dataName, dataList):
        pass

if __name__ == '__main__':
    db = WBDPStorager()
    
