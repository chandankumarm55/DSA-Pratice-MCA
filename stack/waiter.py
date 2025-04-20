#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def waiter(number, q):
    # Function to generate the first q prime numbers
    def generate_primes(n):
        primes = []
        num = 2
        while len(primes) < n:
            is_prime = True
            for p in primes:
                if p * p > num:
                    break
                if num % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
            num += 1
        return primes

    result = []
    primes = generate_primes(q)
    A = number[::-1]  # Reverse the input to simulate stack behavior

    for i in range(q):
        prime = primes[i]
        A_next = []
        B = []

        # Process all plates in current A
        while A:
            plate = A.pop()
            if plate % prime == 0:
                B.append(plate)
            else:
                A_next.append(plate)

        # Add B (top to bottom) to result
        while B:
            result.append(B.pop())

        A = A_next

    # After q iterations, add remaining A stack (top to bottom)
    while A:
        result.append(A.pop())

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
