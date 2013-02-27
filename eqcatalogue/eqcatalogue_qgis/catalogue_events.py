# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eqcatalogue_qgis/catalogue_events.ui'
#
# Created: Wed Feb 27 15:58:47 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CatalogueEvents(object):
    def setupUi(self, CatalogueEvents):
        CatalogueEvents.setObjectName(_fromUtf8("CatalogueEvents"))
        CatalogueEvents.resize(390, 504)
        self.formLayoutWidget = QtGui.QWidget(CatalogueEvents)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 29, 371, 441))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.eventsLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.eventsLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.eventsLayout.setMargin(0)
        self.eventsLayout.setObjectName(_fromUtf8("eventsLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.eventsLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBox_2 = QtGui.QComboBox(self.formLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.eventsLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_2)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.eventsLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtGui.QComboBox(self.formLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.eventsLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.eventsLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.magLayout = QtGui.QVBoxLayout()
        self.magLayout.setObjectName(_fromUtf8("magLayout"))
        self.eventsLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.magLayout)
        self.timeLayout = QtGui.QVBoxLayout()
        self.timeLayout.setObjectName(_fromUtf8("timeLayout"))
        self.eventsLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.timeLayout)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.eventsLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)

        self.retranslateUi(CatalogueEvents)
        QtCore.QMetaObject.connectSlotsByName(CatalogueEvents)

    def retranslateUi(self, CatalogueEvents):
        CatalogueEvents.setWindowTitle(QtGui.QApplication.translate("CatalogueEvents", "Catalogue Events", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CatalogueEvents", "Agencies: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CatalogueEvents", "Scales:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CatalogueEvents", "Magnitude range:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CatalogueEvents", "Time range:", None, QtGui.QApplication.UnicodeUTF8))

