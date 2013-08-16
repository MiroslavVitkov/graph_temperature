#!/bin/python

from plot import Plot

x = range(100)
p = Plot(x_axis = x, width=256, height=256)
for i in range(1,10):
    y = [t / float(i) for t in x]
    p.update_fig
