#!/bin/python

"""Construct a visible plot, connecting the given set of points.
Coordinates are normalized.

"""

import matplotlib.pyplot as plt
import collections as col
from converter import MAX_TEMP, MIN_TEMP


class Window(object):
    """Holds a colelction of equally-sized, static x-axis, dynamic
     y-axis plots.

    """
    def __init__(self, plots_spec, per_plot_width, per_plot_height):
        """plots_spec - a list of dictionaries, each describing a plot:
            interval_s, step_s - characterize the x-axis, seconds
            y_initial - datapoints in model coordinates (seconds)

        """
        # Redraw plots as soon as self.fig.canvas.draw() is called.
        plt.ion()

        # Create the window surface
        dpi=80  # default value
        screen = get_screen_resolution()
        width = screen[0] / dpi
        height = screen[1] / dpi
        self.fig = plt.figure(figsize=(width, height), dpi=dpi,  # the main window
                              facecolor=None, edgecolor=None,
                              linewidth=.0, frameon=None,
                              subplotpars=None, tight_layout=None
                              )

        # Create the individual plots
        self.plots = []
        plots_num = len(plots_spec)
        plots_map = plots_num * 100 + 10  # 990 to 110, 0 is the current plot
        i = 1
        for p in plots_spec:
            # Construct x_axis. Pyplot normalizes (x, y).
            # Furthermore, integers are much faster than floats.
            # Therefore, work in the model domain:
            # degrees Celsius * 10 ^ 3 -> maxres values
            num_points = len(p['y_initial'])
            temp_range = MAX_TEMP - MIN_TEMP
            x_axis = range(0, temp_range, temp_range / num_points)
            while len(x_axis) > num_points:
                x_axis = x_axis[0:-1]

            graph = Graph(window=self.fig, subplot_num=plots_map + i,  # add last digit
                          x_data=x_axis, y_data=p['y_initial'],
                          )
            self.plots.append(graph)
            i += 1

    # Redrawing belongs here for fine control over his time-consuming operation.
    # Note that fig.canvas.draw() redwars the wholewindow!
    def update_figure(self, plot_number, y_data):
        self.plots[fig_number].update_figure(y_data)
        self.fig.canvas.draw()

    def add_datapoint(self, plot_number, y):
        self.plots[plot_number].add_datapoint(y - MIN_TEMP)
        self.fig.canvas.draw()


class Graph(object):
    """Single 2-D dynamic plot."""
    def __init__(self, window, subplot_num, x_data, y_data):
        # Draw self
        ax = window.add_subplot(subplot_num)

        # Obtain handle to y-axis
        line, = ax.plot(x_data, y_data)
        self.y = line

        # Remember list of datapoints
        self.y_data = col.deque(y_data,           # circular buffer
                                maxlen=len(x_data)
                                )
        self.x_data = list(x_data)

    def update_figure(self, new_y_data):
        self.y_data = new_y_data
        self.y.set_ydata(self.y_data)  # Qt call

    def add_datapoint(self, y):
        self.y_data.append(y)  # remember - circular buffer
        self.y.set_ydata(self.y_data)


### General graphical utility calls. ###
def get_screen_resolution():
    """Returns current width, height in pixels."""
    return 1366, 768


def main():
    if 1:
        """Test just Graph class."""
        plt.ion()
        fig = plt.figure(figsize=(15,9))
        temp_range = (MAX_TEMP - MIN_TEMP)
        p = Graph(window=fig, subplot_num=111,
                  x_data=range(0, temp_range, 1000), y_data=range(0, temp_range, 1000)
                  )
        for j in range(1, 5):
            print "Runt", j
            for i in range(0, 32768, 1000):
                p.add_datapoint(i)
                fig.canvas.draw()

    if 0:
        """Test whole window."""
        import converter as conv
        import random
        DATAPOINTS_PER_GRAPH = 60
        plots = [dict(interval_seconds=d,
                 step_seconds=d/DATAPOINTS_PER_GRAPH,
                 y_initial=[0,] * 97)
                 for d in conv.TIME_INTERVALS
                 ]


        w = Window(plots_spec=plots,
                   per_plot_width=200, per_plot_height=150
                   )
        for i in range(1, 5):
            print "Run", i
            for p in range(len(plots)):
                w.add_datapoint(plot_number=p, y=random.randint(MIN_TEMP, MAX_TEMP))


if __name__ == "__main__":
    main()
