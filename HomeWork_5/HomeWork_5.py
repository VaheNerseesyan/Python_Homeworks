# Task 1
"""
Write a recursive function to determine whether
all digits of the number are odd or not.
Input Output
4211133 False
7791 True
5 True
"""


def odd_digits(num: int) -> bool:
    """
    Poper is the last elem of my num, and num % 10 is that, because the recidual of num when we dividing to 10 is the last elem
    """
    poper = num % 10
    if poper == 0:
        return True
    if poper % 2 == 0:
        return False
    else:
        return odd_digits(num // 10)


print(odd_digits(11133))

# Task 2
"""
Write a python function all even number
in 10.000 use threading and print time.
"""

import threading
import time


def even_nums(start: int, stop: int):
    for i in range(start, stop, 2):
        with open("evens.txt", "a") as evensf:
            evensf.write(f"{i}\n")


baj = 10000 // 4
# start_time = time.time()
# t1 = threading.Thread(target = even_nums, args = (2, baj))
# t1.start()
# t1.join()
# t2 = threading.Thread(target = even_nums, args = (baj, 2*baj))
# t2.start()
# t2.join()
# t3 = threading.Thread(target = even_nums, args = (2*baj, 3*baj))
# t3.start()
# t3.join()
# t4 = threading.Thread(target = even_nums, args = (3*baj, 4*baj + 1))
# t4.start()
# t4.join()
# end_time = time.time()
# print("Function worked time -> ",end_time - start_time)

# Task 3
"""
Given N number. Write a recursive function
that should print from 1 to N numbers.
Input Output
5 1, 2, 3, 4, 5
"""


def count_UP_to(number):
    if number == 0:
        return
    else:
        # with changing this ⬇️ two lines, also is changing the counting above UP or DOWN
        count_UP_to(number - 1)
        print(number, end=" ")


count_UP_to(5)
print()

# Task 4
"""
Write a python program to find the longest word from the file content.Need
to use <try-except> block in the file reading process and print time. example:
1. try:
2.      with open("filename.txt") as file:
3.      some code
4. except:
5.      do something
6. Function call: find_long_word("filename.txt")
7. Function output: "LongestWord"
"""


def find_long_word(file_name):
    try:
        with open(file_name, "r") as filess:
            for line in filess:
                info = line[:-1].split(" ")
            print("The longest word is:", max(info, key=len))
    except FileNotFoundError:
        print("Invalid File input !")
    except NameError:
        print("Invalid argument !")


find_long_word("HomeWork_5\Words.txt")


# Extra Task
"""
Counting words from text in file
"""
def lyrics(file_name):
    lyrics = dict()
    with open(file_name, "r") as wordf:
        for line in wordf.readlines():
            words = line[:-1].split(" ")
            temp = {i: (lyrics[i] + 1) if i in lyrics else 1 for i in words}
            lyrics.update(temp)
    return lyrics


print(lyrics(R"HomeWork_5\barer.txt"))
