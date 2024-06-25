#!/usr/bin/python3
"""
log_parsing exercise
"""
import sys


codes = {}
i = 0
file_size = 0
try:
    for line in sys.stdin:
        # print(line)
        try:
            intel = line.split(" ")
            code = intel[-2]
            size = int(intel[-1])
            if len(code) == 3:
                code = int(code)
                codes[code] = codes.get(code, 0) + 1
                file_size += size
                i += 1
        except (IndexError, ValueError):
            pass
        if i == 10:
            print(f"File size: {file_size}")
            sorted_keys = sorted(codes.keys())
            for key in sorted_keys:
                print(f"{key}: {codes[key]}")
            i = 0
except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {file_size}")
    sorted_keys = sorted(codes.keys())
    for key in sorted_keys:
        print(f"{key}: {codes[key]}")
