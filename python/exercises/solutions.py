"""
Solutions to Python Exercises
==============================

Here are the solutions to the exercises.
Try solving them yourself first before looking here!
"""

print("=" * 50)
print("SOLUTION 1: Basic Math Calculator")
print("=" * 50)

num1 = 15
num2 = 4

print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")


print("\n" + "=" * 50)
print("SOLUTION 2: Temperature Converter")
print("=" * 50)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temp_f = 68
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c:.2f}°C")


print("\n" + "=" * 50)
print("SOLUTION 3: Even or Odd Checker")
print("=" * 50)

for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


print("\n" + "=" * 50)
print("SOLUTION 4: Shopping Cart")
print("=" * 50)

shopping_cart = ["apples", "bread", "milk", "eggs", "cheese"]
print("Items in cart:")
for item in shopping_cart:
    print(f"- {item}")
print(f"\nTotal items: {len(shopping_cart)}")


print("\n" + "=" * 50)
print("SOLUTION 5: Student Grades")
print("=" * 50)

students = {
    "Alice": 92,
    "Bob": 87,
    "Charlie": 95,
    "Diana": 88
}

print("Student Grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")

average = sum(students.values()) / len(students)
print(f"\nAverage grade: {average:.2f}")


print("\n" + "=" * 50)
print("SOLUTION 6: FizzBuzz")
print("=" * 50)

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


print("\n" + "=" * 50)
print("SOLUTION 7: List Operations")
print("=" * 50)

numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

numbers.append(6)
numbers.append(7)
print("After adding 6 and 7:", numbers)

numbers.remove(3)
print("After removing 3:", numbers)


print("\n" + "=" * 50)
print("SOLUTION 8: Name Formatter")
print("=" * 50)

def format_name(first_name, last_name):
    return f"{last_name}, {first_name}"

print(format_name("John", "Doe"))
print(format_name("Jane", "Smith"))
print(format_name("Alice", "Johnson"))


print("\n" + "=" * 50)
print("GREAT JOB!")
print("=" * 50)
print("You've completed all the exercises!")
print("Keep practicing and building projects!")
