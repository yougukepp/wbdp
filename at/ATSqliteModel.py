#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *

from datetime import datetime

class ATSqliteModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super(ATSqliteModel, self).__init__(parent)

    def rowCount(self, index):
        #print("TODO:返回行数")
        return 2

    def columnCount(self, index):
        #print("TODO:返回列数")
        return 3

    def data(self, index, role):
        print("TODO:读出数据")
        if role == Qt.DisplayRole:
            return "pp"
        return None

    def headerData(self, section, orientation, role):
        #print("TODO:显示表头")
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                if 0 == section:
                    return "first";
                elif 1 == section:
                    return "second"
                elif 2 == section:
                    return "third"
                else:
                    pass
        return None

    def setData(self, index, value, role = Qt.EditRole):
        #print("TODO:实现数据保存")
        if role != Qt.EditRole:
            return True
        return True

    def flags(self, index):
        print("TODO:返回该项的权限")
        return Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled

if __name__ == '__main__':
  import sys
  print("暂时没有想到如何自测。")

