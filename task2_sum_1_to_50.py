def main():
    print("Sum of Integers from 1 to 50")
    print("----------------------------")
    
    # Initialize sum to 0
    total_sum = 0
    
    print("Calculating sum...")
    
    # Use for loop to iterate from 1 to 50
    for number in range(1, 51):
        total_sum += number
        # Optional: Show progress (comment out for cleaner output)
        # print(f"Adding {number}, Current sum: {total_sum}")
    
    print("\nResult:")
    print(f"The sum of all integers from 1 to 50 is: {total_sum}")
    
    # Additional verification using formula
    formula_sum = 50 * (50 + 1) // 2
    print(f"Verification using formula (n*(n+1)/2): {formula_sum}")
    
    if total_sum == formula_sum:
        print("✓ Calculation verified successfully!")

if __name__ == "__main__":
    main()