Ramadan_day = 12

# Fairy Tale Character
superhero = "Spiderman"  # string

# Mythical Creature
ghost = True  #boolean

# Magical Element
wizard_wand = 13.5  # float


# to see the data type of any variable use type() function
print(type(Ramadan_day))
print(type(superhero))
print(type(ghost))
print(type(wizard_wand))

#concatination
# print("Today is " + Ramadan_day + "th"+ "Ramadan") # this line qill give you error - uncomment and try it
# to get rid of this error - you can do type conversion
# Let's look at data type conversion


#converting int to string 
#str(Ramadan_day)
print("Today is " + str(Ramadan_day) + "th "+ "Ramadan")