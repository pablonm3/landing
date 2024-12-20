from flask import Flask, request, render_template, redirect, flash
import os
from telebot import TeleBot


app = Flask(__name__)


def send_telegram_msg(chat_id, bot_token, message, parse_mode="Markdown"):
    bot = TeleBot(bot_token, parse_mode=parse_mode) #FIXME: cache this in a class
    bot.send_message(chat_id, message)


@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(name, email, message)
        # Validate form data
        if not all([name, email, message]):
            return "Please fill in all fields", 400
        message = f"CONTACT FORM SUBMISSION!\nName: {name}\nEmail: {email}\nMessage: {message}"
        BOT_TOKEN = "7414823330:AAFP1euzmRExANrNjXC1_WdL1YcgAZ2RqtQ"
        CHAT_ID = "1157796625"
        send_telegram_msg(CHAT_ID, BOT_TOKEN, message)
        

        return "Form submitted successfully", 200

    except Exception as e:
        print(f"Error: {str(e)}")
        flash('An error occurred while sending the message', 'error')
        return "An error occurred while sending the message", 500


if __name__ == '__main__':
    app.run(debug=True)