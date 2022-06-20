## Introduction
For GIT (Github) testing only! Btc_bot is simple python bot for requesting btc price on demand. Even if btc price is not really actual thing now :)
## Current Releases
0.1 - Initial commit. <br />
## Platforms
Any Linux. Python3 and python-pip3 required. <br />
Required python libraries installation: <br />
```bash
pip3 install telebot
pip3 install pyTelegramBotAPI
```
If you have 
> AttributeError: 'TeleBot' object has no attribute 'message_handler'
error on launching bot: <br />
```bash
pip3 uninstall PyTelegramBotAPI
pip3 install pyTelegramBotAPI
pip3 install --upgrade pyTelegramBotAPI
```
## Usage
Rename default_config to config.py, provide your keys. <br />
Just launch it on any Linux system, no matter what internet connection(NAT or direct internet) you have. Also coinmarketcap (free) auth token and telegram bot token are required. <br />
Typical launch: *python btc_bot.py* or *python3 btc_bot.py*. You can run it in a background mode (*python btc_bot.py &*) or run in a screen (or tmux) window.
## How can I get coinmarketcap API key?
Its simple. Go to https://coinmarketcap.com/api/ and register. Now you can log on and create your free API key.
## How can I get telegram API key?
Install telegram and find BotFather in search window. Now type: <br />
/newbot <br />
Now enter the name and bot father will generate a key for you.<br />
Additionally you can set avatar for your bot: <br />
/setuserpic <br />
BotFather will as you for bot name. Enter you  bot's name from first step and press enter, then send any picture you like as photo (not like file).
## Config file
Configure setting in config.py: <br />
* tele_key * is your telegram bot api key <br />
* market_url * is coinmarketcap API backend for requesting crypto currencies price <br />
* market_key * is your coinmarketcap api key <br />
## Licenses
Use and modify on your own risk.
