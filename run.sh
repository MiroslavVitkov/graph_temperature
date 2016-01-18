#!/bin/bash
LOGFILE=/tmp/tempr_log

trap "kill -- -$$" EXIT           # Kill all children on exit.

stdbuf -o0 ./hw_comm.py --raw  > "$LOGFILE"  &  # Unbuffered logging.
tail -f "$LOGFILE" | ./plot.py               &
tail -f "$LOGFILE"
