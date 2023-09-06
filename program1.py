
import random
#we'll oftem import libraries like this that provide finctionality.

x = input("pick a number between 1 and 100: ")
# Utilize the built-in input function to ask the user a questio
# Set the value of x to the user typed value

y = random.randint(1,100)
# Ultilize the built-in function to generate a random number between 1-100
# Save this value to the variable y

print("You picked " + x + " and the number " + str(y) + " was generated")
# Print the two values using a regular string

print(f"You picked {x} and the number generated was {y}".format(x,y))
# print the two values using an fstring this time

if int(x) < y:
    print("Too Low60!")
if int(x) > y:
    print("too High")
if int(x) == y:
    print ("Correct!")