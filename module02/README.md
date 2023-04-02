# INTRODUCTION 👋


## Functions 📝

Functions in Python are blocks of code that perform a specific task. They are reusable pieces of code that allow programmers to avoid writing the same code over and over again. Functions take one or more input arguments and return an output, making them a fundamental tool in building complex programs.

Functions in Python can be defined using the def keyword followed by the function name and input arguments. The body of the function is then indented below the function definition. Here's an example of a simple function that takes two input arguments and returns their sum:

```
def add_numbers(a, b):
    return a + b
```
Once a function has been defined, it can be called by passing the required arguments. The function is then executed and the output value is returned to the caller. Here's an example of how the add_numbers function can be called:

```
result = add_numbers(3, 5)
print(result)  # Output: 8
```

In addition to accepting input arguments, functions in Python can also return multiple values, and they can be nested within other functions.

Functions can make your code more modular and easier to read and maintain. By breaking up complex tasks into smaller, more manageable pieces of code, you can create more organized and scalable programs.


Refer to : [functions.py](https://github.com/MLSA-UETP/Python-for-beginners/blob/main/module02/functions.py)


## Loops <img src="https://github.com/MLSA-UETP/Python-for-beginners/blob/main/module02/GIFS/Loop.gif" alt="Logo" width="50" height="50" align="center">


In programming, loops are a way to execute a block of code repeatedly until a certain condition is met. They are essential in automating repetitive tasks and reducing code redundancy. There are two main types of loops in Python: for loops and while loops.

### 📌For Loop

for loops are used to iterate over a sequence of elements such as a list, tuple, or string. The loop variable takes on each element of the sequence in turn, and the code inside the loop body is executed for each iteration of the loop. The range() function is often used to generate a sequence of numbers to loop over.

```
for char in my_string:  # loop through each character in the string
    if char.isalpha():  # check if the character is an alphabet
        print("You can't spell", char.upper(), "without 'science'!")  # print a joke using the character
    else:
        print(char)  # print the character as it is if it is not an alphabet
```
#### Explanation
This code loops through each character in a given string and checks if the character is an alphabet using the .isalpha() method. If the character is an alphabet, it prints a joke saying "You can't spell [the uppercase character] without 'science'!". If the character is not an alphabet, it simply prints the character as it is.

### 📌While Loop
while loops, on the other hand, are used to execute a block of code repeatedly as long as a certain condition is met. The condition is checked at the beginning of each iteration of the loop, and the loop body is executed only if the condition is True.
```
while number_of_cats > 0:  # loop while the number of cats is greater than 0
    print("Why did the cat join the Red Cross? Because she wanted to be a first-aid kit!")  # print a joke
    number_of_cats -= 1  # decrease the number of cats by 1 in each iteration of the loop
```
#### Explanation
This code uses a while loop to iterate through a block of code as long as the number_of_cats is greater than 0. In each iteration of the loop, it prints a joke saying "Why did the cat join the Red Cross? Because she wanted to be a first-aid kit!". After printing the joke, it decreases the value of number_of_cats by 1.

In both types of loops, it is important to make sure that the condition for terminating the loop is eventually met, to avoid an infinite loop that could crash the program or cause other issues.


Refer to : [loops.py](https://github.com/MLSA-UETP/Python-for-beginners/blob/main/module02/loops.py)





<p align="center">Made with ❤️ by <a href="https://github.com/hasn20">Muhammad Hassaan</a></p>

