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
        self.next_node = next_node

        # File handle
        self.file = file
        self.file_mode = file_mode

        #TODO: Initialize all memoty to prevent memory allocation at runtime
        self.data = []

    def add(self, x):
        self.data.append(x)


class Logger(object):
    """Records measured data on the disc for later retrieval."""
    def __init__(self, workdir, backupdir=None):
        # fname = year_month
        # self.curr_month
        # create/open self.curr_file in workdir with name fname
        # if created, write header
        pass

    def add_line(string):
        # get system time, extract month
        # if self.curr_month != month call self.new_month
        # regardless, write string into self.curr_file
        pass

    def begin_new_month(self):
        """Package away the open logfile for the month,
        archive it and open a new file.

        """
        # generate footer: averages per week and for the whole month
        # close self.curr_file
        # arcive and save at self.backupdir

    def read_last_minute(self):
        measurements = []
        for i in X_MIN:
            measurements.append(0) # read from file, if end, read from previous
        return measurements

    def read_last_hour(self)
        measurements = []
        for i in range(0, HOUR_TO_SECONDS, MINUTE_TO_SECONDS):
            measurements.append(0)  # read one line in MINUTE_TO_SAMPLES
        return measurements

    def read(self, seconds_ago, seconds_increment)
        measurement = []
        for i in range(0, seconds_ado, seconds_increment):
            measurements.append(0)  # TODO: read one line from file, if end, read from previous
        return measurement

def main():
    pass

if __name__ == "__main__":
    main()  
