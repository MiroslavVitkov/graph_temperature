#!/usr/bin/env python

"""Receive line strings from device. Parse them and return numeric temperatures.

"""

import serial
import string
import sys
import time

MAX_TEMP = 60
MIN_TEMP = 0
NEWLINE = "\n"

class Serial(object):
    """Serial duplex communication."""
    def __init__(self, raw=False, simulate=False):
        self.simulate = simulate
        self.raw = raw
        if not simulate:
            self.comm = serial.Serial(port='/dev/ttyUSB0',
                                      baudrate=38400,
                                      bytesize=serial.EIGHTBITS,
                                      parity=serial.PARITY_NONE,
                                      stopbits=serial.STOPBITS_ONE,
                                      timeout=None,
                                      xonxoff=False,
                                      rtscts=False,
                                      writeTimeout=None,
                                      dsrdtr=False,
                                      interCharTimeout=None,
                                      )

    def run(self):
        if self.simulate:
            self._generate_random_data()
        else:
            self._listen_forever()

    def _listen_forever(self):
        """Blocking! Forever!"""
        def rl(size=None, eol=NEWLINE):
            """pyserial's implementation does not support the eol parameter"""
            ret = ""
            while True:
                x = self.comm.read()
                if x == eol:
                    return ret
                ret = ret + x
        self.comm.readline = rl

        while True:
            measurement = self.comm.readline()
            if self.raw:
                print measurement
            else:
                temp = self._parse_line_return_temp(measurement)
                if temp is not None:
                    print temp[0], temp[1]

    def _generate_random_data(self):
        """For debug purposes."""
        import random
        while True:
            measurement = str(random.randint(MIN_TEMP, MAX_TEMP)) + ".0"
            print 0, measurement, float(measurement) / 2 # TODO: adapt _parse_line_return_temp()
            time.sleep(0.3)

    def _parse_line_return_temp(self, line):
        try:
            s1 = string.split(s=line, sep=' ')  # time decicelsius
            return (float(s1[1]) / 10), (float(s1[2]) / 10)
        except ValueError:
            return None


def main():
    import sys
    raw = False
    simulate = False
    for arg in sys.argv:
        if arg == '--raw':
            raw = True
        if arg == '--sim':
            simulate = True
    comm = Serial(raw=raw, simulate=simulate)
    comm.run()

if __name__ == "__main__":
    main()
