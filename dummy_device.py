#!/bin/python

"""Output a number between 50.000 and -30.000 every second.
Pass a callback to MainManager

"""

import time
import random
from upper_management import MainManager


m = MainManager()
while $(true):
    time.sleep(1)  # one second
    new = random.randint(-30000, 50000)
    m.incoming_data(new)
