# INTRODUCTION
 "add some good intro for this module explaining what will be covered"


 ## LIST

A list is defined using square brackets ([]) and can contain any type of values, including numbers, strings, other lists, or even objects. Here's an example of how to create a list:

```
my_list = [1, 2, 3, "four", "five"]
```

You can access individual elements in a list by their index, which starts at 0 for the first element. For example, to access the first element in the list above, you would use my_list[0], which would return the value 1. You can also use negative indices to access elements from the end of the list. For example, my_list[-1] would return the last element in the list, which is "five".

You can also modify elements in a list by their index or add new elements using various methods. Here are some examples:


my_list[1] = 10  # Modifies the second element in the list
my_list.append(6)  # Adds the value 6 to the end of the list
my_list.insert(2, "three")  # Inserts the value "three" at index 2
my_list.remove("four")  # Removes the first occurrence of the value "four" from the list
Lists are also useful for iterating over a collection of values using a loop, such as a for loop or a while loop. Here's an example of how to use a for loop to print out each element in a list:


for element in my_list:
    print(element)

This would print out the values 1, 10, "three", "five", and 6, each on a separate line.

## Dictionary

Dictionaries are another important data type in Python, which are used to store collections of key-value pairs. Here's an overview of how to use dictionaries in Python:

A dictionary is defined using curly braces ({}) and consists of a series of key-value pairs, separated by commas. Here's an example:


my_dict = {"apple": 2, "banana": 4, "orange": 1}

In this example, the keys are "apple", "banana", and "orange", and the corresponding values are 2, 4, and 1, respectively.

You can access the values in a dictionary by their keys, using the square bracket notation. For example, my_dict["banana"] would return the value 4.

You can also modify values in a dictionary or add new key-value pairs using various methods. Here are some examples:


my_dict["apple"] = 3  # Modifies the value associated with the key "apple"
my_dict["pear"] = 5  # Adds a new key-value pair to the dictionary
del my_dict["orange"]  # Deletes the key-value pair with the key "orange"

Dictionaries are also useful for iterating over the keys or values in a dictionary using a loop, such as a for loop or a while loop. Here's an example of how to use a for loop to print out each key-value pair in a dictionary:


for key, value in my_dict.items():
    print(key, value)

This would print out each key-value pair, with the key and value separated by a space, each on a separate line.

## Tuple

Tuples are another important data type in Python, which are similar to lists but are immutable, meaning they cannot be modified once they are created. Here's an overview of how to use tuples in Python:

A tuple is defined using parentheses (()) and consists of a series of values, separated by commas. Here's an example:


my_tuple = (1, 2, 3, 4)

In this example, my_tuple contains the values 1, 2, 3, and 4.

You can access the values in a tuple using indexing, just like with lists. For example, my_tuple[0] would return the value 1.

However, you cannot modify the values in a tuple or add new values to it. Once a tuple is created, its contents cannot be changed. If you try to modify a tuple, you will get a TypeError error.

Tuples are useful when you want to create a collection of values that should not be modified, such as the coordinates of a point or the RGB values of a color.

You can also use tuples for unpacking, which is a way to assign the values in a tuple to separate variables. Here's an example:


my_tuple = (1, 2, 3)
a, b, c = my_tuple

In this example, a will be assigned the value 1, b will be assigned the value 2, and c will be assigned the value 3. This can be useful for returning multiple values from a function or for assigning variables in a concise way.

## Error Handling
Error handling in Python refers to the process of anticipating and handling errors or exceptions that may occur during program execution. When a program encounters an error, it raises an exception, which is an object that represents an error or unexpected condition. Python provides a number of tools for handling these exceptions, which can help your program to continue running even in the presence of errors.

The most common way to handle exceptions in Python is to use a try/except block. Here's how it works:

```
try:
    # some code that might raise an exception
except ExceptionType:
    # code to handle the exception
```

In this example, the code inside the try block is executed, and if it raises an exception of the type ExceptionType, then the code inside the except block is executed instead. The except block can include code to handle the exception in some way, such as printing an error message or taking some corrective action.

You can also use multiple except blocks to handle different types of exceptions, like this:


try:
    # some code that might raise an exception
except ExceptionType1:
    # code to handle ExceptionType1
except ExceptionType2:
    # code to handle ExceptionType2
except:
    # code to handle any other type of exception

In this example, the first except block handles exceptions of ExceptionType1, the second except block handles exceptions of ExceptionType2, and the final except block handles any other type of exception that might occur.

You can also use a finally block to specify code that should always be executed, regardless of whether an exception was raised. For example:


try:
    # some code that might raise an exception
except ExceptionType:
    # code to handle the exception
finally:
    # code to execute whether or not an exception was raised

In this example, the code inside the finally block is executed whether or not an exception was raised inside the try block.

