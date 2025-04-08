# -*- coding: utf-8 -*-
"""Polymorphism.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k1IdkUE65MDB9H8ontbYLpmxEz0gxPFy
"""

class Bird:
    def fly(self):
        print("Birds can fly.")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly.")

b = Bird()
p = Penguin()

b.fly()  # Output: Birds can fly.
p.fly()  # Output: Penguins cannot fly.

#1. Polymorphism with Methods
#Different classes can have methods with the same name, but they behave differently.

class Cat:
    def sound(self):
      return "Meow"

class Dog:
    def sound(self):
      return "Woof"

# Using Polymorphism
animals = [Cat(), Dog()]
for animal in animals:
    print(animal.sound())

#Explanation:
#Both Cat and Dog have a sound() method.

#When called inside a loop, Python calls the correct method based on the object.

#2. Polymorphism with Inheritance
#A parent class method is overridden by child classes.


class Vehicle:
  def move(self):
    return "Moving"
class Car(Vehicle):
    def move(self):
      return "Car is driving"

class Boat(Vehicle):
    def move(self):
      return "Boat is sailing"

# Using Polymorphism
vehicles = [Car(), Boat()]
for v in vehicles:
    print(v.move())

 #Explanation:
#Car and Boat override the move() method of Vehicle.
#The correct version is executed based on the object.

class Rectangle:
    def area(self, w, h): return w * h

class Circle:
    def area(self, r): return 3.14 * r * r

# Using Polymorphism
shapes = [Rectangle(), Circle()]
print(shapes[0].area(5, 10))  # Rectangle
print(shapes[1].area(7))      # Circle


#Explanation:
#The same area() method name is used, but parameters differ.
#The function behaves differently for Rectangle and Circle.

