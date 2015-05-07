#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

from WBDPConfiger import WBDPConfiger

gTableTypeInSqliteMaster = 0
gTableNameInSqliteMaster = 1

class WBDPStorager:
    def __init__(self): 
        configer = WBDPConfiger()
        dbFileName = configer.GetDbFileName()
        self.mConn = sqlite3.connect(dbFileName)
        tableList = self.__GetTableList__()

        if 0 == len(tableList): # 未建表 则建表
            tableName = configer.GetTableName()
            tableFormat = configer.GetTableFormat()
            print('建' + tableName + '表...') 
            #print(cmdCreateTable)
            cmdCreateTable = 'CREATE TABLE ' + tableName + tableFormat
            self.mConn.execute(cmdCreateTable)

    def __GetTableList__(self):
        rst  = []
        data = self.__GetTableData__('sqlite_master')
        for item in data:
            typeStr = item[gTableTypeInSqliteMaster]
            nameStr = item[gTableNameInSqliteMaster]
            if 'table' == typeStr: # 仅显示表
                rst.append(nameStr)

        return rst

    def __GetTableData__(self, tableName):
        cmdStr = 'SELECT * FROM ' + tableName
        cursor = self.mConn.execute(cmdStr) 
        data = cursor.fetchall() 

        return data 

    def Update(self, jsoner):
        for item in jsoner:
            print(item)
            break

if __name__ == '__main__':
    db = WBDPStorager()
    
