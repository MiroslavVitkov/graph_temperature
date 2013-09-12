#!/usr/bin/env python
"""Holds static x-axes for different ranges, as well as all the accumulated temperature data ever."""

FNAME_LOG = "temperature_measurements.log"


class Logger(object):
    """Records measured data on the disc for later retrieval.

    Format is one line per second, appended at a large file.
    The file is periodically compressed and backed up, with
    previous archives being deleted.
    """
    def __init__(self, workdir, backupdir=None, backup_interval=None):
        # self.logfile = create/open FNAME_LOG
        pass

    def add_line(self, string):
        # measurement = format string into one line
        # self.logfile.append(measurement)
        pass

    def read(self, interval_seconds, step_seconds):
        return [10000] * interval_seconds
        measurements = []
        for i in range(0, interval_seconds, step_seconds):
            measurements.append(0)  # TODO
        return measurements


def main():
    pass

if __name__ == "__main__":
    main()
