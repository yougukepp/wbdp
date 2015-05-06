#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ATTableView(QTableView):
    def __init__(self, parent=None):
        super(ATTableView, self).__init__(parent)

if __name__ == '__main__':
  import sys
  app = QApplication(sys.argv)
  atTableView = ATTableView()
  atTableView.show()
  sys.exit(app.exec_())
