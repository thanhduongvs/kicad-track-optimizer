# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(353, 183)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.buttonClose = QPushButton(self.centralwidget)
        self.buttonClose.setObjectName(u"buttonClose")

        self.horizontalLayout_2.addWidget(self.buttonClose)

        self.buttonConnect = QPushButton(self.centralwidget)
        self.buttonConnect.setObjectName(u"buttonConnect")

        self.horizontalLayout_2.addWidget(self.buttonConnect)

        self.buttonRun = QPushButton(self.centralwidget)
        self.buttonRun.setObjectName(u"buttonRun")

        self.horizontalLayout_2.addWidget(self.buttonRun)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout_3.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkRemove = QCheckBox(self.centralwidget)
        self.checkRemove.setObjectName(u"checkRemove")

        self.verticalLayout_3.addWidget(self.checkRemove)

        self.checkMerg = QCheckBox(self.centralwidget)
        self.checkMerg.setObjectName(u"checkMerg")

        self.verticalLayout_3.addWidget(self.checkMerg)

        self.checkTotal = QCheckBox(self.centralwidget)
        self.checkTotal.setObjectName(u"checkTotal")

        self.verticalLayout_3.addWidget(self.checkTotal)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 353, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buttonClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.buttonConnect.setText(QCoreApplication.translate("MainWindow", u"Connect to KiCad", None))
        self.buttonRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.checkRemove.setText(QCoreApplication.translate("MainWindow", u"Remove stubs track", None))
        self.checkMerg.setText(QCoreApplication.translate("MainWindow", u"Merging collinear tracks", None))
        self.checkTotal.setText(QCoreApplication.translate("MainWindow", u"Remove stubs track + Merging collinear tracks", None))
    # retranslateUi

