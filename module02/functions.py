# Function that returns the sum of two numbers
def add_numbers(a, b):
    return a + b

# Function that returns the average of a list of numbers
def average(numbers):
    if len(numbers) == 0:
        return None  # Return None if the list is empty
    return sum(numbers) / len(numbers)

# Function that checks if a number is even or odd
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Function that prints a joke
def tell_joke():
    print("Why do programmers prefer dark mode? Because light attracts bugs!")

# Function that calculates the area of a circle
def calculate_area(radius):
    pi = 3.14159
    return pi * radius ** 2




# Calling the add_numbers function
result = add_numbers(3, 5)  # Call the function with the arguments 3 and 5
print(result)  # Prints 8, which is the sum of 3 and 5

# Calling the average function
numbers = [2, 5, 8, 10, 4]  # Create a list of numbers
result = average(numbers)  # Call the function with the list of numbers as argument
print(result)  # Prints 5.8, which is the average of the numbers in the list

# Calling the is_even function
result = is_even(7)  # Call the function with the argument 7
print(result)  # Prints False, because 7 is odd

# Calling the tell_joke function
tell_joke()  # Call the function, which prints the joke to the console

# Calling the calculate_area function
result = calculate_area(2.5)  # Call the function with the argument 2.5
print(result)  # Prints 19.6349375, which is the area of a circle with radius 2.5