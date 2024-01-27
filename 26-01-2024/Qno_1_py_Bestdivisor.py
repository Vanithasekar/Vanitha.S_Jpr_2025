'''Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

Input Format

A single integer denoting .

Constraints

Output Format

Print an integer denoting the best divisor of .

Sample Input 0

12
Sample Output 0

6'''

import math
import os
import random
import re
import sys

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def best_divisor(n):
    best_div = 1
    max_sum_of_digits = 1

    for divisor in range(2, n + 1):
        if n % divisor == 0:
            current_sum_of_digits = sum_of_digits(divisor)
             
            if current_sum_of_digits > max_sum_of_digits:
                max_sum_of_digits = current_sum_of_digits
                best_div = divisor
           
            elif current_sum_of_digits == max_sum_of_digits and divisor < best_div:
                best_div = divisor

    return best_div
 
n = int(input())

 
result = best_divisor(n)
print(result)
