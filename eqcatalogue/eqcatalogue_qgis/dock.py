# -*- coding: utf-8 -*-

"""
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

from catalogue_events import Ui_CatalogueEvents


class GemDock(QDockWidget, Ui_CatalogueEvents):
    def __init__(self, iface, parent=None):
        QDockWidget.__init__(self, parent)
        self.setupUi(self)
        self.add_range_sliders()

    def closeEvent(self, event):
        self.emit( SIGNAL( "closed" ), self )
        return QDockWidget.closeEvent(self, event)

    def add_range_sliders(self):
        pass
        #self.ui.magLayout.addWidget()
        #self.ui.timeLayout.addWidget()
