#!/bin/python

"""Construct a visible plot, connecting the given set of points.
Coordinates are normalized.

"""

import matplotlib.pyplot as plt
import collections as col


WINDOW_WIDTH = 300
WINDOW_HEIGHT = 20
PLOT_WIDTH = 300
PLOT_HEIGHT = 200

class Manager(object):
    """Hold pixel data. Refresh plots when needed.

    """
    def __init__(self, x_axis_static, y_axis_initial):
        self.x_axis = x_axis_static
        self.y_axis = col.deque(y_axis_initial,           # circular buffer
                                maxlen=len(x_axis_static)
                                )
        self.p = Window(plots_num=(3, 2),
                        x_axis=self.x_axis,
                        plot_width=PLOT_WIDTH,
                        plot_height=PLOT_HEIGHT
                       )

    def add_point(self, y):
        self.y_axis.append(y)  # remember: circula buffer
        self.p.update_figure(fig_number=0, y_axis=self.y_axis)


class Window(object):
    """Hold plot objects."""
    def __init__(self, plots_num, x_axis, plot_width, plot_height):
        # Horizontal axis for every and all plots.
        self.x_axis=x_axis

        # Redraw plots as soon as self.fig.canvas.draw() is called.
        plt.ion()

        # Create the window surface
        dpi=80  # default value
        size_x = (float(plot_width) / dpi) * plots_num[0]
        size_y = (float(plot_height) / dpi) * plots_num[1]
        self.fig = plt.figure(figsize=(size_x, size_y), dpi=dpi,  # the main window
                              facecolor=None, edgecolor=None,
                              linewidth=.0, frameon=None,
                              subplotpars=None, tight_layout=None
                              )

        # Create the individual plots
        def _create_plot(subplot):
            ax = self.fig.add_subplot(subplot)
            line, = ax.plot(self.x_axis, self.x_axis)
            graph = Graph(y_axis=line, figure=self.fig)
            return graph
        assert plots_num[0] <= 9, "Number of plots must be a single digit!"
        assert plots_num[1] <= 9, "Number of plots must be a single digit!"
        self.plots = []
        plots_map = plots_num[0] * 100 + plots_num[1] * 10  # 990 to 110, 0 is the current plot
        for i in range(0, plots_num[0]):
            for j in range(1, plots_num[1] + 1):
                p = _create_plot(plots_map + i*plots_num[1] + j)  # form the last difit i.e. current plot number
                self.plots.append(p)

    def update_figure(self, fig_number, y_axis):
        for p in self.plots:
            p.update_figure(y_axis)


class Graph(object):
    """Single 2-D dynamic plot."""
    def __init__(self, y_axis, figure):
        self.y_axis = y_axis
        self.fig = figure

    def update_figure(self, y_pixels):
        self.y_axis.set_ydata(y_pixels)
        self.fig.canvas.draw()

    def get_size(self):  # WARN: this is wrong, it returns the size of the whole window
        f = self.fig
        return (self.width, self.height)

def main():
    """Unit test."""
    if 0:
        p = Graph(x_axis=range(100), width=640, height=480)
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
