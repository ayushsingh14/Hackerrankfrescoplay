#!/bin/python3

import math
import os
import random
import re
import sys


import itertools

#
# Complete the 'usingiter' function below.
#
# The function is expected to return a TUPLE.
# The function accepts following parameters:
#  1. TUPLE tupb
#

def performIterator(tuplevalues):
    a=[]
    u=[]
    count=0
    print(len(tuplevalues[0]))
    for i in itertools.cycle(tuplevalues[0]):  
        if count>=4:  
            break
        else:  
            u.append(i)  
            count += 1
    a.append(tuple(u))
    c=tuplevalues[1][0]
    d=tuple((itertools.repeat(c,len(tuplevalues[1]))))
    a.append(d)
    e=tuple(itertools.accumulate(tuplevalues[2]))
    a.append(e)
    f=tuple(itertools.chain.from_iterable(tuplevalues))
    a.append(f)
    g=tuple(itertools.filterfalse(lambda x : x % 2 == 0,f))
    a.append(g)
    return tuple(a)


if __name__ == '__main__':

    length = int(input().strip())

    qw1 = []
    for i in range(4):
        qw2 = []
        for _ in range(length):
            qw2_item = int(input().strip())
            qw2.append(qw2_item)
        qw1.append(tuple(qw2))
    tupb = tuple(qw1)

    q = performIterator(tupb)
    print(q)
