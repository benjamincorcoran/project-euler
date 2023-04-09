#!/usr/bin/env python3
# Filename: problem_4.py
"""
Problem 4
Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time
import heapq

def recursive_order(start, end):
    if end - start == 1:
        return (())

def is_palindrome(n):
    return str(n)[:3] == str(n)[3:][::-1]

def problem_4():




if __name__ == "__main__":
    start_time = time.time()
    result = problem_4()
    end_time = time.time()

    print(f"The answer is {result:,}.")
    print(f"The the solution took {end_time-start_time:0.2} seconds.")
