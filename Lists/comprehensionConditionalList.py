list1 = [-3,-2,-1,0,1,2,3]
list2 = [number for number in list1 if number > 0]
print(list1)
print(list2)

sentence = "I am Madhu"

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

print(is_consonant('a'))
print(is_consonant('t'))

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)

prev_list = [-3,-2,-1,0,1,2,3]
new_list = [number if number >= 0 else 'neg' for number in prev_list]
print(new_list)

def get_number(number):
    if number >= 0: 
        return number
    else:
        return 'negative'
    
new_list1 = [get_number(number) for number in prev_list]
print(new_list1)