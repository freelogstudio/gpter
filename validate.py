import jsonlines
import sys

with jsonlines.open(sys.argv[1]) as f:
    for it in enumerate(f._fp, 1):
        print('line')

