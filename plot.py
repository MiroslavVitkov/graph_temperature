#!/bin/python

import matplotlib.pyplot as plt
import numpy as np

class Plot(object):
    def __init__(self, x_axis):
        self.x = x_axis
        self.y = None
        
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

    def update_fig(self, y):
        line1, = self.ax.plot(self.x, y, 'r-') # Returns a tuple of line objects, thus the comma
        for point in np.linspace(0, 10*np.pi, 500):
            line1.set_ydata(y)
            self.fig.canvas.draw()

