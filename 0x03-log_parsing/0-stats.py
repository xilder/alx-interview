#!/usr/bin/env python3
"""
log_parsing exercise
"""
import re
import sys


def print_log(codes, file_size):
    """prints log stored"""
    print(f"File size: {file_size}")
    for code, freq in codes.items():
        print(f"{code}: {freq}")


def parse_log():
    """parses log from stdin"""
    codes = {}
    i = 0
    file_size = 0
    try:
        for line in sys.stdin:
            i += 1
            intel = line.split(" ")
            try:
                code = (intel[-2])
                size = int(intel[-1])
                if len(code) == 3:
                    code = int(code)
                    codes[code] = codes.get(code, 0) + 1
                    file_size += int(size)
            except (IndexError, ValueError):
                pass
            if i == 10:
                print_log(codes, file_size)
                i = 0
    except KeyboardInterrupt:
        print_log(codes, file_size)


if __name__ == "__main__":
    parse_log()
