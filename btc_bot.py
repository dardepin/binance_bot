#!/usr/bin/python3

import json
import telebot
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from config import *;

bot = telebot.TeleBot(tele_key)

def parse_data(records):
    if(len(records) > 0):
        #for record in records:
        data = records["data"][0]["quote"]["USD"];
        name = records["data"][0]["name"]
        price = data['price']
        updated = data['last_updated']
        p1h = data['percent_change_1h']
        p24 = data['percent_change_24h']
        p7d = data['percent_change_7d']
        return name + "\nprice: " + str(price) + "\nupdated: " + updated + "\n1 hour change: " + str(p1h) + "%\n24 hour change: " + str(p24) + "%\n7 days change: " + str(p7d) + "%\n"
    else:
        return "no records"
    #and print
    return

def http_error(code):
    if (code == 400):
        msg = "400 (Bad Request)\n"
    if(code == 401):
        msg = "401 (Unauthorized)\n"
    if(code == 402):
        msg = "402 (Payment Required)\n"
    if(code == 403):
        msg = "403 (Forbidden)\n"
    if(code == 429):
        msg = "429 (Too Many Requests)\n"
    if(code == 500):
        msg = "500 (Internal Server Error)\n"
    return msg

@bot.message_handler(commands=['btc'])
def command_btc(m):
    parameters = { 'start':'1', 'limit':'1', 'convert':'USD' }
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': market_key,}
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(market_url, params = parameters)
        if(response.status_code != 200):
            bot.send_message(m.chat.id, http_error(response.status_code));
        #http_ok
        data = json.loads(response.text)
        bot.send_message(m.chat.id, parse_data(data))
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        bot.send_message(m.chat.id, e) #print(e)

#echo available commands
@bot.message_handler(func=lambda message: message.text == "/help")
def command_text_hi(m):
    bot.send_message(m.chat.id, "Available commands:\n /btc\t Bitcoin course\n")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    # this is the standard reply to a normal message
    bot.send_message(m.chat.id, "I don't understand \"" + m.text + "\"\nMaybe try the help at /help")

bot.polling()