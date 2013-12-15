#!/usr/bin/env python

"""Receive line strings from device. Parse them and return numeric temperatures.

"""

import serial
import string


class Serial(object):
    """Serial duplex communication."""
    def __init__(self, clb):
        self.clb = clb  # callback for new available measurement
        self.comm = serial.Serial(port='/dev/ttyUSB0',
                                  baudrate=38400,  # 115200 is highest standard
                                  bytesize=serial.EIGHTBITS,
                                  parity=serial.PARITY_EVEN,
                                  stopbits=serial.STOPBITS_TWO,
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
        def rl(size=None, eol="\n"):
            """pyserial's implementation does not support the eol parameter"""
            ret = ""
            while True:
                x = self.comm.read()
                ret = ret + x
                if x == eol:
                    return ret
        self.comm.readline = rl
        while True:
            measurement = self.comm.readline(size=None, eol="\r")
            temp = self.parse_line_return_temp(measurement)
            self.clb(temp)

    def _generate_random_data(self):
        """For debug purposes."""
        import random
        while True:
            measurement = str(random.randint(-30000, 50000)) + "\n"
            self.clb(measurement)

    def parse_line_return_temp(self, line):
        """sample input:
        Measured temperature: 7678;   converted temp: +13.8750; Relay control output: 1
        sample output (as float):
        13.8750   
        """
        s1 = string.split(s=line, sep=':')
        s2 = string.split(s=s1[2], sep=';')
        return float(s2[0])


def main():
    def clb(x): print x
    comm = Serial(clb=clb)
    comm.listen_forever()

if __name__ == "__main__":
    main()
