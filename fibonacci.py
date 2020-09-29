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

fibonacci = int(input("How many Fibonacci's would you like pal? "))

n1, n2 = 1, 1
count = 1

if fibonacci <= 0:
    print("D'yous not get the fibonacci? Positive numbahs ONLY bud!")
else:
    print("Comin' right up boss! ")
    while count < fibonacci:
        print(n1)
        res = n1 + n2
        n1 = n2
        n2 = res
        count += 1
