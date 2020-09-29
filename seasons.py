# exercise-06 What's the Season?
# Write the code that:
# Prompts the user to enter the month (as three characters): Enter the month of the year (Jan - Dec):
# Then prompts the user to enter the day of the month: Enter the day of the month:
# Calculate what season it is based upon this chart: Dec 21 - Mar 19: Winter Mar 20 - Jun 20: Spring Jun 21 - Sep 21: Summer Sep 22 - Dec 20: Fall
# Print the result as follows:
# is in
# Hints: Consider using the in operator to check if a string is in a particular list/tuple like this: if input_month in ('Jan', 'Feb', 'Mar'):

# After setting the likely season, you can use another if...elif...else statement to "adjust" if the day number falls within a certain range.


month = input("Enter the month of the year (Jan-Dec): ")
day = int(input("Enter the day of the month: "))
month_input = month.lower()
all_months = ['jan', 'feb', 'mar', 'apr', 'may',
              'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

if month_input in all_months:
    if month_input == 'dec' or month_input == 'jan' or month_input == 'feb' or month_input == 'mar':
        if month_input == 'dec' and day >= 21 or month_input == 'mar' and day <= 19:
            print(f"You are in winter.")
        elif month_input == 'mar' and day > 19:
            print("You are in spring")
        elif month_input == 'dec' and day < 21:
            print("You are in fall")
        else:
            print("You are in winter")
    elif month_input == 'apr' or month_input == 'may' or month_input == 'jun':
        if month_input == 'jun' and day > 20:
            print(f'You are in summer')
        else:
            print("You are in spring")
    elif month_input == 'jul' or month_input == 'aug' or month_input == 'sep':
        if month_input == 'sep' and day > 21:
            print(f"You are in fall")
        else:
            print("You are in summer")
    elif month_input == 'oct' or month_input == 'nov':
        print("You are in fall")

else:
    print("Please enter one of the 3-letter months: 'jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec' and then today's date")
