# exercise-01 Vowel or Consonant
# Write the code that:
# Prompts the user to enter a letter in the alphabet: Please enter a letter from the alphabet (a-z or A-Z):
# Write the code that determines whether the letter entered is a vowel
# Print one of following messages (substituting the letter for x):
# The letter x is a vowel
# The letter x is a consonant
# Hints: Use the in operator to check if a character is in another string For example, if some_char in 'abc':

letter_input = input(
    'Please enter a letter from the alphabet(upper or lowercase):')
vowels = ['a', 'e', 'i', 'o', 'u']

if letter_input == vowels:
    print('The letter {letter_input} is a vowel')
else:
    print('The letter {letter_input} is a consonant')

# exercise-02 Length of Phrase
# Write the code that:

# Prompts the user to enter a phrase: Please enter a word or phrase:
# Print the following message:
# What you entered is xx characters long
# Return to step 1, unless the word 'quit' was entered.
# exercise-03 Calculate Dog Years
# Write the code that:

# Prompts the user to enter a dog's age in human years like this: Input a dog's age in human years:
# Calculates the equivalent dog years, where:
# The first two years count as 10 years each
# Any remaining years count as 7 years each
# Prints the answer in the following format: The dog's age in dog years is xx
# Hint: Use the int() function to convert the string returned from input() into an integer

# exercise-04 What kind of Triangle?
# Write the code that:

# Prompts the user to enter the three lengths of a triangle (one at a time): Enter the lengths of three side of a triangle: a: b: c:
# Write the code that determines if the triangle is: equalateral - all three sides are equal in length scalene - all three sides are unequal in length isosceles - two sides are the same length
# Print a message such as:
# A triangle with sides of , & is a triangle
# exercise-05 Fibonacci sequence for first 50 terms
# Write the code that:

# Calculates and prints the first 50 terms of the fibonacci sequence.
# Print each term and number as follows:
#   term: 1 / number: 1
#   term: 2 / number: 1
#   term: 3 / number: 2
#   term: 4 / number: 3
#   term: 5 / number: 5```
#   etc.

# Hint: The next number is found by adding the two numbers before it

# exercise-06 What's the Season?
# Write the code that:

# Prompts the user to enter the month (as three characters): Enter the month of the year (Jan - Dec):
# Then prompts the user to enter the day of the month: Enter the day of the month:
# Calculate what season it is based upon this chart: Dec 21 - Mar 19: Winter Mar 20 - Jun 20: Spring Jun 21 - Sep 21: Summer Sep 22 - Dec 20: Fall
# Print the result as follows:
# is in
# Hints: Consider using the in operator to check if a string is in a particular list/tuple like this: if input_month in ('Jan', 'Feb', 'Mar'):

# After setting the likely season, you can use another if...elif...else statement to "adjust" if the day number falls within a certain range.
