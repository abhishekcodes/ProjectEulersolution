# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 15:53:04 2019

@author: Durgesh

count = 0
n = 1
while n>=0:
    for i in range(i,n):
        if n%i == 0:
            n+=1
            continue
        else:
            if count == 10:
                print(n)
            else:
                count+=1
                
  """

import pytest
from math import log, ceil

def find_primes(limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False

    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False

def upper_bound_for_p_n(n):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))

"""def find_n_prime(n):
    primes = list(find_primes(upper_bound_for_p_n(n)))
    return primes[n - 1]"""




from itertools import islice

def find_n_prime(n):
    primes = find_primes(upper_bound_for_p_n(n))
    return next(islice(primes, n - 1, n))

a = find_n_prime(10001)
  