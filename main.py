import os
import sys

# ANSI Colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"
MAGENTA = "\033[35m"

# ASCII Art for "Cherki Spam"
NAME_ART = """
 CCCC H   H EEEEE RRRR  K   K IIII    SSS  PPPP   AAAAA  M   M
C     H   H E     R   R K  K   I     S     P   P  A   A  MM MM
C     HHHHH EEEE  RRRR  KKK    I      SSS  PPPP   AAAAA  M M M
C     H   H E     R  R  K  K   I         S P      A   A  M   M
 CCCC H   H EEEEE R   R K   K IIII    SSS  P      A   A  M   M
"""

def print_header():
    print(f"{MAGENTA}==============================================================")
    print(f"{CYAN}{NAME_ART}{RESET}")
    print(f"{CYAN}       Created by Cherki - All Rights Reserved")
    print(f"{CYAN}       Contact: Facebook/Instagram/GitHub    ")
    print(f"{CYAN}       Facebook: dev.cherki                 ")
    print(f"{CYAN}       Instagram: dev.cherki                ")
    print(f"{CYAN}       GitHub: devcherki                    ")
    print(f"{MAGENTA}==============================================================\n")

def run_script(script_name):
    """Run the selected script."""
    script_path = os.path.join("tools", script_name)
    if os.path.exists(script_path):
        print(f"{CYAN}Running {script_name}...{RESET}")
        os.system(f"python {script_path}")
    else:
        print(f"{RED}Error: {script_name} not found!{RESET}")

def main():
    print_header()

    # Menu
    print(f"{CYAN}Choose an option:{RESET}")
    print(f"{GREEN}1. Spam SMS{RESET}")
    print(f"{GREEN}2. Generate Random Phone Numbers{RESET}")
    print(f"{GREEN}3. Spam Email{RESET}")
    print(f"{GREEN}4. Generate Random Emails{RESET}")

    choice = input(f"{CYAN}Enter your choice (1-4): {RESET}")

    if choice == "1":
        run_script("spamsms.py")
    elif choice == "2":
        run_script("randomnum.py")
    elif choice == "3":
        run_script("spamemail.py")
    elif choice == "4":
        run_script("randomemail.py")
    else:
        print(f"{RED}Invalid choice. Exiting...{RESET}")

if __name__ == "__main__":
    main()
