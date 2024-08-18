#Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.

a = int(input("Enter a number: "))  # a is variable for getting using user input value

# A number is even if division by 2 gives a remainder of 0.
if (a % 2) == 0:                     

   print("{0} is Even number".format(a))

    # If the remainder is 1, it is an odd number.
else:
   print("{0} is Odd number".format(a))