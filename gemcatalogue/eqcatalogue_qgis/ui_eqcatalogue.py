# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eqcatalogue_qgis/ui_eqcatalogue.ui'
#
# Created: Thu Feb 21 11:00:58 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EqCatalogue(object):
    def setupUi(self, EqCatalogue):
        EqCatalogue.setObjectName(_fromUtf8("EqCatalogue"))
        EqCatalogue.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(EqCatalogue)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(EqCatalogue)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EqCatalogue.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EqCatalogue.reject)
        QtCore.QMetaObject.connectSlotsByName(EqCatalogue)

    def retranslateUi(self, EqCatalogue):
        EqCatalogue.setWindowTitle(QtGui.QApplication.translate("EqCatalogue", "EqCatalogue", None, QtGui.QApplication.UnicodeUTF8))

