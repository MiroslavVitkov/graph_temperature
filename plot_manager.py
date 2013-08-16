#!/bin/python

"""Update plot with new pixel point.

"""

import plot
import data


class PlotManager(object, x_axis):
    def __init__(self):
        self.x = x_axis
        self.p = plot.Dynamic(x_axis=self.x, width=255, height=123)
        self.y = data.Node(datapoints=len(x))

    def notify_new_datapoint(self, y_pixels):
        self.y.add(y_pixels)
        self.p.update_figure(y=self.y)
