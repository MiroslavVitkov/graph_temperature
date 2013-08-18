#!/bin/python

"""Construct a visible plot, connecting the given set of points.
Coordinates are normalized.

"""

import matplotlib.pyplot as plt

PLOT_WIDTH = 640
PLOT_HEIGHT = 480

class Manager(object):
    """Hold pixel data.

    """    
    def __init__(self, x_axis):
        self.x_axis = x_axis
        self.p = Window(plots_num=(1, 1),
                        x_axis=self.x_axis,
                        plot_width=PLOT_WIDTH,
                        plot_height=PLOT_HEIGHT
                       )
        self.capacity = len(self.x_axis)
        self.next_y_index = 0
        self.y_axis = [None] * self.capacity

    def add_point(self, y):
        self.y_axis[self.next_y_index] = y
        self.next_y_index += 1
        assert self.next_y_index <= self.capacity, "Buffer overflow"
        self.p.update_figure(y_pixels=self.y_axis)

    def clear(self):
        self.y_axis = [None] * self.capacity
        self.next_y_index = 0
        self.p.update_figure(y_pixels=self.y_axis)


class Window(object):
    """Hold plot objects."""
    def __init__(self, plots_num, x_axis, plot_width, plot_height):
        self.x_axis=x_axis

        plt.ion()

        # Create the window space
        dpi=80  # default value
        size_x = (float(plot_width) / dpi) * plots_num[0]
        size_y = (float(plot_height) / dpi) * plots_num[1]
        self.fig = plt.figure(figsize=(size_x, size_y), dpi=dpi,
                                       facecolor=None, edgecolor=None,
                                       linewidth=0.0, frameon=None,
                                       subplotpars=None, tight_layout=None
                                      )

        # Create the individual plots        
        self.ax = self.fig.add_subplot(111)
        self.line1, = self.ax.plot(self.x_axis, self.x_axis)
        self.g = Graph(x_axis=self.x_axis, y_axis=self.line1, figure=self.fig)

    def update_figure(self, y_pixels):
        self.g.update_figure(y_pixels)
        #self.line1.set_ydata(y_pixels)
        #self.fig.canvas.draw()

class Graph(object):
    """Single 2-D dynamic plot."""
    def __init__(self, x_axis, y_axis, figure):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.fig = figure

    def update_figure(self, y_pixels):
        self.y_axis.set_ydata(y_pixels)
        self.fig.canvas.draw()

    def get_size(self):
        f = self.fig
        return (self.width, self.height)

def main():
    """Unit test."""
    if 0:
        p = View(x_axis=range(100), width=640, height=480)
        print "Graph window size is:", p.get_size()
        for i in range(1, 100):
            temps = [t / float(i) for t in range(100)]
            p.update_fig(temps)

    if 1:
        m = Manager(x_axis=range(100))
        for i in range(1, 5):
            print "Run", i
            for j in range(100):
                m.add_point(j / float(i))
            m.clear()

    if 0:
        m = Manager(x_axis=range(0, PLOT_WIDTH, 5))
        print "Graph window size is:", m.p.get_size()
        for i in range(1,5):
            for j in range(0, PLOT_HEIGHT, 5):
                m.add_point(j / float(i))
            m.clear()

if __name__ == "__main__":
    main()
