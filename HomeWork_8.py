"""
Armenian phone number validation
"""
def add_country_code(returner):
    def wrapper():
        """
        checking the start of input phone number, if it is starting with 0XX... we will change it +374XX...
        """
        phone_number = input("Input your phone number: ")
        check = phone_number.strip()
        """
        .startswith() function description
        string.startswith(value, start, end)
        """
        if check.startswith("+374"):
            return returner(check)
        if check.startswith("0"):
            checker = "+374" + check[1:]
            return returner(checker)
    return wrapper


def phone_number_validation(checked) -> str:
    """
    checking the length of phone number and the codes from our armenian codes
    """
    checker = checked
    phone_codes = ["33", "55", "93", "77", "94", "95", "98", "44", "41"]
    if len(checker) != 12:
        return "Invalid Phone number !!!\nThe length of phone number is incorrect !!!"
    if checker[5:7] not in phone_codes:
        return "Invalid Phone number !!!\nThe code of phone number does not exist !!!"
    return "Valid Number"


@add_country_code
def run(validated):
    return phone_number_validation(validated)


# print(run())


# Extra Homework
"""
Consider an array of integers with starting index of 1, numbers, that is sorted in ascending order. 
Your task is to identify two distinct elements, numbers[i] and numbers[j], 
such that their sum equals a predetermined target value. 
Here, the constraints are 1 <= i < j <= length(numbers).

Your output should be an integer array of length 2, [i, j], 
representing the indices of the two numbers incremented by one.
The tests are designed in such a way that there is precisely one unique solution. 
You are not allowed to use the same element more than once.

Your solution must use only constant extra space.
Test Cases:
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, i = 1, j = 2. We return [1, 2].
Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore i = 1, j = 3. We return [1, 3].
Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore i = 1, j = 2. We return [1, 2].
Constraints:
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in ascending order.
-1000 <= target<= 1000
The tests are designed such that there is exactly one solution.
"""


def pair_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers) - i):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]


run1 = pair_sum([2, 7, 11, 15], 9)
run2 = pair_sum([2, 3, 4], 6)
run3 = pair_sum([-1, 0], -1)
print(run2)
