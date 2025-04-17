import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# واجهة المستخدم
def show_interface():
    print(Fore.GREEN + Style.BRIGHT + '''
    *******************************************************
    *                 Spam-Mail Tool                      *
    *            Developed by: Dev Cherki                 *
    *                                                     *
    *   FACEBOOK : https://www.facebook.com/dev.cherki    *
    *   INSTAGRAM: https://www.instagram.com/cherki.dev   *
    *******************************************************
    ''')

# طباعة ملونة
def print_colored(text, color):
    print(color + text + Style.RESET_ALL)

# ألوان جاهزة
GREEN = Fore.GREEN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
YELLOW = Fore.YELLOW + Style.BRIGHT
CYAN = Fore.CYAN + Style.BRIGHT
BLUE = Fore.BLUE + Style.BRIGHT

# عرض الواجهة
show_interface()

# إدخال البيانات من المستخدم
email = input(CYAN + "Enter your email address: " + Style.RESET_ALL).strip()
password = input(CYAN + "Enter your App Password (for Gmail): " + Style.RESET_ALL).strip()
txt_file_path = input(CYAN + "Enter path to text file with emails list: " + Style.RESET_ALL).strip()
html_file_path = input(CYAN + "Enter path to HTML file with the message: " + Style.RESET_ALL).strip()
subject = input(CYAN + "Enter the email subject: " + Style.RESET_ALL).strip()

# قراءة قائمة البريد
try:
    with open(txt_file_path, "r") as txt_file:
        receivers = txt_file.read().split()
except FileNotFoundError:
    print_colored(f"ERROR: File not found: {txt_file_path}", RED)
    exit()

# قراءة محتوى HTML
try:
    with open(html_file_path, "r") as html_file:
        html_content = html_file.read()
except FileNotFoundError:
    print_colored(f"ERROR: File not found: {html_file_path}", RED)
    exit()

# إرسال الإيميلات
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)

    for receiver in receivers:
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = email
        msg["To"] = receiver

        html_part = MIMEText(html_content, "html")
        msg.attach(html_part)

        server.sendmail(email, receiver, msg.as_string())
        print_colored(f"Email sent successfully to {receiver}", GREEN)

    server.quit()
    print_colored("All emails have been sent successfully!", BLUE)

except smtplib.SMTPAuthenticationError:
    print_colored("Authentication failed. Please check your email and app password.", RED)

except Exception as e:
    print_colored(f"An error occurred: {e}", RED)
