sentence = input("Enter a sentence: ")
sentence = sentence.lower()

# Initialize variables to keep track of the counts for each vowel and consonant
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
count_consonants = 0

# Use a for loop to iterate over each character in the sentence
for letter in sentence:
    if letter in ['a', 'A']:
        count_a += 1
    elif letter in ['e', 'E']:
        count_e += 1
    elif letter in ['i', 'I']:
        count_i += 1
    elif letter in ['o', 'O']:
        count_o += 1
    elif letter in ['u', 'U']:
        count_u += 1
    elif letter.isalpha():
        count_consonants += 1

# Print out the counts for each vowel and consonant
print("Number of a's:", count_a)
print("Number of e's:", count_e)
print("Number of i's:", count_i)
print("Number of o's:", count_o)
print("Number of u's:", count_u)
print("Number of consonants:", count_consonants)
