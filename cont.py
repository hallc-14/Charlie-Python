#!/usr/bin/env python3

i = 0

while i < 10:
    if i % 2 == 0:
        print( "Found an even number:", i)
        i += 1
        continue # continus with next iteration
    i += 1
