#!/bin/python

"""Handle serial communication with the device and do callbacks.

"""

import serial


class Serial(object):
    """Serial duplex communication."""
    def __init__(self, clb):
        self.clb = clb  # callback for new available measurement
        self.comm = serial.Serial(port=0,
                                  baudrate=9600,
                                  bytesize=EIGHTBITS,
                                  parity=PARITY_NONE,
                                  stopbits=STOPBIT_ONE,
                                  timeout=None,
                                  xoxoff=False,  # sw flow control
                                  rtscts=False,  # hw flow control
                                  writeTimeout=None,
                                  dsrdtr=False,  # hw flow control
                                  interCharTimeout=None,
                                  )

    def run(self):
        measurement = 30000
        self.clb(measurement)

    def write(self, string, newline=True):
        comm.write(string)


def main():
    pass

if __name__ == "__main__":
    main()
