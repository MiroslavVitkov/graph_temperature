#!/usr/bin/env python

"""Handle serial communication with the device and do callbacks.

"""

import serial


class Serial(object):
    """Serial duplex communication."""
    def __init__(self, clb):
        self.clb = clb  # callback for new available measurement
        self.comm = serial.Serial(port='/dev/ttyUSB0',
                                  baudrate=9600,
                                  bytesize=serial.EIGHTBITS,
                                  parity=serial.PARITY_NONE,
                                  stopbits=serial.STOPBITS_ONE,
                                  timeout=None,
                                  xonxoff=False,  # sw flow control
                                  rtscts=False,  # hw flow control
                                  writeTimeout=None,
                                  dsrdtr=False,  # hw flow control
                                  interCharTimeout=None,
                                  )

    def run(self):
        while True:
            print "yey"
            import random
            measurement = random.randint(-20000, 50000)
            #measurement = self.comm.readline()  # blocking
            self.clb(measurement)

    def read_line(self):
        self.comm.read()

    def write(self, string, newline=True):
        comm.write(string)


def main():
    pass

if __name__ == "__main__":
    main()
