# demo_code.py

# Importing necessary modules
import random

# Function to generate a random number and return it
def generate_random_number(min_value, max_value):
    """Returns a random number between min_value and max_value."""
    return random.randint(min_value, max_value)

# Function to calculate the factorial of a number
def factorial(n):
    """Returns the factorial of a number."""
    if n == 0:
        return 1
    return n * factorial(n-1)

# Class to demonstrate basic object-oriented programming (OOP)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Main program logic
if __name__ == "__main__":
    # Print a welcome message
    print("Welcome to the Python Demo Code!")

    # Generate a random number between 1 and 100
    random_number = generate_random_number(1, 100)
    print(f"Random number generated: {random_number}")

    # Calculate and print the factorial of a number
    num = 5
    print(f"The factorial of {num} is: {factorial(num)}")

    # Create an instance of the Person class
    person = Person("Alice", 30)
    print(person.greet())

    # Demonstrating error handling with try-except
    try:
        # This will raise a ZeroDivisionError
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: You can't divide by zero!")
