import os
import pywhatkit as kit
from twilio.rest import Client
import subprocess
import smtplib
import psutil
import requests
from art import text2art
import pyttsx3
from googlesearch import search
from telegram import Bot
from instabot import Bot
import facebook
import discord

def text_to_speech(text, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)  # Set the speed of speech
    engine.say(text)
    engine.runAndWait()

def send_whatsapp_message():
    number = input("Enter the recipient's number (with country code): ")
    message = input("Enter the message: ")
    hour = int(input("Enter the hour (24-hour format): "))
    minute = int(input("Enter the minute: "))
    kit.sendwhatmsg(number, message, hour, minute)

def speak_output():
    message = input("Enter the message to be spoken: ")
    text_to_speech(message, rate=165)
    print(message)

def send_email():
    sender = "riteshsahanibirgunj@gmail.com"
    receiver = input("Enter the recipient's email: ")
    subject = input("Enter the subject: ")
    body = input("Enter the body of the email: ")

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login("riteshsahanibirgunj@gmail.com", "aopi qxya birl jdzx")  # Use your app password here
        smtp.sendmail(sender, receiver, message)

def send_sms():
    account_sid = 'ACbf74d130a476e0b28e50938810f2838e'
    auth_token = '998271b07af10decd12844b4e0e07a4e'
    client = Client(account_sid, auth_token)
    to = input("Enter the recipient's number (with country code): ")
    from_ = '+14157893575'
    body = input("Enter the message: ")
    client.messages.create(to=to, from_=from_, body=body)

def post_to_social_media():
    platform = input("Enter the platform (telegram/instagram/facebook/discord): ").lower()
    message = input("Enter the message to post: ")
    if platform == 'telegram':
        token = input("Enter your Telegram bot token: ")
        chat_id = input("Enter the chat ID: ")
        bot = Bot(token=token)
        bot.send_message(chat_id=chat_id, text=message)
        print("Message posted to Telegram.")
        pass
        
    elif platform == 'instagram':
        username = input("Enter your Instagram username: ")
        password = input("Enter your Instagram password: ")
        bot = Bot()
        bot.login(username=username, password=password)
        bot.upload_photo("path/to/your/image.jpg", caption=message)
        print("Message posted to Instagram.")
        pass
        
    elif platform == 'facebook':
        access_token = input("Enter your Facebook access token: ")
        graph = facebook.GraphAPI(access_token=access_token)
        graph.put_object(parent_object='me', connection_name='feed', message=message)
        print("Message posted to Facebook.")
        pass
        
    elif platform == 'discord':
        token = input("Enter your Discord bot token: ")
        channel_id = int(input("Enter the channel ID: "))
        
        # Create an instance of Intents
        intents = discord.Intents.default()
        intents.message_content = True  # Enable the message_content intent
        
        # Create an instance of Client with intents
        client = discord.Client(intents=intents)
        pass
        
    else:
        print("Unsupported platform")

def change_file_folder_colors():
    os.system('LS_COLORS="di=1;35" && export LS_COLORS')

def read_ram():
    print(psutil.virtual_memory())

def change_gnome_terminal_look():
    profile = input("Enter the GNOME Terminal profile name: ")
    os.system(f'dconf write /org/gnome/terminal/legacy/profiles:/:{profile}/background-color ":red/"')

def run_linux_in_browser():
    os.system('jupyter notebook')

def google_search():
    query = input("Enter the search query: ")
    for result in search(query, tld="com", num=10, stop=10, pause=2):
        print(result)

def run_windows_software():
    software = input("Enter the Windows software to run: ")
    os.system(f'wine {software}')

def sync_folders():
    folder1 = input("Enter the first folder path: ")
    folder2 = input("Enter the second folder path: ")
    os.system(f'rsync -av --progress {folder1} {folder2}')

def print_ascii_art():
    text = input("Enter the text to convert to ASCII art: ")
    print(text2art(text))

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Send WhatsApp Message")
        print("2. Speak Output")
        print("3. Send Email")
        print("4. Send SMS")
        print("5. Post to Social Media")
        print("6. Change File/Folder Colors")
        print("7. Read RAM")
        print("8. Change GNOME Terminal Look")
        print("9. Create User and Set Password")
        print("10. Run Linux in Browser")
        print("11. Google Search")
        print("12. Run Windows Software")
        print("13. Sync Folders")
        print("14. Print ASCII Art")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            send_whatsapp_message()
        elif choice == '2':
            speak_output()
        elif choice == '3':
            send_email()
        elif choice == '4':
            send_sms()
        elif choice == '5':
            post_to_social_media()
        elif choice == '6':
            change_file_folder_colors()
        elif choice == '7':
            read_ram()
        elif choice == '8':
            change_gnome_terminal_look()
        elif choice == '9':
            create_user_set_password()
        elif choice == '10':
            run_linux_in_browser()
        elif choice == '11':
            google_search()
        elif choice == '12':
            run_windows_software()
        elif choice == '13':
            sync_folders()
        elif choice == '14':
            print_ascii_art()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
