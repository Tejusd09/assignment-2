def main():
    print("Even or Odd Number Checker")
    print("---------------------------")
    
    try:
        # Take integer input from user
        num = int(input("Enter an integer: "))
        
        # Check if number is even or odd
        if num % 2 == 0:
            print(f"The number {num} is Even.")
        else:
            print(f"The number {num} is Odd.")
            
    except ValueError:
        print("Error: Please enter a valid integer!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()