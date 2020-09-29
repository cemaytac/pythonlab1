# exercise-04 What kind of Triangle?
# Write the code that:
# Prompts the user to enter the three lengths of a triangle (one at a time): Enter the lengths of three side of a triangle: a: b: c:
# Write the code that determines if the triangle is: equalateral - all three sides are equal in length scalene - all three sides are unequal in length isosceles - two sides are the same length
# Print a message such as:
# A triangle with sides of , & is a triangle


a, b, c = [int(a) for a in input(
    "Enter the lengths of three sides of a triangle: ").split()]
print("a: ", a)
print("b: ", b)
print("c: ", c)
print()

if a == b == c:
    print(f"An equalateral triangle with sides of {a},{b},{c}.")
elif a == b or a == c or b == c:
    print(f"An isosceles triangle with sides of {a},{b},{c}.")
else:
    print(f"A scalene triangle with sides of {a},{b},{c}.")
