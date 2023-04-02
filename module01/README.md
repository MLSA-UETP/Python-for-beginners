# INTRODUCTION
A common task is developing programs that can not only show information on a screen or a console, but also take input from users or even other programs. In this module, you'll build your first program in Python to learn how to handle input and output on the console. You'll also learn Python programming concepts, like variables and converting between data types.

# What will you learn?

In this module, you'll learn to:

 - Use functions to manage input and output to the console
 - Create variables to store data
 - Distinguish between data types
 - Use type conversion to convert between data types
 - Use conditional statements
 - importing modules/packages inside your python code

# Steps

## Create a Python file
To create a program in Python, you need to store it in a file. The file should have the extension .py.

The idea of a program is to do something or carry out a task. To have the program do something, you'll need to add the statements or instructions to perform the task. For example, an instruction could print some text or calculate something. 

## Let's say Hello to the World!
One of the first things you're likely to do is print to a console. On the console, you can run commands and programs. You can also enter information and show information as text on the screen.

To write information to the console, you can use the print() function and implement it as a core function. Because it's a core function, you'll have access to it if Python is installed. To use print() in your program, give it an argument.

Refer to [first_program.py](https://github.com/MLSA-UETP/Python-for-beginners/blob/main/module01/first_program.py) for code details.

## Declare Variables

To get anywhere with coding, you need to understand that you're operating on data. As your program is working on data, you might need to remember a certain value throughout the program's execution. For that, you use variables.

To get hands on variable refer to [variable.py](https://github.com/MLSA-UETP/Python-for-beginners/blob/main/module01/variable.py)


## Data Types

In Python, data types refer to the types of values that can be stored and manipulated in a program. Python is a dynamically typed language, which means that the data type of a variable is determined at runtime based on the value it is assigned.

Here are some of the commonly used data types in Python:

Integer: Integers are whole numbers, such as 1, 2, 3, -1, -2, -3. They are represented in Python using the int data type.

Float: Floats are decimal numbers, such as 3.14, 2.5, -0.1. They are represented in Python using the float data type.

Boolean: Booleans represent the truth value of a statement and can only be True or False. They are represented in Python using the bool data type.

String: Strings are a sequence of characters, such as "hello", "world", "123". They are represented in Python using the str data type.

### Data Type Conversion

The type() function has been used to determine the data type of each variable. In addition, data type conversion has been performed in the code to concatenate the Ramadan_day variable with the string "th" and the word "Ramadan".

### int to string

The Ramadan_day variable is an integer. In order to concatenate it with the string "th" and the word "Ramadan", it needs to be converted to a string using the str() function.

refer to data_types.py

## Assignment operators

Assignment operators in Python are used to assign values to variables. The basic assignment operator is "=", which assigns the value on the right side to the variable on the left side. For example, x = 5 assigns the value 5 to the variable x.

In addition to the basic assignment operator, there are also compound assignment operators, which combine the assignment operation with another operation. The most commonly used compound assignment operators are:

+=: adds the value on the right to the value of the variable on the left and assigns the result to the variable on the left. For example, x += 3 is equivalent to x = x + 3.
-=: subtracts the value on the right from the value of the variable on the left and assigns the result to the variable on the left. For example, x -= 2 is equivalent to x = x - 2.
*=: multiplies the value on the right with the value of the variable on the left and assigns the result to the variable on the left. For example, x *= 4 is equivalent to x = x * 4.
/=: divides the value of the variable on the left by the value on the right and assigns the result to the variable on the left. For example, x /= 2 is equivalent to x = x / 2.
%=: calculates the remainder of the division of the value of the variable on the left by the value on the right and assigns the result to the variable on the left. For example, x %= 3 is equivalent to x = x % 3.
Compound assignment operators are a shorthand way to write expressions that involve both an assignment and another operation. They can make code more concise and easier to read.

## Importing packages in python

In Python, a package is a collection of modules that provide related functionality. Importing packages allows you to access the modules and functions contained within them.

To import a package in Python, you use the import keyword followed by the name of the package

For instance the code demonstrates how to use the "import" command to bring in the "datetime" library in Python.

The "datetime" library is a standard library in Python and provides classes for working with dates and times. In this code, we are importing the "datetime" library to use the "date" class which allows us to get today's date.

After importing the "datetime" library, we call the "date.today()" method to get the current date and store it in the "today_date" variable. Finally, we print the value of "today_date" using the "print()" function.

Importing libraries/packages in Python allows developers to access a wide range of functionality that is not available in the core Python language.

link to a vast range of python packages: https://pypi.org/


refer to package_import.py

## Conditional Statements

In Python, conditional statements are used to execute specific code blocks based on certain conditions. There are three types of conditional statements in Python: if, elif, and else.

The basic structure of an if statement is:


if condition:
    statement(s)
Here, condition is a Boolean expression that is either True or False. If the condition is True, then the statement(s) indented under the if statement are executed.

An elif statement is used to add additional conditions after an if statement. The basic structure of an elif statement is:


if condition1:
    statement(s)
elif condition2:
    statement(s)
Here, if the condition1 is False, then the condition2 is checked. If condition2 is True, then the statement(s) indented under the elif statement are executed.

An else statement is used to execute a block of code if none of the previous conditions were True. The basic structure of an else statement is:


if condition1:
    statement(s)
elif condition2:
    statement(s)
else:
    statement(s)

Here, if both condition1 and condition2 are False, then the statement(s) indented under the else statement are executed.

Conditional statements are commonly used in decision-making processes in programs. They can be used for everything from simple decisions to complex decision trees.








