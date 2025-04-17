import random
import string
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# واجهة المستخدم
def show_interface():
    print(Fore.GREEN + Style.BRIGHT + '''
    *******************************************************
    *               Random Email Generator                *
    *             Developed by: Dev Cherki                *
    *                                                     *
    *   FACEBOOK : https://www.facebook.com/dev.cherki    *
    *   INSTAGRAM: https://www.instagram.com/dev.cherki   *
    *******************************************************
    ''')

# طباعة ملونة
def print_colored(text, color):
    print(color + text + Style.RESET_ALL)

# إنشاء إيميل عشوائي
def generate_email(name, domain):
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{name.lower()}{random_string}@{domain.lower()}"

# إنشاء الإيميلات وحفظها في ملف
def create_emails():
    show_interface()

    name = input(Fore.CYAN + "Enter the person's name (e.g., Tom or Ahmed): " + Style.RESET_ALL).strip()
    domain = input(Fore.CYAN + "Enter the domain (e.g., gmail.com or yahoo.com): " + Style.RESET_ALL).strip()
    count = int(input(Fore.CYAN + "How many emails would you like to create? " + Style.RESET_ALL).strip())
    save_path = input(Fore.CYAN + "Enter the file path to save the emails (e.g., emails.txt): " + Style.RESET_ALL).strip()

    # استخدام المسار الحالي إذا لم يتم تحديد مجلد
    if not os.path.dirname(save_path):
        save_path = os.path.join(os.getcwd(), save_path)

    directory = os.path.dirname(save_path)
    if not os.path.exists(directory):
        print_colored("The directory doesn't exist. Creating it now...", Fore.YELLOW)
        os.makedirs(directory)

    # إنشاء الإيميلات
    with open(save_path, 'w') as f:
        for _ in range(count):
            email = generate_email(name, domain)
            f.write(email + '\n')

    print_colored(f"{count} emails have been created and saved to: {save_path}", Fore.GREEN)

# تشغيل البرنامج
if __name__ == "__main__":
    create_emails()
