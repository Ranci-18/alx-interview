#!/usr/bin/python3
"""module to parse the logs and generate statistics"""
from sys import stdin
import re


def parse_logs_and_print_stats():
    """function to parse logs line by line
    and parse by status code and file size"""
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    file_size = 0
    counter = 0

    try:
        for logline in enumerate(stdin):
            try:
                counter += 1
                regex = r'/^([\d.]+) - \[([\d\- :.]+)\] "(.*?)" (\d+) (\d+)$/'
                match = re.search(regex, logline)
                if match:
                    file_size += int(match.group(5))
                    status_code = match.group(4)
                if status_code in status_codes:
                    status_codes[status_code] += 1
                if counter == 10:
                    print("File size: {}".format(file_size))
                    for key, value in sorted(status_codes.items()):
                        if value > 0:
                            print("{}: {}".format(key, value))
                    counter = 0
            except ValueError:
                continue
    except KeyboardInterrupt:
        print("File size: {}".format(file_size))
        for key, value in sorted(status_codes.items()):
            if value > 0:
                print("{}: {}".format(key, value))
