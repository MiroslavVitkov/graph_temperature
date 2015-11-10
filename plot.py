#!/usr/bin/env python

"""A colelction of classes for dynamically updated XY-plots.

"""

# Constants
MINUTE_S = 60
HOUR_S = MINUTE_S * 60
DAY_S = HOUR_S * 24
WEEK_S = DAY_S * 7
MONTH_S = DAY_S * 30
YEAR_S = DAY_S * 365


# Settings
MAX_TEMP = 60
MIN_TEMP = -10
TEMP_RANGE = MAX_TEMP - MIN_TEMP
TIME_INTERVALS = [MINUTE_S,
                  HOUR_S,
#                  DAY_S,
#                  WEEK_S,
#                  MONTH_S,
#                  YEAR_S,
                  ]

# Imports
import matplotlib.pyplot as plt
import collections as col
import numpy as np

class Demuxer(object):
    """Based on input temperature, update plots as needed"""
    def __init__(self, plots_spec):
        self.w = Window(plots_spec=plots_spec)
        self._counter_samples = 0

    def handle_new_value(self, val):
        """Update relevant plots."""
        self._counter_samples += 1

        # Update shortest interval plot. This always happens.
        self.w.add_datapoint(plot_number=0, y=val)

        # Calculate the impact of a new point on the averaging plots.
        # We skip the first plot, because it is already covered above.
        for i, v in enumerate(TIME_INTERVALS[:-1]):
            target_plot = i + 1
            if self._counter_samples % v == 0:
                avv_val = self._get_average(plot_num = target_plot - 1) # next shorter interval
                self.w.add_datapoint(plot_number=target_plot,
                                     y=avv_val)

    def _get_average(self, plot_num):
        data = self.w.get_yaxis(plot_num=plot_num)
        average = np.mean(data)
        return average

class Window(object):
    """Holds a collection of equally-sized, static x-axis, dynamic
     y-axis plots. Temperature range aware. Takes up the whole screen.

    """
    def __init__(self, plots_spec):
        """plots_spec - list of dicts:
            x_range, y_range, num_points

        """
        # Redraw plots as soon as self.fig.canvas.draw() is called.
        plt.ion()

        # Create the window surface
        dpi=80  # default value
        screen = get_screen_resolution()
        width = screen[0] / dpi
        height = screen[1] / dpi
        self.fig = plt.figure(figsize=(width, height), dpi=dpi)  # the main window

        # Create the individual plots
        self.plots = []
        plots_num = len(plots_spec)
        plots_map = 100 + plots_num * 10  # 234 means 2x3 grid, 4th subplot
        for i, p in enumerate(plots_spec):
            def get_axis(min, max, points):
                a = np.linspace(min, max, points)
                return [int(round(f)) for f in a]

            x_axis = get_axis(p['x_range'][0], p['x_range'][1], p['num_points'])
            y_axis = get_axis(p['y_range'][0], p['y_range'][1], p['num_points'])
            graph = Graph(window=self.fig, subplot_num=plots_map + i + 1,  # add last digit
                          x_axis=x_axis, y_axis=y_axis,
                          )
            self.plots.append(graph)

    # Redrawing belongs here for fine control over this time-consuming operation.
    # Note that fig.canvas.draw() redraws the whole window!
    def update_figure(self, plot_number, y_data):
        self.plots[plot_number].update_figure(y_data)
        self.fig.canvas.draw()

    def add_datapoint(self, plot_number, y):
        self.plots[plot_number].add_datapoint(y)
        self.fig.canvas.draw()

    def get_yaxis(self, plot_num):
        return self.plots[plot_num].y_data


class Graph(object):
    """Single 2-D dynamic plot. The axes must be same length and
    have both minimum and maximum possible values.

    """
    def __init__(self, window, subplot_num, x_axis, y_axis):
        # Draw self
        ax = window.add_subplot(subplot_num)

        # Obtain handle to y-axis
        line, = ax.plot(x_axis, y_axis) # set here axis ranges
        self.y = line

        # Remember list of datapoints
        self.y_data = col.deque(y_axis,
                                maxlen=len(y_axis))  # circular buffer

        # Make plot prettier
        plt.grid(True)
        plt.tight_layout()

    def update_figure(self, new_y_data):
        self.y_data = new_y_data
        self.y.set_ydata(self.y_data)  # pyPlot call

    def add_datapoint(self, y):
        self.y_data.append(y)  # remember - circular buffer
        self.y.set_ydata(self.y_data)


### General graphical utility calls. ###
def get_screen_resolution():
    """Returns current width, height in pixels."""
    return 1366, 768


def main():
    """Utility to smartly graph incoming stream of floats."""
    import sys
    DATAPOINTS_PER_GRAPH = 60
    PLOTS_SPEC = [dict(x_range=(0, d),
                       y_range=(MIN_TEMP, MAX_TEMP),
                       num_points=DATAPOINTS_PER_GRAPH)
                  for d in TIME_INTERVALS
                  ]

    d = Demuxer(plots_spec=PLOTS_SPEC)
    while True:
        value = sys.stdin.readline()
        d.handle_new_value(val=float(value))

if __name__ == "__main__":
    main()
