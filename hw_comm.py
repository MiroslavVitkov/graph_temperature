#!/usr/bin/env python

"""Receive line strings from device. Parse them and return numeric temperatures.

"""

import serial
import string
import sys

MAX_TEMP = 60
MIN_TEMP = -10
NEWLINE = "\n"

class Serial(object):
    """Serial duplex communication."""
    def __init__(self, clb):
        self.clb = clb  # callback for new available measurement
        self.comm = serial.Serial(port='/dev/ttyUSB0',
                                  baudrate=38400,  # 115200 is highest standard
                                  bytesize=serial.EIGHTBITS,
                                  parity=serial.PARITY_NONE,
                                  stopbits=serial.STOPBITS_ONE,
                                  timeout=None,  # None==forever,
                                                 # 0=non-blocking,
                                                 # float=seconds
                                  xonxoff=False,  # sw flow control
                                  rtscts=False,  # hw flow control
                                  writeTimeout=None,  # see 'timeout'
                                  dsrdtr=False,  # hw flow control
                                  interCharTimeout=None,
                                  )

    def listen_forever(self):
        """Blocking! Forever!"""
        def rl(size=None, eol=NEWLINE):
            """pyserial's implementation does not support the eol parameter"""
            ret = ""
            while True:
                x = self.comm.read()
                ret = ret + x
                if x == eol:
                    return ret
        self.comm.readline = rl
        while True:
            measurement = self.comm.readline()
            temp = self.parse_line_return_temp(measurement)
            if temp is not None:
                self.clb(temp)

    def _generate_random_data(self):
        """For debug purposes."""
        import random
        while True:
            measurement = str(random.randint(MIN_TEMP, MAX_TEMP)) + ".0"
            self.clb(measurement)

    def parse_line_return_temp(self, line):
        try:
            s1 = string.split(s=line, sep=' ')  # time decicelsius
            return (float(s1[1]) / 10 )
        except ValueError:
            return None


def main():
    def clb(x):
        print x
        sys.stdout.flush()
    comm = Serial(clb=clb)
    comm.listen_forever()

if __name__ == "__main__":
    main()
