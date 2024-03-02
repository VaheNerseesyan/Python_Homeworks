"""
    !! In my code i have used Black formatter !!
"""
# Task 1
"""
Basics of Lambda: Create a lambda function that multiplies any number by 10.
"""
mul = lambda num: num * 10
print(mul(3))  # -> this can be input too ... mul(int(input"Input num: "))


# Task 2
"""
Using Map: Given a list of integers, use map() to double each number in the
list.
"""
print(list(map(lambda x: x * 2, [1, 2, 3, 4, 5])))


# Task 3
"""
Using Filter: Given a list of numbers, use filter() to extract all the even
numbers.
"""
print(list(filter(lambda x: x % 2 == 0, [1, 3, 55, 4, 2, 34, 5, 6, 7,]))) 


# Task 4
"""
Using Reduce: Use reduce() to find the product of all numbers in a given list.
"""
from functools import reduce


def product(a, b):
    c = a * b
    return c


print(reduce(product, [1, 2, 3, 4, 5]))


# Task 5
"""
Custom Function: Write a function named is_prime that determines if a number
is prime. Use this function with filter() to extract prime numbers from a list.
"""
import math


def is_prime(num):
    if num % 2 == 0:
        return False
    if num == 3:
        return True
    #             ⬇️  this must be grather than 1
    for i in range(2, num // 2):
        """              ^^^ How can here be the other way, (num // math.floor(num**(1/2))) , because the smallest num after 2, that
                        we can devide is the root of num
        """
        if num % i == 0:
            return False
    return True


print(list(filter(is_prime, [0, 1, 2, 3, 4, 27, 11, 9, 19, 21])))
print("Vahe")