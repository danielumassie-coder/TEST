"""
Lesson 3: Control Flow - Making Decisions
==========================================

Programs need to make decisions and repeat actions.
Control flow lets your code be smart and dynamic!

What you'll learn:
- if/else statements (making decisions)
- Loops (repeating actions)
- Comparison operators
"""

# ==================
# IF/ELSE STATEMENTS
# ==================

age = 18

if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor!")

# Multiple conditions with elif
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Comparison operators:
# == (equals)
# != (not equals)
# > (greater than)
# < (less than)
# >= (greater than or equal)
# <= (less than or equal)

temperature = 75

if temperature > 80:
    print("It's hot!")
elif temperature > 60:
    print("It's nice!")
else:
    print("It's cold!")

# ==================
# FOR LOOPS
# ==================

# Loop through a range of numbers
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Loop through a list
fruits = ["apple", "banana", "cherry"]
print("\nMy favorite fruits:")
for fruit in fruits:
    print("-", fruit)

# ==================
# WHILE LOOPS
# ==================

# Repeat while a condition is true
count = 0
while count < 3:
    print("Count is:", count)
    count += 1  # Same as count = count + 1

# ==================
# COMBINING IF AND LOOPS
# ==================

print("\nEven numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:  # % is modulo (remainder)
        print(num)

# EXERCISES:
# 1. Write an if/else that checks if a number is positive or negative
# 2. Create a loop that prints your name 5 times
# 3. Print all odd numbers from 1 to 20

# Your code here:
number = -5
if number > 0:
    print(number, "is positive")
else:
    print(number, "is negative")
