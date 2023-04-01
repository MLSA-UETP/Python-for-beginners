try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print("The result is:", y)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: You must enter a number!")
