# -*- coding: utf-8 -*-
"""
/***************************************************************************
 EqCatalogue
                                 A QGIS plugin
 earthquake catalogue tool
                              -------------------
        begin                : 2013-02-20
        copyright            : (C) 2013 by GEM Foundation
        email                : devops@openquake.org
 ***************************************************************************/

# Copyright (c) 2010-2013, GEM Foundation.
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from dock import GemDock


class EqCatalogue:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/eqcatalogue"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]
        self.dockIsVisible = True

        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/eqcatalogue_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dock = GemDock(self.iface)

    def initGui(self):
        # Create action that will start plugin configuration
        self.show_catalogue = QAction(
            QIcon(":/plugins/eqcatalogue/icon.png"),
            u"Eqcatalogue Toggle Dock", self.iface.mainWindow())
        self.show_catalogue.setCheckable(True)
        self.show_catalogue.setChecked(self.dockIsVisible)

        self.import_isf = QAction(
            QIcon(":/plugins/eqcatalogue/icon.png"),
            u"Import ISF file in db", self.iface.mainWindow())

        self.import_iaspei = QAction(
            QIcon(":/plugins/eqcatalogue/icon.png"),
            u"Import IASPEI file in db", self.iface.mainWindow())

        # connect the action to the run method
        QObject.connect(self.show_catalogue, SIGNAL("triggered()"), self.toggle_dock)
        QObject.connect(self.import_isf, SIGNAL("triggered()"),
            lambda: self.import_catalogue("Isf"))
        QObject.connect(self.import_iaspei, SIGNAL("triggered()"),
            lambda: self.import_catalogue("Iaspei"))

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.show_catalogue)
        self.iface.addPluginToMenu(u"&eqcatalogue", self.show_catalogue)
        self.iface.addPluginToMenu(u"&eqcatalogue", self.import_isf)
        self.iface.addPluginToMenu(u"&eqcatalogue", self.import_iaspei)

        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&eqcatalogue", self.show_catalogue)
        self.iface.removePluginMenu(u"&eqcatalogue", self.import_isf)
        self.iface.removePluginMenu(u"&eqcatalogue", self.import_iaspei)

        self.iface.removeToolBarIcon(self.show_catalogue)

    def toggle_dock(self):
        # show the dock
        self.dockIsVisible = not self.dockIsVisible
        self.dock.setVisible(self.dockIsVisible)

    def import_catalogue(self, format):
        if format == "Isf":
            file_type = 'Isf file (*.txt)'
        elif format == "Iaspei":
            file_type = 'Iaspei file (*.csv)'

        self.file_path = unicode(QFileDialog.getOpenFileName(
            self.iface.mainWindow(), 'Select Catalogue file', QDir.homePath(),
            file_type))
