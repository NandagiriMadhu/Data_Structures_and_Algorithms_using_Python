# Initializing list1 with numbers from -3 to 3
list1 = [-3, -2, -1, 0, 1, 2, 3]

# Creating list2 with only positive numbers from list1 using list comprehension
list2 = [number for number in list1 if number > 0]
print(list1)  # Output: [-3, -2, -1, 0, 1, 2, 3]
print(list2)  # Output: [1, 2, 3]

# Defining a function to check if a letter is a consonant
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

# Testing the is_consonant function with different letters
print(is_consonant('a'))  # Output: False (because 'a' is a vowel)
print(is_consonant('t'))  # Output: True (because 't' is a consonant)

# Creating a list of consonants from the sentence using the is_consonant function
sentence = "I am Madhu"
consonants = [i for i in sentence if is_consonant(i)]
print(consonants)  # Output: ['m', 'M', 'd', 'h'] (the consonants from "I am Madhu")

# Creating a new list by replacing negative numbers with 'neg'
prev_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [number if number >= 0 else 'neg' for number in prev_list]
print(new_list)  # Output: ['neg', 'neg', 'neg', 0, 1, 2, 3]

# Defining a function that returns a number or 'negative' for negative numbers
def get_number(number):
    if number >= 0:
        return number
    else:
        return 'negative'

# Using list comprehension to apply the get_number function on prev_list
new_list1 = [get_number(number) for number in prev_list]
print(new_list1)  # Output: ['negative', 'negative', 'negative', 0, 1, 2, 3]
