"""Fib and Fast Fib with working time"""
import time

def time_checker(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result

    return wrapper


def fast_fib(n, memory):
    if n <= 0:
        return "Wrong Input!"
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memory:
        memory[n] = fast_fib(n - 1, memory) + fast_fib(n - 2, memory)
    return memory[n]


def fibonnaci(num):
    if num == 1:
        return 0
    if num == 1:
        return 0
    if num == 2:
        return 1
    return fibonnaci(num - 2) + fibonnaci(num - 1)


@time_checker
def calculate_fib(num):
    memory = {}
    print(f"Fibonacci number at position {num} is: {fibonnaci(num)}")  # Try with {fast_fib(num, memory)}


num = 35
calculate_fib(num)