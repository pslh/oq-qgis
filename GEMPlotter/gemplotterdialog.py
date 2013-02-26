# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GEMPlotterDialog
                                 A QGIS plugin
 An utility to plot GEM models
                             -------------------
        begin                : 2013-02-26
        copyright            : (C) 2013 by GEM
        email                : michele@openquake.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_gemplotter import Ui_GEMPlotter
from collections import defaultdict
from matplotlib import pyplot as plt
from openquake.nrmllib.risk.parsers import \
    FragilityModelParser, VulnerabilityModelParser
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class GEMPlotterDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_GEMPlotter()
        self.ui.setupUi(self)
        self.modelfile = None

    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        self.close()

    @QtCore.pyqtSlot(int)
    def plot_ff(self, taxonomy_idx):
        #fig = FigureCanvas(Figure())
        #fig.setParent(self.ui.widget)
        if not taxonomy_idx:
            return
        taxonomy = str(self.ui.taxonomyCombo.itemText(taxonomy_idx))
        for state, y in zip(self.states, self.ff[taxonomy]):
            plt.plot(self.iml['imls'], y, label=state)
        plt.legend(loc='upper left')
        plt.show()

    @QtCore.pyqtSlot()
    def on_chooseButton_clicked(self):
        self.modelfile = str(QtGui.QFileDialog.getOpenFileName(
            self, 'Select Fragility Model file',
            QtCore.QDir.homePath(),
            'Model files (*.xml)'))
        self._fillCombo()
        self.ui.taxonomyCombo.currentIndexChanged.connect(self.plot_ff)

    def _fillCombo(self):
        p = iter(FragilityModelParser(self.modelfile))
        kind, self.iml, self.states = next(p)
        self.ff = dict((taxonomy, y) for taxonomy, y, no_damage_limit in p)
        self.ui.taxonomyCombo.addItems(['---'] + self.ff.keys())
        self.ui.taxonomyCombo.setEnabled(True)
