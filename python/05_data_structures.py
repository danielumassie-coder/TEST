"""
Lesson 5: Data Structures - Lists and Dictionaries
===================================================

Data structures help organize and store multiple pieces of data.
Lists and dictionaries are the most commonly used in Python.

What you'll learn:
- Lists (ordered collections)
- Dictionaries (key-value pairs)
- Common operations on both
"""

# ==================
# LISTS
# ==================

# Creating a list
fruits = ["apple", "banana", "cherry", "orange"]
print("Fruits:", fruits)

# Accessing items by index (starts at 0)
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])  # Negative index from end

# Adding items
fruits.append("grape")
print("After adding grape:", fruits)

# Removing items
fruits.remove("banana")
print("After removing banana:", fruits)

# List length
print("Number of fruits:", len(fruits))

# Checking if item exists
if "apple" in fruits:
    print("We have apples!")

# Looping through a list
print("\nAll fruits:")
for fruit in fruits:
    print("-", fruit)

# List with numbers
numbers = [10, 20, 30, 40, 50]
print("\nNumbers:", numbers)
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))

# Slicing lists
print("First 3 fruits:", fruits[0:3])
print("Last 2 fruits:", fruits[-2:])

# ==================
# DICTIONARIES
# ==================

# Creating a dictionary (key-value pairs)
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "occupation": "Engineer"
}

print("\nPerson:", person)

# Accessing values by key
print("Name:", person["name"])
print("Age:", person["age"])

# Adding new key-value pairs
person["email"] = "alice@email.com"
print("After adding email:", person)

# Modifying values
person["age"] = 26
print("After birthday:", person)

# Checking if key exists
if "name" in person:
    print("Name is present in dictionary")

# Getting all keys
print("\nAll keys:", person.keys())

# Getting all values
print("All values:", person.values())

# Looping through dictionary
print("\nPerson details:")
for key, value in person.items():
    print(f"{key}: {value}")

# ==================
# COMBINING LISTS AND DICTIONARIES
# ==================

# List of dictionaries
students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Charlie", "grade": 92}
]

print("\nStudent grades:")
for student in students:
    print(f"{student['name']}: {student['grade']}")

# Dictionary with lists
menu = {
    "breakfast": ["eggs", "toast", "coffee"],
    "lunch": ["salad", "sandwich", "juice"],
    "dinner": ["pasta", "chicken", "wine"]
}

print("\nLunch options:", menu["lunch"])

# ==================
# PRACTICAL EXAMPLES
# ==================

# Shopping list
shopping_list = []
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")

print("\nShopping list:")
for item in shopping_list:
    print("- [ ]", item)

# Phone book
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

print("\nPhone book:")
for name, number in phone_book.items():
    print(f"{name}: {number}")

# ==================
# EXERCISES
# ==================

# 1. Create a list of your 5 favorite movies
favorite_movies = ["Movie1", "Movie2", "Movie3", "Movie4", "Movie5"]
print("\nMy favorite movies:")
for movie in favorite_movies:
    print("-", movie)

# 2. Create a dictionary with your personal info (name, age, hobby)
my_info = {
    "name": "Your Name",
    "age": 25,
    "hobby": "Reading"
}
print("\nMy info:", my_info)

# 3. Create a list of 3 dictionaries representing books (title, author, year)
books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
]

print("\nBooks:")
for book in books:
    print(f"{book['title']} by {book['author']} ({book['year']})")

# Your turn! Create your own data structures below:
