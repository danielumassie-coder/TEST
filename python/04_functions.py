"""
Lesson 4: Functions - Reusable Code Blocks
===========================================

Functions are reusable pieces of code that perform specific tasks.
They help organize code and avoid repetition.

What you'll learn:
- How to define functions
- Parameters and arguments
- Return values
- Why functions are important
"""

# ==================
# BASIC FUNCTIONS
# ==================

def greet():
    """This function prints a greeting"""
    print("Hello! Welcome to Python!")

# Calling the function
greet()
greet()  # You can call it multiple times

# ==================
# FUNCTIONS WITH PARAMETERS
# ==================

def greet_person(name):
    """Greet a specific person"""
    print("Hello,", name + "!")

greet_person("Alice")
greet_person("Bob")

# Multiple parameters
def introduce(name, age):
    """Print an introduction"""
    print("Hi! I'm", name, "and I'm", age, "years old.")

introduce("Charlie", 25)
introduce("Diana", 30)

# ==================
# RETURN VALUES
# ==================

def add(a, b):
    """Add two numbers and return the result"""
    result = a + b
    return result

sum_result = add(5, 3)
print("5 + 3 =", sum_result)

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

print("4 * 7 =", multiply(4, 7))

# ==================
# DEFAULT PARAMETERS
# ==================

def greet_with_title(name, title="Friend"):
    """Greet someone with a title"""
    print("Hello,", title, name + "!")

greet_with_title("Alice")  # Uses default title
greet_with_title("Bob", "Dr.")  # Custom title

# ==================
# PRACTICAL EXAMPLES
# ==================

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

print("Is 4 even?", is_even(4))
print("Is 7 even?", is_even(7))

def calculate_area(length, width):
    """Calculate area of a rectangle"""
    area = length * width
    return area

print("Area of 5x3 rectangle:", calculate_area(5, 3))

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print("25°C =", celsius_to_fahrenheit(25), "°F")

# ==================
# EXERCISES
# ==================

# 1. Create a function that takes a name and prints a goodbye message
def say_goodbye(name):
    print("Goodbye,", name + "! See you later!")

say_goodbye("Emma")

# 2. Create a function that calculates the square of a number
def square(num):
    return num * num

print("Square of 5:", square(5))

# 3. Create a function that checks if someone can vote (age >= 18)
def can_vote(age):
    return age >= 18

print("Can 20-year-old vote?", can_vote(20))
print("Can 16-year-old vote?", can_vote(16))

# Your turn! Create your own functions below:
