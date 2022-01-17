import math

def sum_divisors(n):
    """Returns a list containing the sum of divisors (including proper divisors) of all the numbers below n. 

    >>> sum_divisors(10) # https://oeis.org/A000203
    [0, 1, 3, 4, 7, 6, 12, 8, 15, 13] -- The list contain the sum of divisors of all the numbers from 0 to 9

    """
    result = [1] * n
    result[0] = 0
    for p in range(2, n):
        if result[p] == 1: # p is prime
            p_power, last_m = p, 1
            while p_power < n:
                m = last_m + p_power
                for i in range(p_power, n, p_power):
                    result[i] //= last_m    # (B)
                    result[i] *= m          # (B)
                last_m = m
                p_power *= p
    return result

"""The following function takes the modulus(a), reminder (r) and limit(n) and gives number of numbers less than n, whose 
sum of divisor is a perfect square and which leave reminder r when divided by a."""

def main_function(a, r, n):
    data_list = (sum_divisors(n))
    count = 0
    serial = 0
    for i in data_list:
        if math.sqrt(int(i)) == int(math.sqrt(int(i))) and serial % a == r:
            count = count + 1
        serial = serial + 1
    return count

print(main_function(5, 1, 1001))
