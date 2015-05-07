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

    def __GetTableData__(self, tableName, condition = ''):
        cmdStr = 'SELECT * FROM ' + tableName + condition
        #print(cmdStr)
        cursor = self.mConn.execute(cmdStr) 
        data = cursor.fetchall() 

        return data 

    def Update(self, jsoner):
        for item in jsoner:
            if None != item:
                self.__UpdateALine__(item)

    def __UpdateALine__(self, item): 
        # 实现数据库插入
        print('item:', end = '')
        print(item)

        # 查询表
        configer = WBDPConfiger()
        tableName = configer.GetTableName()
        conditions = configer.GetConditions()

        # 构造查找条件
        #(key, value) WBDPJsoner中构造
        keyTuple = item[0]
        ValueTuple = item[1]
        conditionStr = 'WHERE '
        i = 0
        for c in conditions:
            if 0 != i:
                conditionStr += ' AND '
            conditionStr += c
            conditionStr += '=' + "'" + keyTuple[i] + "'"
            i += 1
        #print(conditionStr)

        data = self.__GetTableData__(tableName, conditionStr)

        if 0 == len(data): # 无该项 Insert
            self.__Insert__(item)
        else: # 有该项 Update
            self.__UpdateDb__(item)

    def __Insert__(self, item):
        pass

    def __UpdateDb__(self, item):
        pass

if __name__ == '__main__':
    db = WBDPStorager()
    
