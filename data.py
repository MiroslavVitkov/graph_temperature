#!/bin/python

import numpy as np

XAXIS = range(100)  # seconds

import math
y = np.sin(XAXIS)
from plot import Plot
p = Plot(XAXIS)
p.update_fig(y)
 
