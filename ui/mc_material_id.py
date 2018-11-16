# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\material_id_creator\ui\mc_material_id.ui'
#
# Created: Fri Nov 16 00:40:44 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mc_material_wg(object):
    def setupUi(self, mc_material_wg):
        mc_material_wg.setObjectName("mc_material_wg")
        mc_material_wg.setEnabled(True)
        mc_material_wg.resize(383, 47)
        self.horizontalLayout = QtGui.QHBoxLayout(mc_material_wg)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lockedCB = QtGui.QCheckBox(mc_material_wg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lockedCB.sizePolicy().hasHeightForWidth())
        self.lockedCB.setSizePolicy(sizePolicy)
        self.lockedCB.setText("")
        self.lockedCB.setObjectName("lockedCB")
        self.horizontalLayout.addWidget(self.lockedCB)
        self.materialName_Lb = QtGui.QLabel(mc_material_wg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.materialName_Lb.sizePolicy().hasHeightForWidth())
        self.materialName_Lb.setSizePolicy(sizePolicy)
        self.materialName_Lb.setObjectName("materialName_Lb")
        self.horizontalLayout.addWidget(self.materialName_Lb)
        self.materialName_Le = QtGui.QLineEdit(mc_material_wg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.materialName_Le.sizePolicy().hasHeightForWidth())
        self.materialName_Le.setSizePolicy(sizePolicy)
        self.materialName_Le.setMaximumSize(QtCore.QSize(180, 16777215))
        self.materialName_Le.setObjectName("materialName_Le")
        self.horizontalLayout.addWidget(self.materialName_Le)
        self.label = QtGui.QLabel(mc_material_wg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.retranslateUi(mc_material_wg)
        QtCore.QMetaObject.connectSlotsByName(mc_material_wg)

    def retranslateUi(self, mc_material_wg):
        mc_material_wg.setWindowTitle(QtGui.QApplication.translate("mc_material_wg", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.materialName_Lb.setText(QtGui.QApplication.translate("mc_material_wg", "material", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mc_material_wg", "color", None, QtGui.QApplication.UnicodeUTF8))

