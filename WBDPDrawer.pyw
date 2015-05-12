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

        self.mCanvas = {}

        configer = WBDPConfiger()

        # 获取 years
        self.mAllYears = self.GetYearOrCountry(configer.GetYearFieldName())
        #print(self.mAllYears)

        # 获取 countries
        self.mAllCountries = self.GetYearOrCountry(configer.GetCountryFieldName())

        # 获取 最新 10强 国家 数据
        data = self.mStorager.GetDataDesc()
        self.mTopTenCountriesData = {}
        for i in range(0,10):
            country = data[i][0]
            k = country
            vTupleList = self.mStorager.GetDataOfACountry(country)
            v = []
            for d in vTupleList:
                v.append(d[1])
            self.mTopTenCountriesData[k] = v

        for k in self.mTopTenCountriesData:
            data = self.mTopTenCountriesData
            print(k)
            print(data[k])

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

    def LimitInCanvasX(self, x):
        xMin = 0
        xMax = self.width()

        # x坐标转换 加上边界
        xMargin = self.mCanvas['x'][0]
        x = xMargin + x

        # x范围限制
        if x < xMin:
            x = xMin 

        if x> xMax:
            x = xMax

        return x

    def LimitInCanvasY(self, y):
        yMin = 0
        yMax = self.height()

        #print('ymin:%d,yMax:%d' % (yMin, yMax))
        #print('y:%d =>' % y, end='')

        # y坐标转换
        # qt原点在左上角 笛卡尔坐标系原点在左下角
        # 另外在加上边界
        yMargin = self.mCanvas['y'][0]
        yMarginMax = self.mCanvas['y'][1]
        y = yMargin + yMarginMax - y

        # y范围限制
        if y < yMin:
            y = yMin

        if y > yMax:
            y = yMax

        #print(y)

        #print('yMargin:%d,yMarginMax:%d' % (yMargin, yMarginMax))

        return y

    def DrawLabel(self, painter, x, y, labelStr):
        # 笛卡尔 => Qt坐标系
        #print('(%d,%d)=>' % (x, y), end='')
        x = self.LimitInCanvasX(x)
        y = self.LimitInCanvasY(y)
        #print('(%d,%d)' % (x, y))
        point = QPoint(x, y) 
        painter.drawText(point, labelStr)

    def DrawLine(self, painter, x0, y0, x1, y1):
        """
        笛卡尔坐标系绘图
        """
        #print('(%d, %d) => (%d, %d)' % (x0,y0,x1,y1))

        # TODO:范围限定于 Widget内
        x0 = self.LimitInCanvasX(x0)
        x1 = self.LimitInCanvasX(x1)
        y0 = self.LimitInCanvasY(y0)
        y1 = self.LimitInCanvasY(y1)
        #print('(%d, %d) => (%d, %d)' % (x0,y0,x1,y1))

        painter.drawLine(x0, y0, x1, y1)

    def paintEvent(self, event):

        configer = WBDPConfiger()
        width = self.width()
        height = self.height()

        # 绘图边界
        xMargin = configer.GetWidthMargin() * width
        yMargin = configer.GetHeightMargin() * height
        xMin = int(xMargin)
        yMin = int(yMargin)
        xMax = int(width - 2 * xMin)
        yMax = int(height - 2 * yMin)
        self.mCanvas = { 'x':(xMin, xMax), 'y':(yMin, yMax) }
        #print('(%d,%d)' % (width, height))
        #print(self.mCanvas)

        # 清屏
        painter = QPainter(self)
        painter.fillRect(0, 0, width, height, QColor(0, 0, 0)) #涂黑

        # 绘制横坐标 year
        pen = QPen(QColor(0, 255, 0))
        pen.setWidth(1)
        painter.setPen(pen) 

        xMax = self.mCanvas['x'][1]
        self.DrawLine(painter, 0, 0, xMax, 0)

        # 绘制纵坐标
        yMax = self.mCanvas['y'][1]
        self.DrawLine(painter, 0, 0, 0, yMax)

        # 坐标 标签
        y = -15
        yearLen = len(self.mAllYears)
        xStep = (self.mCanvas['x'][1] - self.mCanvas['x'][0]) / yearLen
        xNow = 0
        for year in self.mAllYears:
            #print('begin')
            labelStr = str(year)[2] + str(year)[3] 
            #print('(%f,%d)' % (xNow, y))
            self.DrawLabel(painter, xNow, y, labelStr)
            xNow += xStep
            #print('end')

        # 绘制中国数据
        maxValue = self.GetMaxValue()
        minValue = self.GetMinValue()
        #self.mTopTenCountriesData

        # 比率
        rate = 1.0 * (maxValue - minValue) / (self.mCanvas['y'][1] - self.mCanvas['y'][0])
        print(rate)

        painter.end()

    def GetMaxValue(self):
        data = self.mTopTenCountriesData

        vMax = 0
        for countryData in data:
            for aData in data[countryData]:
                if vMax < aData:
                    vMax = aData

        return vMax

    def GetMinValue(self):
        data = self.mTopTenCountriesData

        vMin = 10**100
        for countryData in data:
            for aData in data[countryData]:
                if vMin > aData:
                    vMin = aData

        return vMin



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win = BaseCanvas()
    win.showMaximized()

    sys.exit(app.exec_())

