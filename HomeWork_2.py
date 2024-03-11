# !!! Python Decorators and Generators !!!
#Task 1
""" 
Create a python program which will say which number used more. my_list = [1,
3, 4, 5, 1, 2, 3, 1] output: number 1 - 3 times
"""
def max_num_rep(numbers:list) -> str:
    """
    Getting the list of nums, checking the most repetitive elem, and return it with its repetition count
    """


    nums = list({i: numbers.count(i) for i in numbers}.items())
    max_value = nums[0][1]
    max_key = nums[0][0]
    for i in nums:
        if i[1] > max_value:
            max_key = i[0]
            max_value = i[1]
    return f"number {max_key} - {max_value} times"
print(max_num_rep([1,3,4,5,1,2,3,1]))

#Task 2
"""
Write a Python program to sum all the items in a list. use list comprehension
"""
sum = 0
print([sum:= sum + i for i in [1, 2, 3, 4, 5]][-1])

#Task 3
"""
Write a Python program to get the largest text from a list.
"""
def max_text(lst:list) -> str:
    # 1 method
    """
    assume that the largest elem is the first one in the list, and then check it with the others
    """
    max1 = lst[0]
    for i in lst:
        if len(i) > len(max1):
            max1 = i
    print("First method ->",max1)
    # 2 method
    """
    max(iterable, *[, default=obj, key=func]) -> value max(arg1, arg2, *args, *[, key=func]) -> value

    The max() function allows using a key function that helps customize the comparison process. 
    The key argument accepts a callable function like int(), len(), ord(), or even a custom user-defined function.
    """

    print("Second method ->", max(lst, key = len))
max_text(["Vahe", "Nersesyan", "Python"])

#Task 4
"""
Write a Python program that have two lists and returns True if they have at
least one common member.
"""
def common_member(list1:list, list2:list) -> bool:
    """
    Using set's & function we can know have they any common elem or not
    """
    is_common = bool
    for i in list1:
        if i in list2:
            is_common = True
            break
        else:
            return is_common == False
    return is_common
print(common_member([1,2,3,4],[5,6,6,6,6,3]))

#Task 5
"""
Write a Python program to Sort Words in Alphabetic Order
"""
def word_sorting_by_alphabet(txt:str) -> list:
    """
    . spliting the words by space and using str.title() function, 
      which is uppering each word sorting them to the list
    """
    return sorted([i for i in (txt.title()).split()])
print(word_sorting_by_alphabet("Hello world my full name is Vahe Nersesyan"))

