import random
import string

def generate_password(length, use_numbers=True, use_symbols=True):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
        
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def main():
    print("--- Advanced Password Generator ---")
    try:
        length = int(input("Enter the desired length for your password (e.g., 12): "))
        if length <= 0:
            print("Error: Password length must be greater than 0.")
            return
    except ValueError:
        print("Error: Invalid input! Please enter a numerical value.")
        return

    print("\nConfigure Complexity:")
    use_numbers = get_yes_no_input("Include numbers? (y/n): ")
    use_symbols = get_yes_no_input("Include special symbols (!@#$)? (y/n): ")

    secure_password = generate_password(length, use_numbers, use_symbols)
    
    print("\nGenerating...")
    print(f"Your secure password is: {secure_password}")
    print("-----------------------------------")

if __name__ == "__main__":
    while True:
        main()
        cont = get_yes_no_input("\nGenerate another password? (y/n): ")
        if not cont:
            print("Exiting generator. Stay secure!")
            break