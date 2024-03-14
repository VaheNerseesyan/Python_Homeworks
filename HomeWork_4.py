# Task 1
"""
Given three numbers a, b (a ≤ b) and step. Create an list of
evenly spaced elements starting from a to b spaced by step. you
have 3 argument:
Input Output
1 5 1 [1, 2, 3, 4, 5]
10 100 20 [10, 30, 50, 70, 90]
"""


def count_by_step(start: int, stop: int, step: int) -> list:
    result = list()
    for i in range(start, stop + 1, step):
        result.append(i)
    return result


print(count_by_step(10, 100, 20))


# Task 2
"""
Imagine you and the computer are playing tennis. write a
program where you have a sheet where victory points are
kept and you need to figure out who is the winner.A set is
won by the first side to win 6 games. You should to show
the result of the match. If game win you in list add “a” if
pc “b”.
"""


def tennis_score(result_of_game: list) -> str:
    """
    My way of the tennis score is this, and for his gold scores counting subtlety
    I used this method, reducing the score when it is like a:5 b:5, and the win will be
    for 7 scores, not for 6 scores, so this code is reducing both of scores by 1, and
    in result we have the correct win score checker
    """
    count_a = 0
    count_b = 0
    w_a = 0
    w_b = 0
    k = 0
    while k < len(result_of_game):
        if result_of_game[k] == "a":
            count_a += 1
        elif result_of_game[k] == "b":
            count_b += 1
        if count_a == 5 and count_b == 5:
            count_a = count_b = 4
        if count_a == 6 and count_b < 6:
            count_a = 0
            count_b = 0
            w_a += 1
        elif count_a < 6 and count_b == 6:
            count_a = 0
            count_b = 0
            w_b += 1
        k += 1
    return f"score -> a:{w_a} b:{w_b}"


first = [
    "b",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "b",
    "b",
    "b",
    "b",
    "b",
    "b",
    "a",
    "a",
    "a",
    "a",
    "a",
    "b",
    "b",
    "b",
    "b",
    "b",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
]
second = [
    "b",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "b",
    "b",
    "b",
    "b",
    "b",
    "b",
    "a",
    "a",
    "a",
    "a",
    "a",
    "b",
    "b",
    "b",
    "b",
    "b",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "a",
    "b",
    "b",
    "a",
    "a",
    "b",
    "a",
    "b",
    "a",
    "b",
    "b",
]
"""Example first will return a:4 b:0, and the second one will return a:4 b:1"""
print(tennis_score(first))

# Task 3
"""
Binary search without recursion
"""


def binary_search(lst, search):
    stop = len(lst) - 1
    start = 0
    mid = None
    while start <= stop:
        mid = (stop + start) // 2
        if lst[mid] > search:
            stop = mid - 1
        elif lst[mid] < search:
            start = mid + 1
        else:
            return mid
    return False


lst = [4, 5, 6, 9, 20, 43, 52, 55, 56, 66, 73]
search = 55
result = binary_search(lst, search)
if result == False:
    print(f"There is not element like {search}")
else:
    print("Element is at index", result)


# Task 4
"""
Sorting dictionary with its values without sort or sorted function
"""
dct = {"Vahe": 10, "Vahag": 10, "Narek": 8, "Armen": 2, "Lusine": 1, "Gagou": 5}


def dict_sorting(dct: dict) -> dict:
    sorted_dict = {}
    for i in range(len(dct)):
        """
        min(iterable, *[, default=obj, key=func]) -> value max(arg1, arg2, *args, *[, key=func]) -> value
        The min() function allows using a key function that helps customize the comparison process.
        The key argument accepts a callable function like int(), len(), ord(), or even a custom user-defined function.
        """
        min_key = min(dct, key=dct.get)
        sorted_dict[min_key] = dct.pop(min_key)
    return sorted_dict


print(dict_sorting(dct))