#!/bin/python

"""Holds static x-axes for different ranges, as well as all the accumulated temperature data ever."""

# x axes in seconds for the different graphs
X_MIN = range(60)
X_HOUR = range(0, 60*60, 60)
X_DAY = range(0, 60*60*24, 60*60)
X_WEEK = range(0, 60*60*24*7, 60*60*24)
X_MONTH = range(0, 60*60*24*7*4, 60*60*24*7)
X_YEAR = range(0, 60*60*24*7*4*12, 60*60*24*7*4)

FNAME_LOG = "temperature_measurements"

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
    """Records measured data on the disc for later retrieval.

    Format is one line per second, appended at a large file.
    The file is periodically compressed and backed up, with
    previous archives being deleted.
    """
    def __init__(self, workdir, backupdir=None, backup_interval=None):
        # self.logfile = create/open FNAME_LOG
        pass

    def add_line(string):
        # measurement = format string into one line
        # self.logfile.append(measurement)
        pass

    def read(self, interval_seconds, step_seconds):
        measurement = []
        for i in range(0, interval_seconds, step_seconds):
            measurements.append(0)  # TODO
        return measurement


def main():
    pass

if __name__ == "__main__":
    main()  
