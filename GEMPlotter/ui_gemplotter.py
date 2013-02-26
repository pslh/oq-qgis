# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_gemplotter.ui'
#
# Created: Tue Feb 26 15:12:37 2013
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
        self.gridLayout = QtGui.QGridLayout(GEMPlotter)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(GEMPlotter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cancelButton = QtGui.QPushButton(GEMPlotter)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout.addWidget(self.cancelButton, 3, 2, 1, 1)
        self.chooseButton = QtGui.QToolButton(GEMPlotter)
        self.chooseButton.setObjectName(_fromUtf8("chooseButton"))
        self.gridLayout.addWidget(self.chooseButton, 0, 2, 1, 1)
        self.taxonomyCombo = QtGui.QComboBox(GEMPlotter)
        self.taxonomyCombo.setEnabled(False)
        self.taxonomyCombo.setObjectName(_fromUtf8("taxonomyCombo"))
        self.gridLayout.addWidget(self.taxonomyCombo, 1, 1, 1, 1)
        self.label = QtGui.QLabel(GEMPlotter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.widget = QtGui.QWidget(GEMPlotter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout.addWidget(self.widget, 2, 1, 1, 1)

        self.retranslateUi(GEMPlotter)
        QtCore.QMetaObject.connectSlotsByName(GEMPlotter)
        GEMPlotter.setTabOrder(self.chooseButton, self.taxonomyCombo)
        GEMPlotter.setTabOrder(self.taxonomyCombo, self.cancelButton)

    def retranslateUi(self, GEMPlotter):
        GEMPlotter.setWindowTitle(QtGui.QApplication.translate("GEMPlotter", "GEMPlotter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GEMPlotter", "Taxonomy", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("GEMPlotter", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.chooseButton.setText(QtGui.QApplication.translate("GEMPlotter", "Choose", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GEMPlotter", "GEM Plotter. Please select a Fragility Model .xml file", None, QtGui.QApplication.UnicodeUTF8))

