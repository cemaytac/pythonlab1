# exercise-03 Calculate Dog Years
# Write the code that:
# Prompts the user to enter a dog's age in human years like this: Input a dog's age in human years:
# Calculates the equivalent dog years, where:
# The first two years count as 10 years each
# Any remaining years count as 7 years each
# Prints the answer in the following format: The dog's age in dog years is xx
# Hint: Use the int() function to convert the string returned from input() into an integer

dog_age_input = int(input("Input a dog's age in human years: "))


def dog_years_func(human_years):
    if (human_years <= 2) and (human_years > 0):
        dog_years = human_years * 10
    elif human_years > 2:
        dog_years = ((human_years - 2) * 7) + 20

    print(f"The dog's age in dog years is {dog_years}.")


print(dog_years_func(dog_age_input))
