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
print(
    list(
        filter(
            lambda x: x % 2 == 0,
            [
                1,
                3,
                55,
                4,
                2,
                34,
                5,
                6,
                7,
            ],
        )
    )
)


# Task 4
"""
Using Reduce: Use reduce() to find the product of all numbers in a given list.
"""
from functools import reduce


def product(a: int, b: int):
    c = a * b
    return c


print(reduce(product, [1, 2, 3, 4, 5]))


# Task 5
"""
Custom Function: Write a function named is_prime that determines if a number
is prime. Use this function with filter() to extract prime numbers from a list.
"""
from typing import List
import math


def is_prime(nums: List[int]) -> list:
    """
    . Checking the nums, too see are there nums that are divisible by 2, and the negative numbers
    . With for loop check the divisions from 2, to the half of the num, or the root of the num
    . Return True if the num is Prime, or False if not
    """
    if nums % 2 == 0 or nums == 2 or nums <= 0:
        return False
    #             ⬇️  this must be grather than 1
    for i in range(2, nums // 2):
        """^^^ Here can be the other way, (num // math.floor(num**(1/2))) , because the smallest num after 2, that
        we can devide is the root of num
        """
        if nums % i == 0:
            return False
    return True


print(list(filter(is_prime, [0, 1, -3, 3, 4, 27, 11, 9, 19, 21])))

# Task 6
"""
Combining Map & Filter: Given a list of numbers, first filter out the even
numbers and then square them using map().
"""

print(
    list(map(lambda a: a**2, filter(lambda b: b % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
)


# Task 7
"""
Write a python function to create a simple Calculator.
"""


def calculator(num1: int, operation: str, num2: int):
    """
    . Getting the numbers and checking operation
    . Return the simple calculating
    """
    if operation == "+":
        return f"{num1} + {num2} = {num1+num2}"
    elif operation == "-":
        return f"{num1} - {num2} = {num1-num2}"
    elif operation == "*":
        return f"{num1} * {num2} = {num1*num2}"
    elif operation == "/":
        return f"{num1} / {num2} = {num1/num2}"


num1 = int(input("Input the first number: "))
op = input("Input operation (+ or - or * or /): ")
num2 = int(input("Input the second number: "))
print(calculator(num1, op, num2))


# Task 8
"""
Write a python function to find max of two numbers.
"""


def max_num(num1: int, num2: int):
    """
    . Checking is the nums are equal or not
    """
    if num1 > num2:
        return f"{num1} Is the max."
    elif num1 == num2:
        return f"{num1} = {num2}"
    else:
        return f"{num2} Is the max."


num1 = int(input("Input the first num: "))
num2 = int(input("Input the second num: "))
print(max_num(num1, num2))


# Task 9
"""
Write a python function to sum all numbers from given list.
"""


def sum(nums: list) -> int:
    sum = 0
    for i in nums:
        sum += i
    return sum


print(sum([1, 2, 3, 4]))


# Task 10
"""
Write a python function to multiply all numbers from given list.
"""


def multiply(nums: list) -> int:
    sum = 1
    for i in nums:
        sum *= i
    return sum


print(multiply([1, 2, 3, 4, 5]))

# Task 11
"""
You are given a program that takes all 3 passengers ages as inputs and inserts
them in a list. Complete the program so that if it finds a value less than 16, it breaks
the loop and outputs "Too young! ".
If the age requirement is satisfied, the program outputs "Get ready!".
"""


def age_checking(age1: int, age2: int, age3: int):
    """
    . Getting ages it inserts them in a list
    . And then checking is there age less than 16 or not
    """
    ages = [age1, age2, age3]
    for i in ages:
        if i < 16:
            print("Too young!!!")
            break
        else:
            print("Get ready!!!")
            break


age1 = int(input("Input the first age: "))
age2 = int(input("Input the second age: "))
age3 = int(input("Input the third age: "))
age_checking(age1, age2, age3)
