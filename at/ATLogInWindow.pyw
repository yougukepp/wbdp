#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ATMainWindow import ATMainWindow

class ATLogInWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("登录窗口")

        self.m_win = ATMainWindow()

        self.m_Label = QLabel("密码:")
        self.m_Text = QLineEdit("888888")
        self.m_ButtonOk = QPushButton("确定")
        self.m_ButtonCancel = QPushButton("取消")

        layout = QGridLayout();
        layout.addWidget(self.m_Label, 1, 1, 1, 1)
        layout.addWidget(self.m_Text, 1, 2, 1, 1)
        layout.addWidget(self.m_ButtonOk, 2, 1, 1, 1)
        layout.addWidget(self.m_ButtonCancel, 2, 2, 1, 1)

        self.setLayout(layout);
        self.m_ButtonCancel.clicked.connect(self.CancelSlot)
        self.m_ButtonOk.clicked.connect(self.OkSlot)

    def OkSlot(self):
        passWord = self.m_Text.text()
        if "888888" == passWord:
          self.hide()
          #self.m_win.showMaximized()
          self.m_win.show()
        else:
          errMessageBox = QMessageBox()
          errMessageBox.setText("初始密码是888888")
          errMessageBox.exec_()

    def CancelSlot(self):
        self.m_Text.setText("")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win = ATLogInWindow()
    win.show()

    sys.exit(app.exec_())



