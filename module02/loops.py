# While loop with a silly condition
number_of_cats = 3  # initialize the number of cats to 3

while number_of_cats > 0:  # loop while the number of cats is greater than 0
    print("Why did the cat join the Red Cross? Because she wanted to be a first-aid kit!")  # print a joke
    number_of_cats -= 1  # decrease the number of cats by 1 in each iteration of the loop

# For loop with a play on words
my_string = "Why don't scientists trust atoms? Because they make up everything."  # initialize a string variable

for char in my_string:  # loop through each character in the string
    if char.isalpha():  # check if the character is an alphabet
        print("You can't spell", char.upper(), "without 'science'!")  # print a joke using the character
    else:
        print(char)  # print the character as it is if it is not an alphabet

# Nested loop with a joke
for i in range(3):  # loop 3 times
    for j in range(3):  # loop 3 times for each iteration of the outer loop
        print("Why don't oysters share their pearls? Because they're shellfish!")  # print a joke
    print("That's a real pearl of wisdom, don't you think?")  # print a comment after each iteration of the outer loop

# While loop with a pun
my_bool = True  # initialize a boolean variable to True

while my_bool:  # loop while the boolean variable is True
    print("I'm reading a book about teleportation. It's bound to take me places!")  # print a pun
    my_bool = False  # set the boolean variable to False to exit the loop after one iteration
