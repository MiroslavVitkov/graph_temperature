#!/usr/bin/env python

"""Device -> hw_comm -> dispatch -> parse_com -> convert -> plot
                                 -> log

Update minute, hour and day plots every second.
Update week, month and year plots every day.

"""

import hw_comm as dev
import plot
import data
import converter as conv
import threading


DATAPOINTS_PER_GRAPH = 60
WORKDIR = "~"
BACKUPDIR = None
PLOTS_SPEC = [dict(x_range=(0, d),
                   y_range=(conv.MIN_TEMP, conv.MAX_TEMP),
                   num_points=DATAPOINTS_PER_GRAPH)
              for d in conv.TIME_INTERVALS
              ]


class MainManager(object):
    def __init__(self):
        # Initialize device communication
        def listen_to_port():
            device = dev.Serial(clb=self.handle_incoming_measurement)
            device.listen_forever()
        self.device_thread = threading.Thread(target=listen_to_port, args=(), kwargs={})

        # Record new temperatures here
        self.log = data.Logger(workdir=WORKDIR, backupdir=BACKUPDIR)

        # Plots that depend on streamed data
        self.plots = plot.Window(plots_spec=PLOTS_SPEC)

        # Time-consuming setup done. Lounch program loop!
        #self.device_thread.run()  # blocking!

    def handle_incoming_measurement(self, measurement):
        # Log
        self.log.add_line(measurement)

        # Draw
        self.plots.add_datapoint(plot_number=0,
                                 y=measurement,
                                 )

    def load_initial(self):
        """After system reset, read previous logfiles and update plots.

        """
        y = self.log.read(interval_seconds=60,
                          step_seconds=1,
                          )
        self.plots.update_figure(plot_number=0, y_data=y)

    def run(self):
        self.device_thread.start()


def main():
    if 1:  # play random numbers through debug_device
        m = MainManager()
        m.run()

    if 0:  # restore data from logs
        import time
        m = MainManager()
        m.load_initial()
        time.sleep(10)

if __name__ == "__main__":
    main()
