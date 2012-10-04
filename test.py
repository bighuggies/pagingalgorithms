#!/usr/bin/env python

import sys
import random

if __name__ == '__main__':
    random.seed()

    if len(sys.argv) > 1:
        amount = int(sys.argv[1])
    else:
        amount = 12

    for i in xrange(amount):
        sys.stdout.write(str(random.randint(1, 9)))
