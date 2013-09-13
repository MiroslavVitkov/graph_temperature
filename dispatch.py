#!/usr/bin/env python

"""Device -> hw_comm -> dispatch -> plot
                                 -> log

Update minute, hour, day, week, month and year plots.

"""

import hw_comm as dev
import plot
import data
import threading
from os.path import expanduser  # find $HOME on any OS


# Logging settings
WORKDIR = expanduser('~')
BACKUPDIR = None

# Plotting settings
MINUTE_S = 60
HOUR_S = MINUTE_S * 60
DAY_S = HOUR_S * 24
WEEK_S = DAY_S * 7
MONTH_S = DAY_S * 30
YEAR_S = DAY_S * 365
TIME_INTERVALS = [MINUTE_S,
                  HOUR_S,
                  DAY_S,
                  WEEK_S,
                  MONTH_S,
                  YEAR_S,
                  ]

# temp_C * 10 ^ 3 -> temp_maxres
MAX_TEMP = 50000
MIN_TEMP = -30000
TEMP_RANGE = MAX_TEMP - MIN_TEMP

DATAPOINTS_PER_GRAPH = 60
PLOTS_SPEC = [dict(x_range=(0, d),
                   y_range=(MIN_TEMP, MAX_TEMP),
                   num_points=DATAPOINTS_PER_GRAPH)
              for d in TIME_INTERVALS
              ]


class MainManager(object):
    def __init__(self):
        # Initialize device communication
        def listen_to_port():
            device = dev.Serial(clb=self.handle_incoming_measurement)
            #device.listen_forever()  # TODO: uncomment for production code
            device._generate_random_data()
        self.device_thread = threading.Thread(target=listen_to_port, args=(), kwargs={})

        # Record new temperatures here
        self.log = data.Logger(workdir=WORKDIR, backupdir=BACKUPDIR)

        # Plots that depend on streamed data
        self.plots = plot.Window(plots_spec=PLOTS_SPEC)

        # Scratchpad
        self._counter_samples = 0

    def handle_incoming_measurement(self, measurement):
        # Log
        self.log.add_line(measurement)

        # Draw
        # 1. parse
        import random
        parsed_measurement = random.randint(-30000, 50000)

        # 2. update corresponding plots
        self._counter_samples += 1
        for p, v in enumerate(TIME_INTERVALS):
            if self._counter_samples % v == 0:
                self.plots.add_datapoint(plot_number=p,
                                 y=parsed_measurement,
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
