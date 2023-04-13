#!/usr/bin/python3

import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())  # Add random delay to simulate web server traffic
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),  # Add current timestamp for log entry
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),  # Generate random HTTP response code
        random.randint(1, 1024)  # Generate random response size
    ))
    sys.stdout.flush()  # Flush the log entry to stdout for immediate display
