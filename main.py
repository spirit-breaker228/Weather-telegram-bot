import telebot
import requests
import json

bot = telebot.TeleBot("Your TOKEN")
APIs = "b9bc8793228544bd7dc866696d93d7e2"


@bot.message_handler(commands=["start"])
def start(message):
    """Select weather"""
    bot.send_message(message.chat.id, "Send your city")


@bot.message_handler(content_types="text")
def weather_in_city(message):
    """Send weather"""
    city = message.text.strip().lower()
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIs}"
    )
    if response.status_code == 200:
        data = json.loads(response.text)
        bot.reply_to(
            message,
            f"{city.title()} weather: \n Sky: {data['weather'][0]['description']} \n temp: {data['main']['temp']} celsius \n Feels like: {data['main']['feels_like']} celius \n Wind: {data['wind']['speed']} m/s",
        )
    else:
        bot.reply_to(message, "Wrong city")


bot.infinity_polling()
