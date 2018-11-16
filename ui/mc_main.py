# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\material_id_creator\ui\mc_main.ui'
#
# Created: Fri Nov 16 00:40:44 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(404, 586)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.materiIds_LW = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.materiIds_LW.sizePolicy().hasHeightForWidth())
        self.materiIds_LW.setSizePolicy(sizePolicy)
        self.materiIds_LW.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.materiIds_LW.setObjectName("materiIds_LW")
        self.verticalLayout_2.addWidget(self.materiIds_LW)
        self.addMatPB = QtGui.QPushButton(self.centralwidget)
        self.addMatPB.setObjectName("addMatPB")
        self.verticalLayout_2.addWidget(self.addMatPB)
        spacerItem = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.saveFilePB = QtGui.QPushButton(self.centralwidget)
        self.saveFilePB.setObjectName("saveFilePB")
        self.verticalLayout_2.addWidget(self.saveFilePB)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 404, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTest = QtGui.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.actionImport_material_id_file = QtGui.QAction(MainWindow)
        self.actionImport_material_id_file.setObjectName("actionImport_material_id_file")
        self.actionLoad_latest_project_mdf = QtGui.QAction(MainWindow)
        self.actionLoad_latest_project_mdf.setObjectName("actionLoad_latest_project_mdf")
        self.menuFile.addAction(self.actionLoad_latest_project_mdf)
        self.menuFile.addAction(self.actionImport_material_id_file)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "create material ids", None, QtGui.QApplication.UnicodeUTF8))
        self.addMatPB.setText(QtGui.QApplication.translate("MainWindow", "add Material ID", None, QtGui.QApplication.UnicodeUTF8))
        self.saveFilePB.setText(QtGui.QApplication.translate("MainWindow", "saveFile", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTest.setText(QtGui.QApplication.translate("MainWindow", "test", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_material_id_file.setText(QtGui.QApplication.translate("MainWindow", "import mdf", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_latest_project_mdf.setText(QtGui.QApplication.translate("MainWindow", "load latest project mdf", None, QtGui.QApplication.UnicodeUTF8))

