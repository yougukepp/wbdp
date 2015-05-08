#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from WBDPConfiger import WBDPConfiger
from WBDPStorager import WBDPStorager

class BaseCanvas(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setMouseTracking(True)
        self.mStorager = WBDPStorager() 

        # 获取 years
        configer = WBDPConfiger()
        self.mAllYears = self.GetYearOrCountry(configer.GetYearFieldName())
        #print(self.mAllYears)

        # 获取 countries
        configer = WBDPConfiger()
        self.mAllCountries = self.GetYearOrCountry(configer.GetCountryFieldName())

        # 获取 最新 10强 国家

    def GetYearOrCountry(self, fieldName):
        rst = []

        configer = WBDPConfiger()
        tableName = configer.GetTableName() 

        # 获取year
        allData = self.mStorager.GetData(tableName = tableName, fieldName = fieldName)
        dataDict = {}
        for data in allData:
            dataDict[data[0]] = None # 数据库 格式相关
        for k in dataDict:
            rst.append(k)

        rst = sorted(rst)

        return tuple(rst)
        
    def DrawLabel(self, painter, point, labelStr):
        painter.drawText(point, labelStr)

    def paintEvent(self, event):
        configer = WBDPConfiger()

        # 清屏
        widthMargin = configer.GetWidthMargin() * self.width()
        heightMargin = configer.GetHeightMargin() * self.height()
        x0 = widthMargin
        y0 = heightMargin
        x1 = self.width() - 2 * x0
        y1 = self.height() - 2 * y0
        painter = QPainter(self)
        painter.fillRect(x0, y0, x1, y1, QColor(0, 0, 0))

        # 绘制横坐标 year
        pen = QPen(QColor(0, 255, 0))
        pen.setWidth(1)
        painter.setPen(pen) 
        
        x = 30
        y = self.height() - 2 # 经验值
        for year in self.mAllYears:
            labelStr = str(year)[2] + str(year)[3]
            point = QPoint(x, y)
            self.DrawLabel(painter, point, labelStr)
            x += 25 # 经验值
            
        # 经验值
        x0 = 30
        y -= 18
        painter.drawLine(x0, y, x, y)

        y1 = 10
        # 绘制纵坐标
        painter.drawLine(x0, y, x0, y1)

        painter.end()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win = BaseCanvas()
    win.showMaximized()

    sys.exit(app.exec_())

