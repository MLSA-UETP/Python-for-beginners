  # INTRODUCTION
 
In this module, we will discuss three essential data types in Python: lists, dictionaries, and tuples. Lists are used to store a collection of items in an ordered sequence, and they can contain any type of value. Dictionaries are used to store collections of key-value pairs, with keys mapping to values. Tuples are similar to lists but are immutable, meaning that their values cannot be modified after creation. We will cover how to create and modify these data types, how to access their values, and how to iterate over them using loops.

<br>

 ##  LIST:

A list is a powerful tool in Python that enables you to store a collection of items in a single, ordered sequence. Lists are defined using square brackets `[ ]` and can contain any type of value, from numbers and strings to other lists and objects

### CREATING A LIST🔖

To create a list, use square brackets with each element separated by a comma.<br>
**For example:**
```
my_list = [1, 2, 3, "four", "five"]
```

### ACCESSING ELEMENTS🔖

📌 You can access individual elements in a list by their index, which starts at 0 for the first element.<br>
**For example,**<br>To access the first element in the list above, you would use `my_list[0]`, which would return the value 1.<br><br>
📌 You can also use negative indices to access elements from the end of the list.<br>
**For example,**<br>To access the last element in the list above, you would use `my_list[-1]`, which would return the last element in the list, which is "five".<br>


### MODIFYING AND ADDING ELEMENTS🔖

You can modify elements in a list by their index or add new elements using various methods.<br>
**Here are some examples:**
```
my_list[1] = 10 
my_list.append(6) 
my_list.insert(2, 
my_list.remove("four") 
```

📑 The **1st** line of code, **modifies** the **second element** in the list.<br>
📑 The **2nd** line of code, **adds** the **value 6** to the **end** of the list.<br>
📑 The **3rd** line of code, **inserts** the value **"three"** at **index 2**.<br>
📑 The **4th** line of code, **removes** the **first occurrence** of the value **"four"** from the list.<br>

### ITERATING OVER A LIST🔖

One of the most powerful features of lists is the ability to iterate over them using a loop. This allows you to perform the same operation on every element in the list.
<br>
**Here's an example of how to use a for loop to print out each element in a list:**
```
for element in my_list:
    print(element)
```

<br>

```
1
2
3
four
five
```
**RESULT:**
This would print out the values 1, 10, "three", "five", and 6, each on a separate line.

<br><br>

## DICTIONARY:

Dictionaries are an essential data type in Python that allow you to store collections of key-value pairs. Here's a brief overview of how dictionaries are used in Python.

### CREATING A DICTIONARY🔖

A dictionary is defined using curly braces ` { } ` and consists of a series of key-value pairs, separated by commas
<br> 
**Here's an example:**
```
my_dict = {"apple": 2, "banana": 4, "orange": 1}
```
**In the above example**, `"apple"`, `"banana"`, and `"orange"` are **keys**, and `2`, `4`, and `1` are their corresponding **values**.

### ACCESSING VALUES IN A DICTIONARY🔖

You can access values in a dictionary using their keys with square brackets.
<br>
**For example**, to retrieve the value associated with the key `"banana"`, you would write:
```
my_dict["banana"]
```
**RESULTS:**
This would return the value `4`.

### MODIFYING DICTIONARIES🔖
You can modify the values of a dictionary or add new key-value pairs using various methods.
<br>
**Here are some examples:**
```
my_dict["apple"] = 3
```
📌 Modifies the value associated with the key "apple"
```
my_dict["pear"] = 5
```
📌 Adds a new key-value pair to the dictionary
```
del my_dict["orange"]
```
📌 Deletes the key-value pair with the key "orange"

### ITERATING OVER A DICTIONARY🔖

Dictionaries are useful for iterating over their keys or values using a loop, such as a for loop or a while loop.
<br>
Here's an **example** of how to use a for loop to print out each key-value pair in a dictionary:

```
for key, value in my_dict.items():
    print(key, value)
```
**RESULT:** This would print out each key-value pair, with the key and value separated by a space, each on a separate line.

<br>
<br>

## TUPLE:

Tuples are one of the built-in data types in Python, which are similar to lists but are immutable. In simple terms, tuples are a collection of values that cannot be modified once they are created.
<br>
Here's an **overview** of how tuples are used in Python.

### DEFINING A TUPLE🔖

Tuples are defined using parentheses `()` and a series of values separated by commas.
<br>
Here's an **example:**
```
my_tuple = (1, 2, 3, 4)
```

In this **example**, `my_tuple` contains the values `1`, `2,` `3`, and `4`.

### ACCESSING TUPLE VALUES🔖

You can access the values in a tuple using indexing, just like with lists.
<br>

For **example**:
```
my_tuple[0]
```
**RESULT:** This would return the value `1`.

### MODIFYING TUPLES🔖

Unlike lists, tuples cannot be modified once they are created.
```
my_tuple[0] = 5
```
**Attempting** to modify a tuple will result in a `TypeError`.

📌 Tuples are useful when you want to create a collection of values that should not be modified, such as the coordinates of a point or the RGB values of a color.

### UNPACKING TUPLES🔖

Tuples can be used for unpacking, which allows us to assign the values in a tuple to separate variables.
<br>
Here's an **example**:
```
my_tuple = (1, 2, 3)
a, b, c = my_tuple
```

In this **example**,
<br>
`a` will be assigned the value `1`, `b` will be assigned the value `2`, and `c` will be assigned the value `3`. 
<br>
<br>
📌 This can be useful for returning multiple values from a function or for assigning variables in a concise way.

<br>
<br>

## ERROR HANDLING:

Error handling in Python refers to the process of anticipating and handling errors or exceptions that may occur during program execution.
<br>
When a program encounters an error, it raises an exception, which is an object that represents an error or unexpected condition.
<br>
Python provides a number of tools for handling these exceptions, which can help your program to continue running even in the presence of errors.

### TRY/EXCEPT BLOCK🔖

The most common way to handle exceptions in Python is to use a try/except block.
<br>
Here's how it **works**:

```
try:
```
📌 Some code that might raise an exception
```
except ExceptionType:
```
📌 Code to handle the exception

In this **example,** 
<br>
📑 The code inside the `try` block is executed, and if it raises an exception of the type `ExceptionType`, then the code inside the `except` block is executed instead.
<br>
📑 The `except` block can include code to handle the exception in some way, such as printing an error message or taking some corrective action.
<br>
<br>
**🏷You can also use multiple `except` blocks to handle different types of exceptions, like this:**
```
try:
```
📌 Some code that might raise an exception
```
except ExceptionType1:
```
📌 Code to handle ExceptionType1
```
except ExceptionType2:
```
📌 Code to handle ExceptionType2
```
except:
```
📌 Code to handle any other type of exception

<br>

In this **example**,
<br>
📑 The first `except` block handles exceptions of `ExceptionType1`.
<br>
📑 The second `except` block handles exceptions of `ExceptionType2`.
<br>
📑 The final `except` block handles any other type of exception that might occur.

### FINALLY BLOCK🔖

You can also use a `finally` block to specify code that should always be executed, regardless of whether an exception was raised.
<br>
For **example:**
```
try:
```
📌 Some code that might raise an exception
```
except ExceptionType:
```
📌 Code to handle the exception
```
finally:
```
📌 Code to execute whether or not an exception was raised

In this **Example**,
<br>
The code inside the `finally` block is executed whether or not an exception was raised inside the `try` block.

<br><br>

**<p align="center">Made with 🤍 by <a href="https://github.com/saadshah8">Muhammad Saad Ali Shah</a></p>**
