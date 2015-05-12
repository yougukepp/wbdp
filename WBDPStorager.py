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

    def GetData(self, tableName, fieldName = '*', condition = ''):
        cmdStr = 'SELECT ' + fieldName + ' FROM ' + tableName + condition
        #print(cmdStr)
        cursor = self.mConn.execute(cmdStr) 
        data = cursor.fetchall() 

        return data 

    def __GetDataDesc__(self): 
        '''
        仅实现 GDP排序
        '''
        configer = WBDPConfiger()

        tableName = configer.GetTableName()
        fieldName = 'COUNTRY, VALUAE'
        conditionStr = "WHERE YEAR = '2013' ORDER BY VALUAE DESC" 
        
        data = self.GetData(tableName, fieldName, conditionStr)

        return data

    def __GetTableList__(self):
        rst  = []
        data = self.GetData('sqlite_master')
        for item in data:
            typeStr = item[gTableTypeInSqliteMaster]
            nameStr = item[gTableNameInSqliteMaster]
            if 'table' == typeStr: # 仅显示表
                rst.append(nameStr)

        return rst

    def Update(self, jsoner):
        for item in jsoner:
            if None != item:
                self.__UpdateALine__(item)
        # 提交
        self.mConn.commit()

    def __UpdateALine__(self, item): 
        # 实现数据库插入
        #print('item:', end = '')
        #print(item)
        configer = WBDPConfiger()
        tableName = configer.GetTableName()
        conditions = configer.GetConditions()

        # 地区数据不入数据库
        area = configer.GetArea()
        country = item[0][0] #WBDPJsoner中构造
        if country in area:
            return

        # 构造查找条件
        #(key, value) WBDPJsoner中构造
        keyTuple = item[0]
        conditionStr = 'WHERE '
        i = 0
        for c in conditions:
            if 0 != i:
                conditionStr += ' AND '
            conditionStr += c
            conditionStr += '=' + "'" + keyTuple[i] + "'"
            i += 1
        #print(conditionStr)

        data = self.GetData(tableName, fieldName = '*', condition = conditionStr)

        if 0 == len(data): # 无该项 Insert
            self.__Insert__(item)
        else: # 有该项 Update
            self.__UpdateDb__(item)

    def __Insert__(self, item): 
        configer = WBDPConfiger()
        tableName = configer.GetTableName()
        tableSimpleFormat = configer.GetTableSimpleFormat()

        #(key, value) WBDPJsoner中构造
        keyTuple = item[0]
        valueTuple = item[1]
        valuesStr = ''

        for k in keyTuple:
            valuesStr += "'" + k + "'" + ','

        i = 0
        for v in valueTuple:
            if 0 != i:
                valuesStr += ','
            valuesStr +=  v
            i += 1

        cmdInsertTable = 'INSERT INTO ' + tableName + tableSimpleFormat + ' VALUES (' + valuesStr + ')'
        #print(cmdInsertTable) 
        self.mConn.execute(cmdInsertTable)

    def __UpdateDb__(self, item):
        """
        TODO: 实现更新操作
        """
        print("WBDPStorager.__UpdateDb__未实现")

if __name__ == '__main__': 
    db = WBDPStorager()
    data = db.__GetDataDesc__()
    for d in data:
        print(d)
    
