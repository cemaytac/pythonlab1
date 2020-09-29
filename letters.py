# exercise-01 Vowel or Consonant
# Write the code that:
# Prompts the user to enter a letter in the alphabet: Please enter a letter from the alphabet (a-z or A-Z):
# Write the code that determines whether the letter entered is a vowel
# Print one of following messages (substituting the letter for x):
# The letter x is a vowel
# The letter x is a consonant
# Hints: Use the in operator to check if a character is in another string For example, if some_char in 'abc':

letter_input = input(
    'Please enter a letter from the alphabet(upper or lowercase): ')

vowels = ['a', 'e', 'i', 'o', 'u']

if letter_input.isalpha() and len(letter_input) == 1:
    if letter_input in vowels:
        print(f'Your letter is a vowel')
    else:
        print(f'Your letter is a consonant')
else:
    print('enter ONE LETTER please!')