# Task 1
"""
Create a class which given a year, return the century
it is in. The first century spans from the year 1 up to
and including the year 100, the second - from the
year 101 up to and including the year 200, etc.
For year = 1900, the output should be = 19
"""


class Century:
    def __init__(self, year):
        self.year = year

    def check(self):
        century = self.year // 100
        return century if not self.year % 100 else century + 1


b = Century(101)
# print(b.check())


# Task 2
"""
Create a class given the string, check if it is a palindrome.
word should be lowercase and 1 ≤ inputString.length ≤ 105
Example
For inputString = "aabaa", the output should be true;
For inputString = "abac", the output should be false;
For inputString = "a", the output should be true.
"""
from xml.dom import ValidationErr


class Palindrome:
    def __init__(self, word: str):
        self.word = word

    def validate_input(self) -> None:
        if not (1 <= len(self.word) <= 105 and self.word.islower()):
            raise ValidationErr({"massage": "wrong input !"})

    def is_palindrome(self) -> bool:
        return self.word == self.word[::-1]

    def run(self):
        self.validate_input()
        return self.is_palindrome()


a = Palindrome("aabaa")
# print(a.run())


# Task 3
"""
Create a Class which given an list of integers, find the pair of
adjacent elements that has the largest product and return that
product.
For inputList = [3, 6, -2, -5, 7, 3],
the output should be = 21.
AND EXTRA IS TO CHECK FOR ANY PAIRS !
"""


class Pairs:
    def __init__(self, lst: list):
        self.lst = lst

    def pair_of_product(self):
        max_num = float("-inf")
        for i in range(len(self.lst) - 1):
            if self.lst[i] * self.lst[i + 1] > max_num:
                max_num = self.lst[i] * self.lst[i + 1]
        return max_num

    def the_biggest_product(self):
        return sorted(self.lst)[-1] * sorted(self.lst)[-2]

        # max = float("-inf")
        # for i in range(len(self.lst)):
        #     for j in range(len(self.lst) - i):
        #         if self.lst[i] * self.lst[j] > max:
        #             max = self.lst[i] * self.lst[j]
        # return max


a = Pairs([3, 6, -2, -5, 7, 3])
# print(a.the_biggest_product())

# Task 4
"""
Create a class which given a list of strings, return another list containing
all of its longest strings.
Example
For inputList = ["aba", "aa", "ad", "vcd", "aba"],
the output should be
 allLongestStrings(inputList) = ["aba", "vcd", "aba"].
"""


class Highest_Word:
    def __init__(self, lst):
        self.lst = lst

    def checker(self):
        sorted_list = sorted(["aba", "aa", "ad", "vcd", "aba"], key=len)
        the_last = [sorted_list[-1]]
        for i in range(len(sorted_list) - 2, -1, -1):
            if len(sorted_list[i]) == len(the_last[0]):
                the_last.append(sorted_list[i])
        return the_last


runner = Highest_Word(["aba", "aa", "ad", "vcd", "aba"])
# print(runner.checker())

# Task 5
"""
Ticket numbers usually consist of an even number of digits.A ticket number is
considered lucky if the sum of the first half of the digits is equal to the sum of the
second half.Given a ticket number n, determine if it's lucky or not. Example For n
= 1230, the output should be
Lucky(n) = true;
For n = 239017,
the output should be Lucky(n) = false
"""


class Lucky:
    def __init__(self, num):
        self.num = num

    def num_valid(self):
        if len(str(self.num)) % 2 != 0:
            raise ValidationErr({"massage": "wrong input !"})

    def ticket_check(self):
        self.num = [int(i) for i in str(self.num)]
        half = len(self.num) // 2
        return sum(self.num[:half]) == sum(self.num[half:])

    def run(self):
        self.num_valid()
        return self.ticket_check()


a = Lucky(1230)
# print(a.run())
# print(list('1230')[:len(list('1230')) // 2])


