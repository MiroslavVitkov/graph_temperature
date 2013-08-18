#!/bin/python

"""Convert between model coordinates(time, temperature) and view coordinates(pixels, pixels)."""

import collections as col


def linscale(point, inrange, outrange):
    normalized = (point - inrange[0]) / float((inrange[1] - inrange[0]))
    scaled = normalized * (outrange[1] - outrange[0])
    shifted = scaled - outrange[0]
    return shifted

def temp2pixels(temp, temp_range, graph_height):
    p = linscale(temp, temp_range, (0, graph_height))
    pix = int(round(pix))
    return pix

def seconds2pixels(time, time_range, graph_length):
    if isinstance(time, col.Iterable):
        pix = []
        for t in time:
            p = linscale(t, time_range, (0, graph_length))
            pix.append(int(round(p)))
    else:
        p = linscale(time, time_range, (0, graph_lenght))
        pix = int(round(p))
    return pix

def int2maxres(x):
    """maxres is one of the sensor's native representations.
    maxres(3.1514) = 3151

    """
    def conv_single_val(v):
        return v * 100
    if isinstance(x, col.Iterable):
        ret = []
        for i in x:
            r = int(conv_single_val(i))
            ret.append(r)
    else:
        ret = conv_single_val(x)
    return ret

def maxres2float(x):
    """See int2maxres()."""
    return x / float(100)


def main():
    pass

if __name__ == "__main__":
    main()
