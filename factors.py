# Author: Matthew Armstrong
# Date: 6/29/21
# Description: program that determines the factors of a positive integer
user_input = int(input("Please enter a positive integer:"))
print("The factors of", user_input, "are:")
for factors in range(1, user_input+1):
    if user_input % factors == 0:
        print(factors)
