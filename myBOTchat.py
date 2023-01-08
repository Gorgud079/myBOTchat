import telebot
from telebot import types
import requests


# 5958778313:AAGUgvbS-3hOnkoNYnRhawBO04vWBlUVImk
TOKEN = "5958778313:AAGUgvbS-3hOnkoNYnRhawBO04vWBlUVImk"
first_number = 0
last_number = 0
start_point = "rus"
bot = telebot.TeleBot(TOKEN)
# valut = {
# 	"rub" : {
# 		"dollars": 0.01,
# 		"euro" : 0.01},
# 	"euro" : {
# 		"dollars": 1.08,
# 		"rub": 75.66},
# 	"dollars": {
# 		"euro": 0.93,
# 		"rub": 70.34}
# }
# r = requests.get("https://www.banki.ru/products/currency/cb/")
# print(dir(r))
# with open("index.html", "w") as file:
# 	file.write(r.text)

@bot.message_handler(commands=["start"])
def start_welcome(message):
	keyboard = types.InlineKeyboardMarkup()
	key_start = types.InlineKeyboardButton(text= "START", callback_data= "start")
	keyboard.add(key_start)
	key_help = types.InlineKeyboardButton(text= "HELP", callback_data= "help")
	keyboard.add(key_help)
	info = "Здравствуйте, я бот-конвертер"
	bot.send_message(message.from_user.id, text= info, reply_markup= keyboard)


@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
	try:
		if call.data == "start":
			keyboard = types.InlineKeyboardMarkup()
			rub_start_key = types.InlineKeyboardButton(text="RUB", callback_data="rub")
			keyboard.add(rub_start_key)
			eu_start_key = types.InlineKeyboardButton(text="EURO", callback_data="euro")
			keyboard.add(eu_start_key)
			dollars_start_key = types.InlineKeyboardButton(text="DOLLARS", callback_data="dollars")
			keyboard.add(dollars_start_key)
			bot.send_message(call.message.chat.id, text="Выберите валюту с которой нужно перевести.", reply_markup=keyboard)
		elif call.data == "help":
			keyboard = types.InlineKeyboardMarkup()
			key_start = types.InlineKeyboardButton(text="ДА", callback_data="start")
			keyboard.add(key_start)
			key_help = types.InlineKeyboardButton(text="НЕ ЗНАЮ", callback_data="help")
			keyboard.add(key_help)
			info = "Я бот-конвертер, провожу обмен денежной единицы одной страны на деньги другой по текущему курсу. Доступны: евро, доллары и рубли. Продолжим?"
			bot.send_message(call.message.chat.id, text=info, reply_markup=keyboard)
		elif call.data == "rub" or call.data == "euro" or call.data == "dollars":
			x = second_choose(call)
			start_point = call
			return call, x, start_point
	except KeyError:
		pass


# @bot.callback_query_handler(func=lambda call: True)
def second_choose(call):
	try:
		if call.data == "rub" or call.data == "euro" or call.data == "dollars":
			keyboard = types.InlineKeyboardMarkup()
			rub_last_key = types.InlineKeyboardButton(text="RUB", callback_data="rub_last")
			keyboard.add(rub_last_key)
			eu_last_key = types.InlineKeyboardButton(text="EURO", callback_data="euro_last")
			keyboard.add(eu_last_key)
			dollars_last_key = types.InlineKeyboardButton(text="DOLLARS", callback_data="dollars_last")
			keyboard.add(dollars_last_key)
			bot.send_message(call.message.chat.id, text="Выберите на какую валюту поменять", reply_markup=keyboard)
			last_point = call
			number = price(call)
			return call, number, last_point



	except KeyError:
		pass
def price(call):
	if call.data == "rub_l" or call.data == "euro1" or call.data == "dollars2":
			bot.send_message(call.message.chat.id, "Введите сумму")
# @bot.callback_query_handler(func=lambda call:True)
# def callback_work(call):
# 	try:
# 		if call.data == "rub":
# 			bot.send_message(call.message.chat.id, text="Выберите")
# 		elif call.data == "euro":
# 			bot.send_message(call.message.chat.id, "Выберите 1")
#
# 	except KeyError:
# 		pass

def start_choose(call):
	keyboard = types.InlineKeyboardMarkup()
	key_start = types.InlineKeyboardButton(text="ДА", callback_data="start")
	keyboard.add(key_start)
	key_help = types.InlineKeyboardButton(text="НЕ ЗНАЮ", callback_data="help")
	keyboard.add(key_help)
	info = "Я бот-конвертер, провожу обмен денежной единицы одной страны на деньги другой по текущему курсу. Доступны: евро, доллары и рубли. Продолжим?"
	bot.send_message(call.message.chat.id, text=info, reply_markup=keyboard)



		# bot.send_message(call.message, "Whatever")
		# keyboard = types.InlineKeyboardMarkup()
		# key_start = types.InlineKeyboardButton(text="START11", callback_data="start1")
		# keyboard.add(key_start)
		# key_help = types.InlineKeyboardButton(text="HELP11", callback_data="help11")
		# keyboard.add(key_help)
		# info = "Second number"
		# bot.send_message(call.message, text=info, reply_markup=keyboard)


	# if call.data == "rub":
	# 	global start_point
	# 	start_point = call.text
	# 	bot.send_message(call.message.chat.id, "Введите rub")
	# 	bot.register_next_step_handler(call.message, rub_start)
	# 	"""НЕ РАБОТАЕТ"""
	# elif call.data == "euro":
	# 	bot.register_next_step_handler(call.message, eu_start)
	# elif call.data == "dollars":
	# 	bot.register_next_step_handler(call.message, dollars_start)


def rub_start(message):
	bot.send_message(message.from_user.id, "Введите rub")

def eu_start(message):
	bot.send_message(message.from_user.id, "Введите euro")

def dollars_start(message):
	bot.send_message(message.from_user.id, "Введите dollars")
# def callback_worker(call):
# 	try:
# 		if call.data == "start":
# 			# bot.send_message(call.message.chat.id, "Выберите валюту с которой нужно перевести")
# 			bot.register_next_step_handler(call.message, start_1)
# 			# return call
# 	except KeyError:
# 		pass
# def start_1(message):
#
# 	keyboard = types.InlineKeyboardMarkup()
# 	rus_start = types.InlineKeyboardButton(text="RUS", callback_data="rus")
# 	keyboard.add(rus_start)
# 	eu_start = types.InlineKeyboardButton(text="EURO", callback_data="euro")
# 	keyboard.add(eu_start)
# 	dollars_start = types.InlineKeyboardButton(text="DOLLARS", callback_data="dollars")
# 	keyboard.add(dollars_start)
# 	bot.send_message(message.from_user.id, text="Выберите валюту с которой нужно перевести.", reply_markup=keyboard)



# def start(message):
# 	pass


# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you oing?")
# @bot.message_handler(commands=["help"])
# def help_welcome(message):
# 	bot.reply_to(message, f"Привет, как дела {message.chat.username}?")



# bot.infinity_polling()
bot.polling(none_stop= True)