# Python program to display multiplication tables with a menu-based interface

while True:
    print("\n=== Multiplication Table Program ===")
    print("1. Enter a number for the multiplication table")
    print("2. Enter the next number for a new multiplication table")
    print("3. Go back to the first step")
    print("4. Exit the program")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1' or choice == '2':
        # Entering a number to generate the multiplication table
        number = int(input("Enter the number for the multiplication table: "))
        print(f"\nMultiplication Table for {number}:\n")
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
    
    elif choice == '3':
        # Go back to the first step
        print("\nReturning to the first step...\n")
        continue
    
    elif choice == '4':
        # Exit the program
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please select a valid option.")
