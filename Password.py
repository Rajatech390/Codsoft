import random
import string

# Function to generate password
def generate_password(length):
    # Define character sets
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choice
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Main function to get user input and generate password
def main():
    # Ask user for password length
    length = int(input("Enter the desired length of your password: "))
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated Password:", password)

# Run the main function
if __name__ == "__main__":
    main()