# Task 6
"""
Create a class: Some people are standing in a row in a park. There are trees
between them which cannot be moved. Your task is to rearrange the people by their
heights in a non-descending order without moving the trees. People can be very tall!
Example
 For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
 sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""


class Height:
    def __init__(self, lst: list):
        self.lst = lst

    def sort_by_height(self):
        old = self.lst
        new = sorted([i for i in old if i != -1])
        counter = 0
        for i in range(len(old)):
            if old[i] != -1:
                old[i] = new[counter]
                counter += 1
        print(old)


a = Height([-1, 150, 190, 170, -1, -1, 160, 180])
# a.sort_by_height()

# Task 7
"""
Several people are standing in a row and need to be divided into two teams. The first
person goes into team 1, the second goes into team 2, the third goes into team 1
again, the fourth into team 2, and so on.You are given an array of positive integers -
the weights of the people. Return an array of two integers, where the first element is
the total weight of team 1, and the second element is the total weight of team 2 after
the division is complete.
Example For a = [50, 60, 60, 45, 70], the output should be
alternating Sums(a) = [180, 105].
"""


class Two_Teams_Height:
    def __init__(self, lst):
        self.lst = lst

    def team_excange(self):
        sums = sum([self.lst[i] for i in range(0, len(self.lst), 2)])
        alternating_sum = [sums, (sum(self.lst) - sums)]
        return alternating_sum


runner = Two_Teams_Height([50, 60, 60, 45, 70])
# print(runner.team_excange())


# EXTRA TASK
import random


class Queastion_Game:
    def __init__(self, questions: dict):
        self.questions = questions
        self.incorrect_counter = 0

    def question_choose(self, incorrect_questions, n=5):
        questions = random.choices(list(math_questions.items()), k=n)
        questions.extend(incorrect_questions)
        random.shuffle(questions)
        return questions

    def incorrect_question_choose(self, incorrect_questions, n=3):
        questions = random.choices(incorrect_questions, k=n)
        random.shuffle(questions)
        return questions

    def game_brain(self, questions):
        incorrect = []
        self.incorrect_counter = 0
        for question, answer in questions:
            print(f"Question: {question}")
            print("Answers: ")
            answers = list(math_questions.values())
            answers.remove(answer)
            answers = random.choices(answers, k=3)
            answers.append(answer)
            random.shuffle(answers)
            for i, options in enumerate(answers, start=1):
                print(f"{i}. {options}")
            user_answer = input("Your choice is: ")
            if user_answer == answer:
                print("Correct !")
                # self.correct_counter += 1
                try:
                    incorrect.remove((question, answer))
                except ValueError:
                    pass
            else:
                print("Incorrect !!!")
                self.incorrect_counter += 1
                if (question, answer) not in incorrect:
                    incorrect.append((question, answer))
        return incorrect

    def printer(self):
        return "\nBrain Game!\n"

    def main(self, incorrect_questions, n=5):
        print(self.printer())
        questions = self.question_choose(incorrect_questions, n)
        incorrect_questions = self.game_brain(questions)
        # while True:
        #     if self.incorrect_counter > 2.5 or self.incorrect_counter == 1:
        #         return self.main(incorrect_questions, 3)
        #     if not incorrect_questions:
        #         return "Congratulations! You answered all questions correctly."
        if self.incorrect_counter == 3:
            questions = self.incorrect_question_choose(incorrect_questions, 3)
            incorrect_questions = self.game_brain(questions)
        if self.incorrect_counter == 4:
            questions = self.incorrect_question_choose(incorrect_questions, 3)

math_questions = {
    "What is 2 + 2?": "4",
    "What is 5 * 3?": "15",
    "What is 10 / 2?": "5",
    "What is 7 - 4?": "3",
    "What is 8 + 5?": "13",
    "What is 6 * 4?": "24",
    "What is 15 * 3?": "45",
    "What is 9 * 3?": "27",
    "What is 12 + 4?": "16",
    "What is 25 * 2?": "50",
    "What is 18 / 3?": "6",
    "What is 11 - 6?": "5",
    "What is 3 + 9?": "12",
    "What is 4 * 7?": "28",
    "What is 20 / 4?": "5",
    "What is 15 - 7?": "8",
    "What is 10 * 8?": "80",
    "What is 6 * 5?": "30",
    "What is 45 / 5?": "9",
    "What is 20 - 9?": "11",
    "What is 7 + 11?": "18",
    "What is 8 * 4?": "32",
    "What is 36 / 6?": "6",
    "What is 14 - 6?": "8",
    "What is 9 + 10?": "19",
    "What is 3 * 8?": "24",
    "What is 24 / 3?": "8",
    "What is 17 - 9?": "8",
    "What is 14 + 6?": "20",
    "What is 2 * 10?": "20",
}

runer = Queastion_Game(math_questions)
runer.main([])
