# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eqcatalogue_qgis/catalogue_events.ui'
#
# Created: Thu Feb 28 10:45:50 2013
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
        CatalogueEvents.resize(329, 544)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inasafe/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CatalogueEvents.setWindowIcon(icon)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setContentsMargins(3, 0, 3, 3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.grpQuestion = QtGui.QGroupBox(self.dockWidgetContents)
        self.grpQuestion.setObjectName(_fromUtf8("grpQuestion"))
        self.gridLayout_3 = QtGui.QGridLayout(self.grpQuestion)
        self.gridLayout_3.setContentsMargins(0, 6, 0, 0)
        self.gridLayout_3.setVerticalSpacing(1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.date_range = DateRangeFilter(self.grpQuestion)
        self.date_range.setObjectName(_fromUtf8("date_range"))
        self.gridLayout_3.addWidget(self.date_range, 9, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.grpQuestion)
        self.label_8.setMargin(10)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 6, 0, 1, 1)
        self.cboExposure = QtGui.QComboBox(self.grpQuestion)
        self.cboExposure.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.cboExposure.setObjectName(_fromUtf8("cboExposure"))
        self.gridLayout_3.addWidget(self.cboExposure, 5, 0, 1, 2)
        self.cboHazard = QtGui.QComboBox(self.grpQuestion)
        self.cboHazard.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.cboHazard.setObjectName(_fromUtf8("cboHazard"))
        self.gridLayout_3.addWidget(self.cboHazard, 2, 0, 1, 2)
        self.label = QtGui.QLabel(self.grpQuestion)
        self.label.setMargin(10)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.grpQuestion)
        self.label_7.setMargin(10)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.grpQuestion)
        self.label_2.setMargin(10)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 8, 0, 1, 1)
        self.mag_range = DoubleRangeFilter(self.grpQuestion)
        self.mag_range.setObjectName(_fromUtf8("mag_range"))
        self.gridLayout_3.addWidget(self.mag_range, 7, 0, 1, 1)
        self.gridLayout.addWidget(self.grpQuestion, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        CatalogueEvents.setWidget(self.dockWidgetContents)
        self.label_7.setBuddy(self.cboExposure)

        self.retranslateUi(CatalogueEvents)
        QtCore.QMetaObject.connectSlotsByName(CatalogueEvents)

    def retranslateUi(self, CatalogueEvents):
        CatalogueEvents.setWindowTitle(QtGui.QApplication.translate("CatalogueEvents", "Events Catalogue", None, QtGui.QApplication.UnicodeUTF8))
        self.grpQuestion.setTitle(QtGui.QApplication.translate("CatalogueEvents", "Use criteria to filter the catalogue", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("CatalogueEvents", "Define magnitude range:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CatalogueEvents", "Select one or more agencies:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("CatalogueEvents", "Select one or more magnitude scales:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CatalogueEvents", "Define date range:", None, QtGui.QApplication.UnicodeUTF8))

from rangeFilter import DoubleRangeFilter, DateRangeFilter
import resources_rc
