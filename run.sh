#!/bin/bash
LOGFILE=/tmp/tempr_log

trap "kill -- -$$" EXIT           # Kill all children on exit.

./hw_comm.py > "$LOGFILE"      &  #  This locks the port, you can't minicom it at the same time.
tail -f "$LOGFILE" | ./plot.py &
tail -f "$LOGFILE"
