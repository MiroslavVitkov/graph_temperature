#!/bin/python

"""Convert between model coordinates(time, temperature) and view coordinates(pixels, pixels)."""

import collections as col

def linscale(point, inrange, outrange):
    normalized = (point - inrange[0]) / float((inrange[1] - inrange[0]))
    scaled = normalized * (outrange[1] - outrange[0])
    shifted = scaled - outrange[0]
    return shifted

def normalize(point, max):
    return point / float(max)

def temp2pixels(temp, temp_range, graph_height):
    #p = linscale(temp, temp_range, (0, graph_height))
    #pix = int(round(pix))
    pix = normalize(temp - temp_range[0], temp_range[1] - temp_range[0])
    return pix

def seconds2pixels(time, time_range, graph_length):
    if isinstance(time, col.Iterable):
        pix = []
        for t in time:
            #p = linscale(t, time_range, (0, graph_length))
            #pix.append(int(round(p)))
            pix.append(normalize(t - time_range[0], time_range[1] - time_range[0]))
    else:
        #p = linscale(time, time_range, (0, graph_lenght))
        #pix = int(round(p))
        pix = normalize(time - time_range[0], time_range[1] - time_range[0])
    return pix


def main():
    pass

if __name__ == "__main__":
    main()
