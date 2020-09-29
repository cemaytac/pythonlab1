# exercise-02 Length of Phrase
# Write the code that:
# Prompts the user to enter a phrase: Please enter a word or phrase:
# Print the following message:
# What you entered is xx characters long
# Return to step 1, unless the word 'quit' was entered.

while True:
    phrase_input = input('Please enter a word or phrase: ')
    if phrase_input == 'quit':
        break
    else:
        print(f'What you entered is {len(phrase_input)} characters long')
