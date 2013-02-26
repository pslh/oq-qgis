# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GEMPlotter
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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "gem-plotter"


def description():
    return "An utility to plot GEM models"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "GEM"

def email():
    return "michele@openquake.org"

def classFactory(iface):
    # load GEMPlotter class from file GEMPlotter
    from gemplotter import GEMPlotter
    return GEMPlotter(iface)
