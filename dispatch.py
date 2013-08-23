#!/bin/python

"""Device -> hw_comm -> dispatch -> parse_com -> convert -> plot
                                 -> log

Update minute, hour and day plots every second.
Update week, month and year plots every day.

"""

import dummy_device as dev
import plot
import data
import converter as conv


DATAPOINTS_PER_GRAPH = 60


class MainManager(object):
    def __init__(self):
        # Initialize device communication
        self.device = dev.Simple(clb=self.handle_incoming_measurement)  # dummy device!!!

        # Record new temperatures here
        self.log = data.Logger(workdir="~")

        # Plots that depend on streamed data
        y = self.log.read(interval_seconds=60, step_seconds=1)
        self.p = plot.Manager(x_axis_static=conv.get_axis(DATAPOINTS_PER_GRAPH),
                              y_axis_initial=y,
                              )

    def handle_incoming_measurement(self, measurement):
        # Log
        self.log.add_line(measurement)

        # Draw
        self.p.add_point(measurement - conv.MIN_TEMP)  # scale [0, TEMP_RANGE]

    def load_initial(self):
        """After system reset, read previous logfiles and update plots.

        """
        y = self.log.read(interval_seconds=60,
                          step_seconds=1,
                          )
        self.p.set_yaxis(y)

    def run(self):
        self.device.run()


def main():
    import time
    if 0:
        m = MainManager()
        for i in range(1, 10):
            for j in range(0, 60):
                m.handle_incoming_measurement(j / float(i))
            m.handle_new_dataset()

    if 0:  # play random numbers through debug_device
        m = MainManager()
        m.device.run()

    if 1:  # restore data from logs
        m = MainManager()
        while 1:
            m.load_initial()
            time.sleep(10)

    if 0:  # Short-cirquit communication and feed plot and logs random data.
        m = MainManager()
        m.run()

if __name__ == "__main__":
    main()
