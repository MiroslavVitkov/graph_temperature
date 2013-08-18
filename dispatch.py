#!/bin/python

"""Device -> hw_comm -> dispatch -> parse_com -> convert -> plot
                                 -> parse_com -> log

"""

import dummy_device as dev
import plot
import data
import converter as conv


class MainManager(object):
    def __init__(self):
        # Initialize device communication
        self.s = dev.Simple(clb=self.handle_incoming_measurement)

        # Record new temperatures here
        self.y = []

        # Plots that depend on streamed data
        axis_one_minute = conv.seconds2pixels(time=range(60), time_range=(0, 60), graph_length=640)
        self.p = plot.Manager(x_axis=axis_one_minute)

    def handle_incoming_measurement(self, measurement):
        y = conv.temp2pixels(temp=measurement,
                             temp_range=(-20000, 50000),
                             graph_height=480)
        self.p.add_point(y)

    def handle_new_dataset(self):
        self.p.clear()

def main():
    if 0:
        m = MainManager()
        for i in range(1, 10):
            for j in range(0, 60):
                m.handle_incoming_measurement(j / float(i))
            m.handle_new_dataset()

    if 1:
        m = MainManager()
        m.s.run()

if __name__ == "__main__":
    main()
