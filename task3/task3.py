import random
import string

def generate_password():
    # Define possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(8))
    return password

def main():
    print(" Welcome to the Password Generator ")
    
    try:
        password = generate_password()
        print(f"\n Generated Password: {password}")
    except ValueError:
        print(" Invalid input. Please enter a number.")

# Run the program
main()
