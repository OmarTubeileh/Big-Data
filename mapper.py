#!/usr/bin/env python3
import sys
import csv

def discretize_age(age):
    try:
        age = int(age)
        if age < 20:
            return 0  # 0-19
        elif age < 40:
            return 1  # 20-39
        elif age < 60:
            return 2  # 40-59
        else:
            return 3  # 60+
    except ValueError:
        return age

# Read header
header = True

for line in sys.stdin:
    if header:
        # Emit the header as-is
        print(line.strip())
        header = False
        continue

    # Parse CSV
    columns = line.strip().split(',')
    age = columns[0]  # Assuming age is in the first column
    discrete_age = discretize_age(age)

    # Output the rest of the line with the discretized age
    columns[0] = str(discrete_age)
    print(",".join(columns))