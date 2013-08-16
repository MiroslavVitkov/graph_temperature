#!/bin/python

import matplotlib.pyplot as plt

class Plot(object):
    def __init__(self, x_axis):
        self.x = x_axis
        self.y = None
        
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

    def update_fig(self, y):
        line1, = self.ax.plot(self.x, y, 'r-') # Returns a tuple of line objects, thus the comma
        for point in self.x:
            line1.set_ydata(y)
            self.fig.canvas.draw()


def main():
    """Unit test."""
    p = Plot(range(100))
    while True:
        p.update_fig(range(100))

if __name__ == "__main__":
    main()
