import telebot
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from config import BOT_TOKEN, ADMIN_ID, MONGO_URI, MONGO_DB_NAME

# Setup
bot = telebot.TeleBot(BOT_TOKEN)
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB_NAME]
users_col = db["registered_users"]

user_sessions = {}  # Temporary login sessions

# -- Utility Functions --
def register_user(user_id):
    if not users_col.find_one({"user_id": user_id}):
        users_col.insert_one({"user_id": user_id})

def get_all_user_ids():
    return [doc["user_id"] for doc in users_col.find()]

# -- Handlers --

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    register_user(chat_id)
    bot.send_message(chat_id, "👋 Welcome! Use /scrid to extract your Telegram API credentials.")

@bot.message_handler(commands=['scrid'])
def handle_scrid(message):
    chat_id = message.chat.id
    register_user(chat_id)
    bot.send_message(chat_id, "📲 Please enter your phone number (with country code, e.g., +98xxxx):")
    bot.register_next_step_handler(message, process_phone)

def process_phone(message):
    chat_id = message.chat.id
    phone = message.text.strip()
    user_sessions[chat_id] = {'phone': phone}

    try:
        req = requests.Session()
        response = req.post('https://my.telegram.org/auth/send_password', data={'phone': phone})
        if 'too many tries' in response.text.lower():
            bot.send_message(chat_id, "⚠️ Too many attempts. Please try again later.")
            return

        data = response.json()
        user_sessions[chat_id]['random_hash'] = data['random_hash']
        user_sessions[chat_id]['session'] = req

        bot.send_message(chat_id, "📩 Code sent to your Telegram. Please enter the login code:")
        bot.register_next_step_handler(message, process_code)
    except Exception as e:
        bot.send_message(chat_id, f"❌ Failed to send code. Error: {e}")

def process_code(message):
    chat_id = message.chat.id
    code = message.text.strip()

    if chat_id not in user_sessions:
        bot.send_message(chat_id, "⏳ Session expired. Please use /scrid again.")
        return

    session_data = user_sessions[chat_id]
    phone = session_data['phone']
    random_hash = session_data['random_hash']
    req = session_data['session']

    login_data = {
        'phone': phone,
        'random_hash': random_hash,
        'password': code
    }

    try:
        req.post('https://my.telegram.org/auth/login', data=login_data)
        apps_page = req.get('https://my.telegram.org/apps')
        soup = BeautifulSoup(apps_page.text, 'html.parser')

        api_id = soup.find('label', string='App api_id:').find_next_sibling('div').select_one('span').get_text()
        api_hash = soup.find('label', string='App api_hash:').find_next_sibling('div').select_one('span').get_text()


        msg = (
            "✅ *Telegram API Credentials Retrieved:*\n\n"
            f"`API ID:` `{api_id}`\n\n"
            f"`API Hash:` `{api_hash}`\n\n"

            "🔗 Bot By t.me/VexoCloud"
        )
        bot.send_message(chat_id, msg, parse_mode="Markdown")
    except Exception as e:
        bot.send_message(chat_id, f"❌ Unable to retrieve credentials. Error: {e}")

@bot.message_handler(commands=['broadcast'])
def broadcast_command(message):
    if message.chat.id != ADMIN_ID:
        bot.send_message(message.chat.id, "🚫 You are not authorized to use this command.")
        return
    bot.send_message(message.chat.id, "📢 Send the message you want to broadcast:")
    bot.register_next_step_handler(message, send_broadcast)

def send_broadcast(message):
    success, fail = 0, 0
    for user_id in get_all_user_ids():
        try:
            bot.send_message(user_id, f"📣 *Broadcast Message:*\n\n{message.text}", parse_mode="Markdown")
            success += 1
        except:
            fail += 1
    bot.send_message(message.chat.id, f"✅ Sent to {success} users.\n❌ Failed for {fail} users.")

bot.polling()
