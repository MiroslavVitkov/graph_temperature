#!/bin/python

"""Convert between model coordinates(time, temperature) and view coordinates(pixels, pixels)."""

#from __future__ import division
#import numpy as np

def linscale_point(point, inrange, outrange):
    normalized = (point - inrange[0]) / inrange[1] - inrange[0]
    scaled = normalized * (outrange[1] - outrange[0])
    shifted = normalized - outrange[0]
    return shifted 

#def linscale_vector(in_vect, out_max):
#    in_max = np.max(in_vect)
#    in_norm = in_vect / in_max
#    scaled = in_norm * out_max
#    return int(round(scaled))

def temp2pixels(temp, temp_range, graph_height):
    return linscale_point(temp, temp_range, (0, graph_height))
    

def main():
    pass

if __name__ == "__main__":
    main()
