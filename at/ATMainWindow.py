#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ATTableView import ATTableView
from ATSqliteModel import ATSqliteModel

class ATMainWindow(QMainWindow):
  def __init__(self, parent=None):
    super(ATMainWindow, self).__init__(parent)

    model = ATSqliteModel()
    tableView = ATTableView()
    tableView.setModel(model)
    self.setCentralWidget(tableView)

    statusBar = QStatusBar(self)
    statusBarLabel1 = QLabel("标签1")
    statusBarLabel2 = QLabel("标签2")
    statusBarLabel3 = QLabel("标签3")
    statusBar.addWidget(statusBarLabel1)
    statusBar.addWidget(statusBarLabel2)
    statusBar.addWidget(statusBarLabel3)
    self.setStatusBar(statusBar)

if __name__ == '__main__':
  import sys

  app = QApplication(sys.argv)
  win = ATMainWindow()
  win.showMaximized ()
  sys.exit(app.exec_())

