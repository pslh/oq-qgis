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

import uuid
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from dock import GemDock

from eqcatalogue import CatalogueDatabase, filtering
from eqcatalogue.importers import V1, Iaspei, store_events

FMT_MAP = {'isf': V1, 'iaspei': Iaspei}


class EqCatalogue:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = QFileInfo(
            QgsApplication.qgisUserDbFilePath()
        ).path() + "/python/plugins/eqcatalogue"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]
        self.dockIsVisible = True

        if QFileInfo(self.plugin_dir).exists():
            localePath = (self.plugin_dir + "/i18n/eqcatalogue_" +
                          locale + ".qm")

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dock = GemDock(self.iface)

    def initGui(self):
        # Create action that will start plugin configuration
        self.show_catalogue_action = QAction(
            QIcon(":/plugins/eqcatalogue/icon.png"),
            u"Eqcatalogue Toggle Dock", self.iface.mainWindow())
        self.show_catalogue_action.setCheckable(True)
        self.show_catalogue_action.setChecked(self.dockIsVisible)

        self.import_isf_action = QAction(
            QIcon(":/plugins/eqcatalogue/icon.png"),
            u"Import ISF file in db", self.iface.mainWindow())

        self.import_iaspei_action = QAction(
            QIcon(":/plugins/eqcatalogue/icon.png"),
            u"Import IASPEI file in db", self.iface.mainWindow())

        self.show_pippo1_action = QAction(
            QIcon(":/plugins/eqcatalogue/icon.png"),
            u"Display Sqlite Data", self.iface.mainWindow())

        self.show_pippo2_action = QAction(
            QIcon(":/plugins/eqcatalogue/icon.png"),
            u"Display Sqlite Data", self.iface.mainWindow())

        # connect the action to the run method
        QObject.connect(self.show_catalogue_action, SIGNAL("triggered()"),
                        self.toggle_dock)
        QObject.connect(self.import_isf_action, SIGNAL("triggered()"),
                        lambda: self.import_catalogue("isf"))
        QObject.connect(self.import_iaspei_action, SIGNAL("triggered()"),
                        lambda: self.import_catalogue("iaspei"))

        QObject.connect(self.show_pippo1_action, SIGNAL("triggered()"), self.show_pippo1)

        QObject.connect(self.show_pippo2_action, SIGNAL("triggered()"), self.show_pippo2)

	QObject.connect(self.dock.filterButton, SIGNAL("clicked()"), self.filter)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.show_catalogue_action)
        self.iface.addPluginToMenu(u"&eqcatalogue", self.show_catalogue_action)
        self.iface.addPluginToMenu(u"&eqcatalogue", self.import_isf_action)
        self.iface.addPluginToMenu(u"&eqcatalogue", self.import_iaspei_action)
        self.iface.addPluginToMenu(u"&eqcatalogue", self.show_pippo1_action)
        self.iface.addPluginToMenu(u"&eqcatalogue", self.show_pippo2_action)

        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock)

	self.populate_agencies()

    def populate_agencies(self):
	dbfile = '/home/michele/pippo.db'
        db = CatalogueDatabase(filename=dbfile)
        agencies = [str(a) for a in db.get_agencies()]
	self.dock.agenciesCombo.addItems(agencies)	


    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removeToolBarIcon(self.show_catalogue_action)
        self.iface.removePluginMenu(
            u"&eqcatalogue", self.show_catalogue_action)
        self.iface.removePluginMenu(u"&eqcatalogue", self.import_isf_action)
        self.iface.removePluginMenu(u"&eqcatalogue", self.import_iaspei_action)
        self.iface.removePluginMenu(u"&eqcatalogue", self.show_pippo1_action)
        self.iface.removePluginMenu(u"&eqcatalogue", self.show_pippo2_action)

    def toggle_dock(self):
        # show the dock
        self.dockIsVisible = not self.dockIsVisible
        self.dock.setVisible(self.dockIsVisible)

    ## this is an example of using the raw spatialite layer
    def show_pippo1(self, agencies=None):
        dbfile = '/home/michele/pippo.db'
        db = CatalogueDatabase(filename=dbfile)
	if agencies is None:
		agencies = db.get_agencies()
	data = filtering.WithAgencies(agencies)
	uri = QgsDataSourceURI()
	uri.setDatabase(dbfile)
	schema = ''
	table = 'catalogue_origin'
        geom_column = 'position'
        uri.setDataSource(schema, table, geom_column)

        display_name = 'Origin'
        vlayer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')
        QgsMapLayerRegistry.instance().addMapLayer(vlayer)
        ids = tuple(row.origin.id for row in data)
        vlayer.setSubsetString('id in %s' % str(ids))
        vlayer.triggerRepaint()

    ## this is an example of using an in-memory layer
    def show_pippo2(self):
        dbfile = '/home/michele/pippo.db'
        db = CatalogueDatabase(filename=dbfile)
        agencies = db.get_agencies()
        one_agency = agencies.pop()  # example PRA
        data = filtering.WithAgencies([one_agency])
        uri = QgsDataSourceURI()

        display_name = 'Origin'
        uri = 'Point?crs=epsg:4326&index=yes&uuid=%s' % uuid.uuid4()
        vlayer = QgsVectorLayer(uri, display_name, 'memory')
        QgsMapLayerRegistry.instance().addMapLayer(vlayer)

        provider = vlayer.dataProvider()
        vlayer.startEditing()
        provider.addAttributes([
            QgsField('agency', QVariant.String),
            QgsField('event_name', QVariant.String),
            QgsField('event_measure', QVariant.String),
        ])
        features = []
        for row in data:
            feat = QgsFeature()
            x, y = row.origin.position_as_tuple()
            geom = QgsGeometry.fromPoint(QgsPoint(x, y))
            feat.setGeometry(geom)
            feat.setAttributes([QVariant(str(row.agency)),
                                QVariant(row.event.name),
                                QVariant(str(row.event.measures[0]))])
            features.append(feat)
        provider.addFeatures(features)
        vlayer.commitChanges()
        vlayer.updateExtents()
	self.iface.mapCanvas().setExtent(vlayer.extent())		
	vlayer.triggerRepaint()

    def import_catalogue(self, format):
        if format == "isf":
            file_type = 'Isf file (*.txt)'
        elif format == "iaspei":
            file_type = 'Iaspei file (*.csv)'

        self.import_file_path = unicode(QFileDialog.getOpenFileName(
            self.iface.mainWindow(), 'Select Catalogue file', QDir.homePath(),
            file_type))

        self.save_file_path = unicode(QFileDialog.getSaveFileName(
            self.iface.mainWindow(), 'Save Catalogue file into',
            QDir.homePath(),
            file_type))

        self.cat_db = CatalogueDatabase(filename=self.save_file_path)
        with open(self.import_file_path, 'rb') as cat_file:
            store_events(FMT_MAP[format], cat_file, self.cat_db)

    def filter(self):
	selectedItems = self.dock.agenciesCombo.checkedItems()
	print selectedItems
        self.show_pippo1(map(str, selectedItems))
