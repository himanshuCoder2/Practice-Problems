def is_prime(num):
  """Checks if a number is prime."""

  # Handle edge cases
  if num <= 1:
    return False
  if num <= 3:
    return True

  # Check divisibility by 2 and 3
  if num % 2 == 0 or num % 3 == 0:
    return False

  # Check divisibility by numbers of the form 6k ± 1 up to the square root of num
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6

  return True

# Get user input
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
  print(number, "is a prime number")
else: 

  print(number, "is not a prime number") 
