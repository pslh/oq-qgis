# -*- coding: utf-8 -*-

"""
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

from catalogue_events import Ui_CatalogueEvents
from rangeFilter import DoubleRangeFilter, DateRangeFilter


class GemDock(QDockWidget, Ui_CatalogueEvents):
    def __init__(self, iface, parent=None):
        QDockWidget.__init__(self, parent)
        self.setupUi(self)
        self.add_range_sliders()

    def closeEvent(self, event):
        self.emit( SIGNAL( "closed" ), self )
        return QDockWidget.closeEvent(self, event)

    def add_range_sliders(self):
        self.mag_range.setOrientation(Qt.Horizontal)
        self.date_range.setOrientation(Qt.Horizontal)
	self.mag_range.setMinimum(1)
	self.mag_range.setMaximum(10)
	self.mag_range.setLowValue(5)
	self.mag_range.setHighValue(8)

    def on_filterButton_clicked(self):
	selectedItems = self.agenciesCombo.checkedItems()
	
