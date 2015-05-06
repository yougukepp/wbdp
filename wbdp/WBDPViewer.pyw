#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from WBDPSpider import WBDPSpider

class WBDPViewer(QMainWindow):
    def __init__(self, parent=None):
        super(WBDPViewer, self).__init__(parent) 
        
        updateDataBaseAct = QAction("&UDB", self)
        updateDataBaseAct.setStatusTip("Update DataBase")
        updateDataBaseAct.triggered.connect(self.UpdateDataBase) 

        fileToolBar = self.addToolBar("UDB")
        fileToolBar.addAction(updateDataBaseAct)
        fileToolBar.setAllowedAreas(Qt.TopToolBarArea | Qt.BottomToolBarArea)
        self.addToolBar(Qt.TopToolBarArea, fileToolBar)
        
        tableWidget = QTableWidget() 
        self.setCentralWidget(tableWidget)

    def UpdateDataBase(self):
        print('begin update')
        print('end update')
        
if __name__ == '__main__':

  app = QApplication(sys.argv)
  win = WBDPViewer()
  #win.showMaximized()
  win.show()
  sys.exit(app.exec_())

