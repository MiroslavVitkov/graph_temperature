#!/bin/python

"""Construct a visible plot, connecting the given set of points.
Coordiantes are measured in pixels.

"""

import matplotlib.pyplot as plt

class Dynamic(object):
    def __init__(self, x_axis, width, height):
        self.x = x_axis
        self.y = None

        plt.ion()

        dpi=80  # default value
        size_x = float(width) / dpi
        size_y = float(height) / dpi
        self.fig = plt.figure(figsize=(size_x, size_y), dpi=dpi,
                                       facecolor=None, edgecolor=None,
                                       linewidth=0.0, frameon=None,
                                       subplotpars=None, tight_layout=None)
        self.ax = self.fig.add_subplot(111)

        f = self.fig
        self.width = f.get_figwidth() * dpi
        self.height = f.get_figheight() * dpi

        self.line1, = self.ax.plot(self.x, self.x, 'r-') # Returns a tuple of line objects, thus the comma

    def update_fig(self, y_pixels):
        self.line1.set_ydata(y)
        self.fig.canvas.draw()

    def getsize(self):
        f = self.fig
        return dict(width=self.width, height=self.height)

def main():
    """Unit test."""
    p = Dynamic(x_axis=range(100), width=640, height=480)
    print "Graph window size is:", p.getsize()
    for i in range(1, 100):
        temps = [t / float(i) for t in range(100)]
        p.update_fig(temps)

if __name__ == "__main__":
    main()
