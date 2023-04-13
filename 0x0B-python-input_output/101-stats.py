#!/usr/bin/python3

import sys

status_codes = {
    '200': 0,  # Keep track of occurrences of HTTP 200 status code
    '301': 0,  # Keep track of occurrences of HTTP 301 status code
    '400': 0,  # Keep track of occurrences of HTTP 400 status code
    '401': 0,  # Keep track of occurrences of HTTP 401 status code
    '403': 0,  # Keep track of occurrences of HTTP 403 status code
    '404': 0,  # Keep track of occurrences of HTTP 404 status code
    '405': 0,  # Keep track of occurrences of HTTP 405 status code
    '500': 0   # Keep track of occurrences of HTTP 500 status code
}

lc = 0  # Line counter
file_size = 0  # Total file size counter


def print_info():
    """
    Print file size and status code occurrences
    """
    print('File size: {:d}'.format(file_size))

    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {:d}'.format(scode, code_times))


try:
    for line in sys.stdin:
        if lc != 0 and lc % 10 == 0:
            print_info()

        pieces = line.split()

        try:
            status = int(pieces[-2])

            if str(status) in status_codes.keys():
                status_codes[str(status)] += 1
        except status:
            pass

        try:
            file_size += int(pieces[-1])
        except status:
            pass

        lc += 1

    print_info()
except KeyboardInterrupt:
    print_info()
    raise
