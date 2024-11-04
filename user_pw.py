#!/bin/python

import math
import os
import random
import re
import sys

"""
User-Friendly Password System

This program implements an authentication system that accepts a password 
if it matches the exact password set or if it matches the password with 
a single additional character appended to the end.

Hashing Function:
The system uses a specific hashing function defined as:
    h(s) = (s[0]*p^(n-1) + s[1]*p^(n-2) + ... + s[n-2]*p + s[n-1]) mod M

where:
    - `f(x)` is the ASCII value of character `x`
    - `p = 131`
    - `M = 10^9 + 7`

Example:
If the password `s` is `"cAr1"`, then:
    h(s) = (f('c')*131^3 + f('A')*131^2 + f('r')*131 + f('1')) mod 10^9 + 7
         = (99 * 131^3 + 65 * 131^2 + 114 * 131 + 49) mod 10^9 + 7
         = 223691457

Event Types:
1. setPassword(s): Sets the current password to `s`.
2. authorize(x): Checks if `x` matches the hash of the current password or the 
   hash of the current password with any single character appended. Returns `1` 
   if authorized, otherwise returns `0`.
"""


#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#
def hashing(s):
    chars = [char for char in s]
    p = 131
    M=10**9 + 7
    n = len(s)
    h = 0
    
    for i in range(n):
        # get ascii of char
        h = h + ord(chars[i])*p**(n-1-i)

    return h%M
    
def authEvents(events):
    results=[]
    s=''
    authorized=False
    
    for event in events:
        event_type = event[0]
        param = str(event[1])
        
        if event_type == 'setPassword':
            s = param
            continue
            
        if event_type == 'authorize':
            # get the hash of current password
            auth_hash = hashing(s)
            param = int(param)
            
            # if hash matches parameter, return 1
            if param == auth_hash:
                results.append(1)
                authorized=True
                continue
            
            authorized=False
            # hash of pw with a single character 
            for i in range(128):
                # chr() gets char of ascii value
                new = s + chr(i)
                if param == hashing(new):
                    results.append(1)
                    authorized=True
                    break
            
            if not authorized:
                results.append(0)
    return results
                
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    events_rows = int(raw_input().strip())
    events_columns = int(raw_input().strip())

    events = []

    for _ in xrange(events_rows):
        events.append(raw_input().rstrip().split())

    result = authEvents(events)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
