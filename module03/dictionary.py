#In this example, the keys are "apple", "banana", and "orange", and the corresponding values are 2, 4, and 1, respectively.
# dict{key:value}
my_dict = {"apple": 2, "banana": 4, "orange": 1}

#accessing the values with keys
my_dict["banana"]

#modification with dicts
my_dict["apple"] = 3  # Modifies the value associated with the key "apple"
my_dict["pear"] = 5  # Adds a new key-value pair to the dictionary
del my_dict["orange"]  # Deletes the key-value pair with the key "orange"

# loop with dict
for key, value in my_dict.items():
    print(key, value)