#Task 6
"""
Write a Python program that creates a generator function that generates all
prime numbers between two given numbers.
"""
from typing import List
def is_prime(num: int) -> bool:
    """
    . Checking the nums, too see are there nums that are divisible by 2, and the negative numbers
    . With for loop check the divisions from 2, to the half of the num, or the root of the num
    . Return True if the num is Prime, or False if not
    """

    if num % 2 == 0 or num == 2 or num <= 0:
        return False
    #             ⬇️  this must be grather than 1
    for i in range(2, num // 2):
        """^^^ Here can be the other way, (num // math.floor(num**(1/2))) , because the smallest num after 2, that
        we can devide is the root of num
        """
        if num % i == 0:
            return False
    return True

def prime_nums(start:int, stop:int, func):
    """
    checking is the num prime or not with is_prime() function sinc start num adding += 1 to stop num
    """
    while start <= stop:
        if func(start):
            yield int(start) 
        start += 1

counter = prime_nums(2,20, is_prime)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#Task 7
"""
Create python program which will check if your password is strong or no. if Len
your password is great than 8 and if your password have 2 numbers and 2 of the
following special characters ('!', '@', '#', '$', '%', '&', '*')
Sample Input: Python@$World11
Sample Output: Strong
"""
import string
def valid_password(password: str) -> str:
    """
    checking the len of password, then checking are ther 2 numbers and 2 special symbols or not
    """
    nums = 0
    spec_nums = 0
    is_valid = True
    for symbol in str(password):
        if len(password) < 8:
            is_valid = False
            break
        if symbol in string.digits:
            nums += 1
                                 #  ⬇️ this can be string.punctuation too
        if symbol in ['!', '@', '#', '$', '%', '&', '*']:
            spec_nums += 1
    if not is_valid or (nums < 2 or spec_nums < 2) :
        print(password, ": -> is not Strong Password !!")
    else:
        print(password, ": -> Strong Password !!")
valid_password("abcdef1234567")

#Task 8
"""
Create python program where you want to find id in link if link have id print id.
Sample Input: https://www.youtube.com/watch?v=RRW2aUSw5vU
Sample Output: RRW2aUSw5vU
"""
def link_id(link:str) -> str:
    """
    checking the link Spliting by =
    """
    lst = link.split("=")
    if len(lst) < 2:
        return "The link dont have an id !"
    else:
        return lst[1]
print(link_id("https://www.youtube.com/watch?v=RRW2aUSw5vU"))

#Task 9
"""
Write a Python program that implements a decorator to validate function arguments
based on a given condition.
"""
def valid_arguments(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                return "Invalid argument !"
        return wrapper
    return decorator

@valid_arguments(lambda x,*args : x > 0)
def pow_2(x,y,z,c,v,b):
    return x ** 2 + y + z + c + v + b
print(pow_2(5, 6, 7, 8, 9, 0))


#Task 10
"""
Write a Python program that implements a decorator to validate function arguments
length.
"""
def valid_arguments(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                return "Invalid argument !"
        return wrapper
    return decorator 
                                #⬇️ type args is tuple, and i may choose to run it with list or with tuple 
@valid_arguments(lambda *args: list(args) == [arg for arg in args if len(arg) > 3])
def hello_name(name1:str, name2:str) -> str:
    return f"Hello {name1}, {name2}"
print(hello_name("Vahe", "Narek"))

# !!! Python Recursion !!!
#Task 1
"""
Write a Python program which will
remove all zeros from an IP
address.
ip = "216.008.094.196"
"""
def zero_remover(ip_address:str) -> str:
    """ initializing IP address ip_address = "216.008.094.196"
        spliting using the split() functions
        converting every part to int
        convert each to str again before joining them
        joining every part using the join() method
    """
    parts = ip_address.split(".")
    new_parts = []
    for part in range(len(parts)):
        new_parts.append(parts[part].replace("0", ""))
    ip_address = ".".join(new_parts)
    return ip_address

print(zero_remover("216.008.904.196"))

#Task 2
"""
Given an list of numbers. Find the maximum element in list.Without use max function.
"""
def max(lst:list) -> int:
    """
    Assume that the max is the first elem of list
    then check the condition with max and the other nums in list
    """
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max

print(max([5,4,3,2,1]))

#Task 3
"""
Write a Python program that validates passwords based on the following
criteria:
● The password must be at least 8 characters long.
● The password must contain at least one uppercase letter.
● The password must contain at least one lowercase letter.
● The password must contain at least one digit (0-9).
● The password must contain at least one special character (e.g., @, #, $,
etc.).
"""
import string
def password_validation(password:str) -> str:
    digits, specials, lowers, uppers, = 0, 0, 0, 0
    for i in str(password):
        if len(password) < 8:
            break
        if i.isdigit():
            digits += 1
        if i in string.punctuation:
            specials += 1
        if i.islower():
            lowers += 1
        if i.isupper():
            uppers += 1

    if digits >= 1 and specials >= 1 and lowers >= 1 and uppers >= 1:
        print(password, ": -> is Valid Password !!")
    else:
        print(password, ": -> is not Valid Password !!")

password_validation("Python@$World11")

#Task 4
"""
Write a program that takes in a string as input, counts and outputs the number of vowels.
For example:
input: test
output: 1
"""
def vowels_counter(txt:str) -> str:
    vowels = "AaEeIiOoUu"
    return len([symbols for symbols in txt if symbols in vowels])

print(vowels_counter("Vahe Nersesyan"))

#Task 5
"""
Write a function. Create the list which elements are
products between two neighbours.
 Input                        Output
 input : [3, 7, 12, 5, 20, 0] output: [21, 84, 60, 100, 0]
 input : [1, 1, 4, 32, 6]     output: [1, 4, 128, 192 ]
"""
def neighbour_product(lst:list) -> list:
    """
    in range with one index smaller doing the multiply with elements by += index with one number step
    """
    product = []
                          #⬇️This is for⬇️
    for i in range(len(lst) - 1):#      ⬇️
                           #           ⬇️ this, because if we use lst[i + 1], the output will be index error out of range
        product.append(lst[i] * lst[i + 1])
    return product

print(neighbour_product([1, 1, 4, 32, 6]))

#Task 6
"""
Given a sentence with missing words and an array of words. Replace all _ in a sentence with the words from
the array.
Input “_ we have a _.”
[“Ashot”, “problem”]
Output: “Ashot we have a problem.
"""
def under_line_replacer(txt:str, word:list) -> str:
    """
    Spliting the sentence with spaces

    """
    elems = txt.split()
    length = len(elems)
    k = 0
    for i in range(length):
        if elems[i] == "_":
            elems[i] = word[k]
            k += 1
    print(" ".join(elems))
under_line_replacer("_ we have a _ .", ["Ashot", "problem"])

#Task 7
"""
Given a list of strings. Find the strings with maximum
and minimum lengths in array. Print the sum of their
lengths.
Input: [“anymore”, “raven”, “me”, “communicate”]
Output: 13
"""
def max_min_len(lst:list) -> int:
    """
    buble sorting
    """
    max1 = len(lst[0])
    min1 = len(lst[0])
    for bar in lst[1::]:
        if len(bar) > max1:
            max1 = len(bar)
        if len(bar) < min1:
            min1 = len(bar)
    print(min1 + max1)

max_min_len(["anymore", "raven", "me", "communicate"])

#Task 8
"""
Given a list of numbers and a number. Find the index
of a first element which is equal to that number. If there is
not such a number, that find the index of the first element
which is the closest to it. Input Output
[21, -9, 15, 2116, -71, 33], -71 4
[ 36, -12, 47, -58, 148, -55, -19, 10], -56 5
"""

def find_the_nearest_element_index(input_list: list[int], searched_num: int) -> int:
    """
    Check the first is the same num in following list or not
    then assume that min difference is float('inf) and
    checking the absolute differnece choose the min diiference num index
    """
    if searched_num in input_list:
        return input_list.index(searched_num)
    min_difference_index = None
    min_difference = float('inf')
    for i in range(len(input_list)):
        if abs(searched_num - input_list[i]) < min_difference:
            min_difference = abs(searched_num - input_list[i])
            min_difference_index = i
    return min_difference_index

input_list_1 = [36, -12, 47, -58, 148, -55, -55, 10]
searched_num_1 = -56

answer = find_the_nearest_element_index(input_list_1, searched_num_1)
print(answer)

#Task 9
"""
Given an dict. Invert it (keys become values and values
become keys). If there is more than key for that given
value create an list.Input
{ "a": 1, "b": 2, "c": 2 }
Output
{ 1: "a", 2: ["b", "c"] }
{a:1, b:2}
"""
old_dict = {"a": 1, "b": 2, "c": 2 , "d": 2}
print(list(old_dict.values()))
def dict_invertor(dct:dict) -> dict:
    """
    . !!! OLD DICTIONARY VALUES MUST BE IMMUTABLE !!!
    adding the value, keys in new dict if there is no duplicated values in old dict
    or creating and appending new duplicated values in old list
    """
    new_dict = dict()
    for key, value in dct.items():
        if not new_dict.get(value):
            new_dict[value] = key
        else:
            if isinstance(new_dict[value], list):
                new_dict[value].append(key)
            else:
                new_dict[value] = list((new_dict[value] , key))
    return new_dict

print(dict_invertor(old_dict))

#Task 10
"""
Define a function which can generate a dictionary
where the keys are numbers between 1 and N (both
included) and the values are square of keys. The function
should print the dict.Example :
N = 5
{1: 1, 2:4, 3:9, 4:16, 5:25}
"""
def nums_power_of_two(num:int) -> dict:
    print({i: i * i for i in range(1, num + 1)})

nums_power_of_two(5)