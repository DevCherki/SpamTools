import random

# ANSI colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

# Input from user
country_code = input(f"{CYAN}Enter country code (e.g., +2126): {RESET}").strip()
file_name = input(f"{CYAN}Enter output file name (e.g., numbers.txt): {RESET}").strip()
number_length = int(input(f"{CYAN}Enter the number of digits after the country code (e.g., 8): {RESET}"))
amount = int(input(f"{CYAN}How many unique numbers do you want to generate? {RESET}"))

# Ensure .txt extension
if not file_name.endswith(".txt"):
    file_name += ".txt"

# Check max limit
max_possible = 10 ** number_length
if amount > max_possible:
    print(f"{RED}ERROR: You cannot generate more than {max_possible} unique numbers!{RESET}")
    exit()

# Generate unique numbers
numbers_set = set()
while len(numbers_set) < amount:
    random_number = ''.join([str(random.randint(0, 9)) for _ in range(number_length)])
    full_number = country_code + random_number
    numbers_set.add(full_number)

# Save to file
with open(file_name, "w") as file:
    for number in numbers_set:
        file.write(number + "\n")

# Output summary
print(f"\n{GREEN}Successfully generated {len(numbers_set)} unique phone numbers.{RESET}")
print(f"{YELLOW}Saved to file: {file_name}{RESET}")
