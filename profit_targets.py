#!/bin/python

import math
import os
import random
import re
import sys

"""
Profit Targets

A financial analyst is managing a portfolio represented by an array of yearly profits, 
`stocksProfit`. The goal is to find the number of distinct pairs of stocks (profits) 
whose sum equals a given target profit. Distinct pairs are defined as pairs that 
differ in at least one element, meaning each pair should be unique.

Function:
The function `stockPairs(stocksProfit, target)` takes two parameters:
    - `stocksProfit`: an array of integers representing the yearly profits of stocks.
    - `target`: an integer representing the target profit for each pair.

The function should return an integer, which is the total number of distinct pairs 
where the sum of each pair’s profits is exactly equal to the target.

Example:
Input:
    stocksProfit = [5, 7, 9, 13, 11, 6, 6, 3, 3]
    target = 12

Output:
    3

Explanation:
    There are 3 distinct pairs with a sum of 12:
    - (5, 7)
    - (3, 9)
    - (6, 6)
Only unique pairs are counted, and each pair should only be counted once.
"""



#
# Complete the 'stockPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stocksProfit
#  2. LONG_INTEGER target
#

def stockPairs(stocksProfit, target):
    # Write your code here
    # don't include duplicates
    unique_pairs = set()
    tracked = set()
    
    for x in stocksProfit:
        # check diff 
        diff = target-x
        
        # if that diff has been tracked then it would be a unique pair
        if diff in tracked:
            pair = tuple(sorted((x,diff)))
            unique_pairs.add(pair)
            
        tracked.add(x)
    
    return len(unique_pairs)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stocksProfit_count = int(raw_input().strip())

    stocksProfit = []

    for _ in xrange(stocksProfit_count):
        stocksProfit_item = int(raw_input().strip())
        stocksProfit.append(stocksProfit_item)

    target = int(raw_input().strip())

    result = stockPairs(stocksProfit, target)

    fptr.write(str(result) + '\n')

    fptr.close()
