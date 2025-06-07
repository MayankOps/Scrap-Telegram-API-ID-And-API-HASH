# 🤖 Telegram Scrap API ID And API Hash

![image](https://github.com/user-attachments/assets/99b9ec06-733a-4afc-b11e-ed88447e86c2)

## 🚀 Overview
The ** Telegram Scrap API ID And API Hash** is a powerful tool designed to help users easily retrieve their Telegram API credentials. Built using Python, this bot leverages the Telebot library for seamless interaction with the Telegram API and BeautifulSoup for web scraping to extract necessary information from the Telegram website.

## ✨ Features
- 📝 **User Registration**: Automatically registers users when they start interacting with the bot.
- 📱 **Phone Number Input**: Prompts users to enter their phone number for authentication.
- 🔑 **Code Verification**: Sends a verification code to the user's Telegram and allows them to input it for login.
- 🛠️ **API Credentials Retrieval**: Scrapes the Telegram website to retrieve the API ID, API Hash, Public Key, and Production Configuration.
- 📢 **Broadcast Messaging**: Allows the admin to send messages to all registered users.

## ⚙️ Installation

### Prerequisites
- 🐍 Python 3.10+
- 🍃 MongoDB (local or Atlas)


### Steps
1. **Clone the Repository**:
   ```
   git clone https://github.com/MayankOps/Scrap-Telegram-API-ID-And-API-HASH
   cd Scrap-Telegram-API-ID-And-API-HASH
   ```

2. **Install Required Packages**:
   Use pip to install the necessary libraries:
   ```
   pip install -r requirements.txt
   ```

3. **Configure the Bot**:
   - Open `config.py` and replace the `BOT_TOKEN` with your Telegram bot token.
   - Set the `ADMIN_ID` to your Telegram user ID.
   - Update the `MONGO_URI` if you are using a remote MongoDB instance.

4. **Run the Bot**:
   Execute the bot script:
   ```
   python bot.py
   ```

## 🕹️ Usage
- Start the bot by sending the `/start` command in your Telegram chat.
- Follow the prompts to enter your phone number and verification code.
- Use the `/scrid` command to retrieve your Telegram API credentials.
- Admin users can use the `/broadcast` command to send messages to all registered users.

---

## 💼 Project Details
- **Author**: Mayank Patil

This project showcases my understanding of Python programming and API integration for secure user authentication. 🎓

---

## 📞 Contact Details

- **Email**: ‎[contactmayank@aol.com](mailto:contactmayank@aol.com)

---

## 🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to submit a pull request.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🙏 Acknowledgments
- [Telebot](https://github.com/eternnoir/pyTelegramBotAPI) for the Telegram bot framework.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for web scraping capabilities.
