#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    ip_address = '{:d}.{:d}.{:d}.{:d}'.format(random.randint(1, 255), random.randint(1, 255),
                                              random.randint(1, 255), random.randint(1, 255))
    date = datetime.datetime.now()
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    file_size = random.randint(1, 1024)
    sys.stdout.write('{} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n'.format(ip_address, date, status_code, file_size))
    sys.stdout.flush()
    sleep(random.random())
