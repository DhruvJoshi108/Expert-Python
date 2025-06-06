# -*- coding: utf-8 -*-
"""OOP-Encapsulation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x0oxGHUo80TjBPd_kr95DXZ01XuU85ox
"""

# Question 1:
# Create a Laptop class with a private attribute __price. Implement a method set_price(new_price) to update the price and get_price() to retrieve the price.
class Laptop:
  def __init__(self,name,price):
    self.name = name
    self.__price = price
  def set_price(self , new_price):
    self.__price = new_price
  def get_price(self):
    return self.__price
lp = Laptop("HP" , 50000)

print(lp.name , lp.get_price())

lp.set_price(60000)

print(lp.name , lp.get_price())

"""# New Section"""

# Question 2:
# Create a BankAccount class with a private attribute __balance. Implement methods to deposit, withdraw, and check balance while ensuring the balance cannot be modified directly.
class BankAccount:
  def __init__(self, name  , balance = 0 ):
    self.name = name
    self.__balance = balance

  def withdraw(self , amount):
    if amount <= self.__balance:
      self.__balance -= amount
      return self.__balance
    else:
       return 'Insufficient balance'

  def deposit(self,amount):
    self.__balance += amount
    return self.__balance

  def check_balance(self):
    return self.__balance

wit = BankAccount('Dhruv', 1000)
print("Name:", wit.name)
print("Balance after deposit:", wit.deposit(5000))
print("Balance after withdrawal:", wit.withdraw(10000))

# Question 3:
# Create a Movie class with a private attribute __rating. Implement methods to set and get the rating, ensuring the rating is between 1 and 10.
class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.set_rating(rating)

    def set_rating(self, new_rating):
        if 1 <= new_rating <= 10:
            self.__rating = new_rating
        else:
            "Rating must be between 1 and 10."

    def get_rating(self):
        return self.__rating


v = Movie("xyz", 6)
print(v.get_rating())

# Question 4:
# Create a Book class with private attributes __title and __author. Implement a constructor to set these values and provide methods to retrieve them.
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def info(self):
        print(f"The title is {self.title} and it's author is {self.author}")
a=Book("Great Expectations","Charles Dickens")
b=Book("The God of Small Things","Arundhati Roy")
a.info()
b.info()

