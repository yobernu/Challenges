# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(nums):
    # Write your code here
        diff = max(nums)
        lst = [0] * (100)
        for i in range(len(nums)):
            lst[nums[i]] += 1
        print(lst)
        return lst
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    nums = list(map(int, input().rstrip().split()))

    result = countingSort(nums)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
