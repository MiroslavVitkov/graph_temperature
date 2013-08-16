#!/bin/python

"""Holds static x-axes for different ranges, as well as all the accumulated temperature data ever."""

# x axes in seconds for the different graphs
X_MIN = range(60)
X_HOUR = range(0, 60*60, 60)
X_DAY = range(0, 60*60*24, 60*60)
X_WEEK = range(0, 60*60*24*7, 60*60*24)
X_MONTH = range(0, 60*60*24*7*4, 60*60*24*7)
X_YEAR = range(0, 60*60*24*7*4*12, 60*60*24*7*4)

class Node(object):
    """General data structuring node. Can be associated with a file in r/rw/w/None way.

    """
    def __init__(self, datapoints, prev_node=None, next_node=None, file=None, file_mode=None):
        # Doubly linked list
        self.prev_node = prev_node
        self,next_node = next_node

        # File handle
        self.file = file
        self.file_mode = file_mode

        # Initialize all memoty to prevent memory allocation at runtime
        self.temperatures = [0, ] * datapoints


def main():
    pass

if __name__ == "__main__":
    main()  
