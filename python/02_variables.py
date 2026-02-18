"""
Lesson 2: Variables - Storing Information
==========================================

Variables are like containers that store information.
Think of them as labeled boxes where you can keep data.

What you'll learn:
- How to create variables
- Different types of data (strings, numbers, booleans)
- How to use variables in your programs
"""

# Creating variables with strings (text)
name = "Alice"
favorite_food = "Pizza"

print("Hello, my name is", name)
print("I love", favorite_food)

# Creating variables with numbers
age = 25
height = 5.8  # This is a decimal number (float)

print(name, "is", age, "years old")
print("Height:", height, "feet")

# You can change variable values
age = 26  # Birthday!
print("After birthday:", name, "is now", age)

# Boolean variables (True or False)
is_student = True
is_working = False

print("Is student?", is_student)

# You can do math with number variables
x = 10
y = 5

print("x + y =", x + y)  # Addition
print("x - y =", x - y)  # Subtraction
print("x * y =", x * y)  # Multiplication
print("x / y =", x / y)  # Division

# Combining strings (concatenation)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# EXERCISES:
# 1. Create variables for your name, age, and city
# 2. Print a sentence using those variables
# 3. Create two numbers and print their sum and product

# Your code here:
my_name = "Your Name"
my_age = 20
my_city = "Your City"

print("Hi! I'm", my_name, "from", my_city)
