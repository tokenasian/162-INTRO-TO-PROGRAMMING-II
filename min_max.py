# Author: Matthew Armstrong
# Date: 6/29/21
# Description: program that determines the min and max of a value
print("How many integers would you like to enter?")
user_input = int(input())
print("Please enter", user_input, "integers.")
min_value = 0
max_value = 0
for i in range(user_input):
    user_input = int(input())
    if user_input > max_value:
        max_value = user_input
    if user_input < min_value:
        min_value = user_input
print("min:", min_value)
print("max:", max_value)