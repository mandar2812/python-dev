#!/usr/bin/python
import csv
import sys

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False


f = open(sys.argv[1], 'rt')
w = open(sys.argv[2], 'wt')

try:
    reader = csv.reader(f)
    writer = csv.writer(w)
    for row in reader:
        row1 = map(lambda elem: elem if (not is_number(elem) or elem.isdigit()) else str(round(float(elem), 3)), row)
        writer.writerow(row1)
finally:
    f.close()
    w.close()

