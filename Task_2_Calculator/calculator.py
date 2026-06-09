def main():
    print("--- Simple Python Calculator ---")
    
    # 1. Prompt user for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("\nError: Invalid input! Please enter numerical values only.")
        return

    # 2. Display operation choices
    print("\nSelect an Operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    # 3. Prompt user for operation choice
    choice = input("\nEnter your choice (1/2/3/4): ")

    # 4. Perform calculation and display result
    print("\n--- Result ---")
    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is undefined.")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Invalid operation selected.")
    print("--------------")

if __name__ == "__main__":
    # Loop to allow multiple calculations
    while True:
        main()
        cont = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if cont != 'yes' and cont != 'y':
            print("Exiting calculator. Goodbye!")
            break