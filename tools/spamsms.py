import os
import time
from colorama import Fore, Style, init

# تهيئة colorama لتنسيق الألوان
init(autoreset=True)

# واجهة المستخدم
def show_interface():
    print(Fore.GREEN + Style.BRIGHT + '''
    *******************************************************
    *             Spam-SMS Tool                           *
    *         Developed by: Dev Cherki                    *
    *                                                     *
    *   Contact Me:                                       *
    *   Facebook: https://www.facebook.com/dev.cherki     *
    *   Instagram: https://www.instagram.com/dev_cherki   *
    *******************************************************
    ''')

# إرسال الرسائل النصية عبر Termux API
def send_sms(file_path, message):
    try:
        # قراءة الأرقام من الملف
        with open(file_path, "r") as file:
            numbers = file.readlines()

        # إرسال الرسائل النصية باستخدام Termux API
        for number in numbers:
            number = number.strip()  # إزالة المسافات البيضاء
            if number:  # التأكد من أن الرقم غير فارغ
                # إرسال الرسالة
                os.system(f'termux-sms-send -n {number} "{message}"')
                print(Fore.YELLOW + f"تم إرسال الرسالة إلى: {number}")
                time.sleep(1)  # تأخير بسيط بين الرسائل لإعطاء الوقت

    except FileNotFoundError:
        print(Fore.RED + f"لم يتم العثور على الملف: {file_path}")
    except Exception as e:
        print(Fore.RED + f"حدث خطأ: {str(e)}")

# عرض واجهة المستخدم وبدء إرسال الرسائل
def main():
    show_interface()  # عرض الواجهة
    
    # طلب إدخال مسار الملف من المستخدم
    file_path = input(Fore.CYAN + "أدخل مسار ملف الأرقام (مثل: /sdcard/Download/data.txt): ").strip()
    
    # طلب إدخال الرسالة من المستخدم
    message = input(Fore.CYAN + "أدخل نص الرسالة: ").strip()

    # بدء إرسال الرسائل
    send_sms(file_path, message)

# تنفيذ السكربت
if __name__ == "__main__":
    main()
