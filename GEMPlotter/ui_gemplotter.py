# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_gemplotter.ui'
#
# Created: Tue Feb 26 16:25:12 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GEMPlotter(object):
    def setupUi(self, GEMPlotter):
        GEMPlotter.setObjectName(_fromUtf8("GEMPlotter"))
        GEMPlotter.resize(532, 300)
        self.verticalLayout = QtGui.QVBoxLayout(GEMPlotter)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(GEMPlotter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.chooseButton = QtGui.QToolButton(GEMPlotter)
        self.chooseButton.setObjectName(_fromUtf8("chooseButton"))
        self.horizontalLayout.addWidget(self.chooseButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.taxonomyCombo = QtGui.QComboBox(GEMPlotter)
        self.taxonomyCombo.setEnabled(False)
        self.taxonomyCombo.setObjectName(_fromUtf8("taxonomyCombo"))
        self.taxonomyCombo.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.taxonomyCombo)
        self.plotLayout = QtGui.QHBoxLayout()
        self.plotLayout.setObjectName(_fromUtf8("plotLayout"))
        self.verticalLayout.addLayout(self.plotLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.saveButton = QtGui.QPushButton(GEMPlotter)
        self.saveButton.setEnabled(False)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.cancelButton = QtGui.QPushButton(GEMPlotter)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(GEMPlotter)
        QtCore.QMetaObject.connectSlotsByName(GEMPlotter)

    def retranslateUi(self, GEMPlotter):
        GEMPlotter.setWindowTitle(QtGui.QApplication.translate("GEMPlotter", "GEMPlotter", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GEMPlotter", "GEM Plotter. Please select a Fragility Model .xml file", None, QtGui.QApplication.UnicodeUTF8))
        self.chooseButton.setText(QtGui.QApplication.translate("GEMPlotter", "Choose", None, QtGui.QApplication.UnicodeUTF8))
        self.taxonomyCombo.setItemText(0, QtGui.QApplication.translate("GEMPlotter", "Taxonomy", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("GEMPlotter", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("GEMPlotter", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

