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

 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "eqcatalogue"


def description():
    return "earthquake catalogue tool"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "GEM Foundation"

def email():
    return "devops@openquake.org"

def classFactory(iface):
    # load EqCatalogue class from file EqCatalogue
    from eqcatalogue import EqCatalogue
    return EqCatalogue(iface)
