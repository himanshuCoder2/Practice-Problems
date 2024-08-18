import random

class MultipleProgram:
    def main(self):
        while True:
            # Display the menu of available programs
            print("\n1. Palindrome\n2. Armstrong\n3. Fibonacci\n4. Prime Number")
            print("5. Even or Odd\n6. Factorial\n7. Swap Two Numbers\n8. Generate Random Number\n9. Exit")
            num = int(input("Which program do you want to execute? :- "))

            # Execute the corresponding function based on user input
            if num == 1:
                self.palindrome()
            elif num == 2:
                self.armstrong()
            elif num == 3:
                self.fibonacci()
            elif num == 4:
                self.prime_number()
            elif num == 5:
                self.even_or_odd()
            elif num == 6:
                self.factorial()
            elif num == 7:
                self.swap_numbers()
            elif num == 8:
                self.generate_random_number()
            elif num == 9:
                print("Exiting program.")
                break
            else:
                print("Invalid input")

    def palindrome(self):
        # Check if a number is a palindrome
        n = int(input("Enter number: "))
        temp = n
        sum = 0
        while n > 0:
            sum = sum * 10 + n % 10
            n = n // 10
        if temp == sum:
            print(f"{temp} is a Palindrome number")
        else:
            print(f"{temp} is not a Palindrome number")

    def armstrong(self):
        # Check if a number is an Armstrong number
        num = int(input("Enter a number: "))
        n = len(str(num))
        temp = num
        sum = 0
        while temp > 0:
            digit = temp % 10
            sum += digit ** n
            temp = temp // 10
        if num == sum:
            print(f"{num} is an Armstrong Number")
        else:
            print(f"{num} is not an Armstrong Number")

    def fibonacci(self):
        # Generate a Fibonacci sequence up to the nth term
        n = int(input("Enter the value of n: "))
        num1, num2 = 0, 1
        print(num1, num2, end=" ")
        for _ in range(2, n):
            num3 = num1 + num2
            print(num3, end=" ")
            num1, num2 = num2, num3
        print()

    def prime_number(self):
        # Check if a number is prime
        num = int(input("Enter a number: "))
        is_prime = True
        if num <= 1:
            is_prime = False
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
        if is_prime:
            print(f"{num} is a Prime Number")
        else:
            print(f"{num} is not a Prime Number")

    def even_or_odd(self):
        # Check if a number is even or odd
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is Even number")
        else:
            print(f"{num} is Odd number")

    def factorial(self):
        # Calculate the factorial of a number
        num = int(input("Enter a number: "))
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print(f"Factorial of  given {num} is {fact}")

    def swap_numbers(self):
        # Swap two numbers
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"Before swap: num1 = {num1}, num2 = {num2}")
        num1, num2 = num2, num1
        print(f"After swap: num1 = {num1}, num2 = {num2}")

    def generate_random_number(self):
        # Generate a random number between 1 and 100
        random_number = random.randint(1, 100)
        print(f"Generated Random Number: {random_number}")

# Create an instance of the class and execute the main function
if __name__ == "__main__":
    program = MultipleProgram()
    program.main()
