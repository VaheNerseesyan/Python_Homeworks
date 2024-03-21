#Task 1
"""
Write a python class to find max, min num and and
sum in your list:
don't use max sum and min function
"""

class ListPresenter():
    def __init__(self, lst: list) -> None:
        self.lst = lst

    def max_elem(self) -> int:
        max = self.lst[0]
        for i in self.lst:
            if i > max:
                max = i
        return max
    
    def min_elem(self) -> int:
        min = self.lst[0]
        for i in self.lst:
            if i < min:
                min = i
        return min
    
    def sum_elems(self) -> int:
        sum = 0
        for i in self.lst:
            sum += i
        return sum
    
a = ListPresenter([1,2,-3,34,5])
print(a.max_elem())
print(a.min_elem())
print(a.sum_elems())

#Task 2
"""
Write a python class to find two highest values in your
dict:
"""
class MaxFinder():
    def __init__(self, dct: dict) -> None:
        self.dct = dct

    def max_value(self):
        max = float("-inf")
        ky = None
        for key, value in self.dct.items():
            if value > max:
                max = value
                ky = key
        self.dct.pop(ky)
        return max
    
    def next_max(self):
        return self.max_value()
    
b = MaxFinder({"Vahe": 19, "Narek": 24, "John": 44})
print(b.max_value())
print(b.next_max())

#Task 3
"""
Write a python class where your child class takes all
methods in parent class and print them.
"""

class Cars():
    def names(self):
        first_car = "Porsche"

    def colors(self):
        color1 = "Blue"

class Presenter(Cars):
    def __init__(self) -> None:
        super().__init__()
        self.printer()

    def printer(self):
        print("Cars Class Methods: ")
        for i in [i for i in dir(Cars)]:
            print(i)

c = Presenter()

#Task 4
"""
Write a Python class named Rectangle constructed by
a length and width and a method which will compute the
area of a rectangle.
"""

class Rectangle:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
 
    def area(self):
        return self.height * self.weight
    
a = Rectangle(4,6)
print(a.area())

#Task 5
"""
Write a python class where we use polymorphism:
Example:
a.country() - Erevan
b.country() - Paris
"""
class Armenia:
    def city(self):
        print("Erevan")
 
class Usa:
    def city(self):
        print("Paris")
 
a = Armenia()
u = Usa()
a.city()
u.city()

#Task 6
"""
Create a class Change:You have 3
methods in your class:
Usd --- Eur
Usd --- Amd
Usd --- Ru
"""
class Change():
    def USD_EUR(self, amount):
        return amount * 0.92
    def USD_AMD(self, amount):
        return amount * 397.93
    def USD_RU(self, amount):
        return amount * 92.40
    
money = Change()
print(money.USD_AMD(100))
print(money.USD_EUR(100))
print(money.USD_RU(100))