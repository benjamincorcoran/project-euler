#!/usr/bin/env python3
# Filename: problem_3.py
"""
Problem 3
Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import time

def sieve_primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve_section = sieve[i*i::2*i]
            sieve[i*i::2*i] = [False]*len(sieve_section)
    
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def problem_3():
    sqr_pr = int(600851475143**0.5) + 1
    for prime in sieve_primes(sqr_pr)[::-1]:
        if 600851475143%prime == 0:
            return prime

if __name__ == "__main__":
    start_time = time.time()
    result = problem_3()
    end_time = time.time()

    print(f"The answer is {result:,}.")
    print(f"The the solution took {end_time-start_time:0.2} seconds.")
