""" This is the Bokeh charts testing interface.

"""
#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2014, Continuum Analytics, Inc. All rights reserved.
#
# Powered by the Bokeh Development Team.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

from collections import OrderedDict
import unittest

import numpy as np
import pandas as pd

from bokeh.charts import Bar

from bokeh.charts.builder.tests._utils import create_chart

#-----------------------------------------------------------------------------
# Classes and functions
#-----------------------------------------------------------------------------

class TestBar(unittest.TestCase):
    def test_supported_input(self):
        xyvalues = OrderedDict()
        xyvalues['python']=[2, 5]
        xyvalues['pypy']=[12, 40]
        xyvalues['jython']=[22, 30]

        for i, _xy in enumerate([xyvalues, dict(xyvalues), pd.DataFrame(xyvalues)]):
            bar = create_chart(Bar, _xy)
            builder = bar._builders[0]
            np.testing.assert_array_equal(builder._data['pypy'], np.array(xyvalues['pypy']))
            np.testing.assert_array_equal(builder._data['python'], np.array(xyvalues['python']))
            np.testing.assert_array_equal(builder._data['jython'], np.array(xyvalues['jython']))

            # test mid values, that should always be y/2 ..
            np.testing.assert_array_equal(builder._data['midpython'], np.array([1, 2.5]))
            np.testing.assert_array_equal(builder._data['midpypy'], np.array([6, 20]))
            np.testing.assert_array_equal(builder._data['midjython'], np.array([11, 15]))

            # stacked values should be 0 as base and + y/2 of the column
            # skipping plain dict case as stacked values randomly fails due to
            # dictionary unordered nature
            if i != 1:
                np.testing.assert_array_equal(builder._data['stackedpython'], np.array([1, 2.5]))
                np.testing.assert_array_equal(builder._data['stackedpypy'], np.array([8, 25]))
                np.testing.assert_array_equal(builder._data['stackedjython'], np.array([25, 60]))

            np.testing.assert_array_equal(builder._data['cat'], np.array(['0', '1']))
            np.testing.assert_array_equal(builder._data['width'], np.array([0.8, 0.8]))
            np.testing.assert_array_equal(builder._data['width_cat'], np.array([0.2, 0.2]))

        lvalues = [[2, 5], [12, 40], [22, 30]]
        for i, _xy in enumerate([lvalues, np.array(lvalues)]):
            bar = create_chart(Bar, _xy)
            builder = bar._builders[0]
            np.testing.assert_array_equal(builder._data['0'], np.array(lvalues[0]))
            np.testing.assert_array_equal(builder._data['1'], np.array(lvalues[1]))
            np.testing.assert_array_equal(builder._data['2'], np.array(lvalues[2]))

            # test mid values, that should always be y/2 ..
            np.testing.assert_array_equal(builder._data['mid0'], np.array([1, 2.5]))
            np.testing.assert_array_equal(builder._data['mid1'], np.array([6, 20]))
            np.testing.assert_array_equal(builder._data['mid2'], np.array([11, 15]))

            # stacked values should be 0 as base and + y/2 of the column
            np.testing.assert_array_equal(builder._data['stacked0'], np.array([1, 2.5]))
            np.testing.assert_array_equal(builder._data['stacked1'], np.array([8, 25]))
            np.testing.assert_array_equal(builder._data['stacked2'], np.array([25, 60]))

            np.testing.assert_array_equal(builder._data['cat'], np.array(['0', '1']))
            np.testing.assert_array_equal(builder._data['width'], np.array([0.8, 0.8]))
            np.testing.assert_array_equal(builder._data['width_cat'], np.array([0.2, 0.2]))

