import telebot
from telebot import types
import requests
import json

# 5958778313:AAGUgvbS-3hOnkoNYnRhawBO04vWBlUVImk
TOKEN = "5958778313:AAGUgvbS-3hOnkoNYnRhawBO04vWBlUVImk"

start_point = "fff"
last_point = " "
bot = telebot.TeleBot(TOKEN)
try:

	@bot.message_handler(commands=["start"])
	def start_welcome(message):
		try:
			keyboard = types.InlineKeyboardMarkup()
			key_start = types.InlineKeyboardButton(text= "🌏 START 🌎", callback_data= "start")
			keyboard.add(key_start)
			key_help = types.InlineKeyboardButton(text= "🤔 HELP 🧐", callback_data= "help")
			keyboard.add(key_help)
			info = "🏦 Привет, я бот-конвертер 💹™"
			bot.send_message(message.from_user.id, text= info, reply_markup= keyboard)
		except ValueError:
			instruction = "🟥 Введите команду /start для начала 🟥"
			bot.send_message(message.from_user.id, text=instruction)

	@bot.callback_query_handler(func=lambda call:True)
	def callback_worker(call):
		try:
			if call.data == "start":
				keyboard = types.InlineKeyboardMarkup()
				rub_start_key = types.InlineKeyboardButton(text="🇷🇺 RUB 🇷🇺", callback_data="RUB")
				keyboard.add(rub_start_key)
				eu_start_key = types.InlineKeyboardButton(text="🇪🇺 EURO 🇪🇺", callback_data="EUR")
				keyboard.add(eu_start_key)
				dollars_start_key = types.InlineKeyboardButton(text="🇺🇲 USD 🇺🇲", callback_data="USD")
				keyboard.add(dollars_start_key)
				bot.send_message(call.message.chat.id, text="① ➡ Выберите валюту с которой нужно перевести. ➡", reply_markup=keyboard)
			elif call.data == "help":
				keyboard = types.InlineKeyboardMarkup()
				key_start = types.InlineKeyboardButton(text="✅ ДА ✅", callback_data="start")
				keyboard.add(key_start)
				key_help = types.InlineKeyboardButton(text="❓❓НЕ ЗНАЮ ❓❓", callback_data="help")
				keyboard.add(key_help)
				info = "Я бот-конвертер, провожу обмен денежной единицы одной страны на деньги другой по текущему курсу.\nДоступны: \n🗿 Eвро - EUR (€)\n🗽 Доллары - USD ($)\n🪆 Рубли - RUB (₽)\nПродолжим?"
				bot.send_message(call.message.chat.id, text=info, reply_markup=keyboard)
			elif call.data == "RUB" or call.data == "EUR" or call.data == "USD":
				x = second_choose(call)
				global start_point
				start_point = call.data
				return x, start_point
			elif call.data == "rub_last" or call.data == "euro_last" or call.data == "dollars_last":
				# bot.send_message(call.message.chat.id, "Введите сумму")
				# last_point = call
				numb = choose(call)
				return numb
		except KeyError:
			pass

	@bot.callback_query_handler(func=lambda call:True)
	def second_choose(call):
		try:
			if call.data == "RUB" or call.data == "EUR" or call.data == "USD":
				keyboard = types.InlineKeyboardMarkup()
				rub_last_key = types.InlineKeyboardButton(text="🇷🇺RUB 🇷🇺", callback_data="rub_last")
				keyboard.add(rub_last_key)
				eu_last_key = types.InlineKeyboardButton(text="🇪🇺 EURO 🇪🇺", callback_data="euro_last")
				keyboard.add(eu_last_key)
				dollars_last_key = types.InlineKeyboardButton(text="🇺🇲 USD 🇺🇲", callback_data="dollars_last")
				keyboard.add(dollars_last_key)
				bot.send_message(call.message.chat.id, text="② ⬇ Выберите на какую валюту нужно поменять ⬇", reply_markup=keyboard)
		except KeyError:
			pass

	def choose(call):
		if call.data == "rub_last" or call.data == "euro_last" or call.data == "dollars_last":
			bot.send_message(call.message.chat.id, "③ Введите сумму")
			global last_point
			if call.data == "rub_last":
				last_point = "RUB"
			elif call.data == "euro_last":
				last_point = "EUR"
			elif call.data == "dollars_last":
				last_point = "USD"
			# print(last_point)
			return last_point

	@bot.message_handler(content_types = ["text"])
	def convert(message: telebot.types.Message):
		try:
			amount = message.text
			r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={start_point}&tsyms={last_point}")
			total_base = json.loads(r.content)[last_point]
			text = f"Цена {amount} {start_point} в {last_point} - {total_base * int(amount)} {last_point}\nДля того чтобы начать сначала нажмите - /start"
			bot.send_message(message.chat.id, text)
		except KeyError or ValueError:
			bot.send_message(message.chat.id, "Введите пожалуйста число\nИли нажмите на эту ссылку для того чтобы начать заново")
		except requests.exceptions.ReadTimeout:
			print("\n Переподключение к серверам \n")

except requests.exceptions.ReadTimeout:
	print("Переподключение к серверам заново")


bot.polling(none_stop= True)