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
# calculate_fib(num)

"""Create cash  for dictionary for 5 seconds"""

""" WITH THREADING"""
import threading
import queue

my_dict = {}


def remove_oldest_pair(queue):
    while True:
        time.sleep(5)  # This is within a separate thread, so it doesn't block the main thread
        try:
            key, _ = queue.get(timeout=1)  # Get the oldest key from the queue
            del my_dict[key]
            print(f"Removed oldest key: {key}")
            print(f"Updated dictionary: {my_dict}")
        except queue.Empty:
            pass


def manage_dict():
    removal_queue = queue.Queue()

    # Start the thread for removing the oldest pair every 5 seconds
    removal_thread = threading.Thread(target=remove_oldest_pair, args=(removal_queue,), daemon=True)
    removal_thread.start()

    print("Enter key-value pairs. Type 'exit' to stop.")

    while True:
        key = input("Enter key: ")
        if key == 'exit':
            break
        value = input("Enter value: ")
        if value == 'exit':
            break

        my_dict[key] = value
        removal_queue.put((key, value))
        print(f"Current dictionary: {my_dict}")


# manage_dict()

"""SIMPLy WAY"""


def manages_dict():
    last_removed_time = time.time()

    print("Enter key-value pairs. Type 'exit' to stop.")

    while True:
        key = input("Enter key: ")
        if key == 'exit':
            break
        value = input("Enter value: ")
        if value == 'exit':
            break

        my_dict[key] = value
        print(f"Current dictionary: {my_dict}")

        # Check if it's time to remove the oldest pair
        if time.time() - last_removed_time >= 5:
            if my_dict:
                oldest_key = next(iter(my_dict))
                del my_dict[oldest_key]
                print(f"Removed oldest key: {oldest_key}")
                print(f"Updated dictionary: {my_dict}")
                last_removed_time = time.time()


# manages_dict()

