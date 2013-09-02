#!/usr/bin/env python

"""Output a number between 50.000 and -30.000 every second.
Pass a callback to MainManager

"""

import time
import random


class Simple(object):
    def __init__(self, clb):
        self.clb = clb

    def run(self):
        while True:
            time.sleep(1)  # one second
            new = random.randint(-20000, 50000)
            self.clb(new)
