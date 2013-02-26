import os
import sys
import unittest

from gemplotterdialog import GEMPlotterDialog
from PyQt4 import QtGui, QtCore, QtTest

FRAGMODEL = os.path.expanduser('~/oq-nrmllib/examples/fragm_d.xml')


class GEMPlotterTestCase(unittest.TestCase):
    def setUp(self):
        self.app = QtGui.QApplication(sys.argv)
        self.dialog = GEMPlotterDialog()
        self.dialog.modelfile = FRAGMODEL
        self.dialog._fillCombo()

    def tearDown(self):
        self.app.closeAllWindows()

    def test_damage_states(self):
        combo = self.dialog.ui.taxonomyCombo
        items = map(combo.itemText, range(combo.count()))
        self.assertEqual(['RC/DMRF-D/LR', 'RC/DMRF-D/HR'], items)
        self.assertTrue(combo.isEnabled())

    def test2(self):
        c = self.dialog.ui.taxonomyCombo
        c.currentIndexChanged.connect(self.dialog.plot_ff)
        c.setCurrentIndex(c.findText('RC/DMRF-D/LR'))
        c.currentIndexChanged.disconnect()

if __name__ == '__main__':
    unittest.main()
