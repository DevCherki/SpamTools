import random
import string
import os
from colorama import Fore, init

# Initialize colorama for terminal color support
init(autoreset=True)

# Function to generate a random email
def generate_email(name, domain):
    # Generate a random string for uniqueness
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    email = f"{name.lower()}{random_string}@{domain.lower()}"
    return email

# Main function to create emails
def create_emails():
    # Collect user input
    print(Fore.CYAN + "Hello! Let's help you create emails.")
    name = input(Fore.YELLOW + "Enter the person's name (e.g., Tom or Ahmed): ")
    domain = input(Fore.YELLOW + "Enter the domain (e.g., gmail.com or yahoo.com): ")
    count = int(input(Fore.YELLOW + "How many emails would you like to create? "))
    save_path = input(Fore.YELLOW + "Enter the file path to save the emails (e.g., C:/emails.txt): ")

    # If the user only entered the file name (no directory), use the current directory
    if not os.path.dirname(save_path):
        save_path = os.path.join(os.getcwd(), save_path)

    # Check if the directory exists, if not, create it
    directory = os.path.dirname(save_path)
    if not os.path.exists(directory):
        print(Fore.YELLOW + "The directory doesn't exist. Creating it now...")
        os.makedirs(directory)

    # Generate emails and save them to the file
    with open(save_path, 'w') as f:
        for _ in range(count):
            email = generate_email(name, domain)
            f.write(email + '\n')

    print(Fore.GREEN + f"{count} emails have been created and saved to {save_path}.")

# Run the function to create emails
if __name__ == "__main__":
    create_emails()
