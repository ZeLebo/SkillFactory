import telebot
import time
from Cryptos import CryptoClassUpdated as CryptoClass
import keyboards

from decouple import config
bot = telebot.TeleBot(config("code"))

coins = []
coins_number = []
in_work = False
start_message = keyboards.start_message
time_period = 60
regular_checks = False
regular_checks_time = 60


def regular_price_tracking(message):
    answer = 'The regular checks:\n'
    for i in coins:
        answer += i.name + " is " + str(i.price) + "$\n"
    if coins:
        bot.send_message(message.from_user.id, answer)
    if not coins:
        bot.send_message(message.from_user.id,
                         "You don't have any coins to track\nYou can add them using 'add [coin name]'")


def regular_checks_switch(message):
    global regular_checks, regular_checks_time
    try:
        if int(message.text[15:]) == 0:
            regular_checks = False
            bot.send_message(message.from_user.id, "The regular checks are off")
        else:
            regular_checks = True
            regular_checks_time = int(message.text[15:])
            bot.send_message(message.from_user.id, "Now you will get the price every " + message.text[15:] + " minutes")
    except ValueError:
        bot.send_message(message.from_user.id, "Seems like you have put the wrong time...")

    else:
        while regular_checks:
            time.sleep(60 * regular_checks_time)
            if regular_checks:
                regular_price_tracking(message)


def time_period_change(message):
    global time_period
    try:
        print(message.text[15:])
        if int(message.text[15:]) and int(message.text[15:]) >= 1:
            time_period = int(message.text[15:])
            bot.send_message(message.from_user.id,
                             "Time period changed\nNow the price will be checked every "
                             + str(time_period) + " minutes")

        else:
            bot.send_message(message.from_user.id, "Wrong time period")
    except ValueError:
        bot.send_message(message.from_user.id, "Not a number")


def price_tracking(message):
    try:
        for i in coins:
            i.update_price()
            print('checking the price of ' + i.name)

            if i.price > i.last_price * 1.05:
                percent = (100 * i.price / i.last_price) - 100
                i.last_price = i.price
                answer = i.name + " is " + str(i.price) + "$\nIt's " + str(percent) + "% higher that the previous peak"
                bot.send_message(message.from_user.id, answer)

            elif i.price < i.last_price * 0.95:
                percent = 100 - (100 * i.price / i.last_price)
                i.last_price = i.price
                answer = i.name + " is " + str(i.price) + "$\nIt's " + str(percent) + "% lower that the previous peak"
                bot.send_message(message.from_user.id, answer)

    except IndexError:
        bot.send_message(message.from_user.id, "something is wrong")
    except ZeroDivisionError:
        print('The is not here yet')


def show_coins(message):
    coins_list = ""
    for i in coins:
        coins_list += i.name + ' is ' + str(i.price) + '$\n'
    if coins_list:
        bot.send_message(message.from_user.id, coins_list)
    else:
        bot.send_message(message.from_user.id, "You don't have any coins", reply_markup=keyboards.CoinKeyboard)


def add_coin(message):
    try:
        if message.text[4:].upper() in coins_number:
            bot.send_message(message.from_user.id, "You have this coin =)")
            return

        else:
            coins.append(CryptoClass(message.text[4:].upper()))
            coins_number.append(coins[-1].name)
    except IndexError:
        bot.send_message(message.from_user.id, "Can't find such coin =(")
    else:
        bot.send_message(message.from_user.id, coins[-1].name + " was successfully added")

        text_message = coins[-1].name + " is " + str(coins[-1].price) + "$"
        bot.send_message(message.from_user.id, text_message)


def remove_coin(message):
    try:
        coins.pop(coins_number.index(message.text[7:].upper()))
        coins_number.pop(coins_number.index(message.text[7:].upper()))

        bot.send_message(message.from_user.id, message.text[7:] + " was removed")

    except IndexError:
        print("Can't find this index")
    except ValueError:
        print("Object is not in the list")
        bot.send_message(message.from_user.id, "No such coin")


@bot.message_handler(content_types=['text'])
def get_message(message):
    global in_work
    if message.text.lower() == "start":
        bot.send_message(message.from_user.id, start_message)

    elif message.text.lower().startswith("add"):
        add_coin(message)

    elif message.text.lower().startswith("remove"):
        remove_coin(message)

    elif message.text.lower().startswith("stop"):
        in_work = False
        bot.send_message(message.from_user.id, "The tracking was stopped")

    elif message.text.lower().startswith("go"):
        in_work = True
        while in_work:
            price_tracking(message)
            time.sleep(60)

    elif message.text.lower() == "show coins":
        show_coins(message)

    elif message.text.lower().startswith("change time to"):
        time_period_change(message)

    elif message.text.lower() == "regular checks keyboard":
        bot.send_message(message.from_user.id, "Here are some samples for regular checks",
                         reply_markup=keyboards.regular_checks_keyboard)

    elif message.text.lower().startswith("regular checks"):
        regular_checks_switch(message)

    elif message.text.lower() == "coin keyboard":
        bot.send_message(message.from_user.id, "Here's the coin keyboard", reply_markup=keyboards.CoinKeyboard)

    elif message.text.lower() == "show keyboards":
        for i in keyboards.keyboard_list:
            bot.send_message(message.from_user.id, "Here's keyboards", reply_markup=i)

    else:
        bot.send_message(message.from_user.id, "Seems like the coin was typed wrong", reply_markup=keyboards.keyboard)


def add_coin_query(query):
    if query.data in coins_number:
        bot.send_message(query.message.chat.id, "You have this coin")
    else:
        coins.append(CryptoClass(query.data))
        coins_number.append(query.data)
        bot.send_message(query.message.chat.id, query.data + " was successfully added")
        bot.send_message(query.message.chat.id, query.data + " is " + str(coins[-1].price) + "$")


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    if query.data == "Show coins":
        coins_list = ""
        for i in coins:
            coins_list += i.name + ' is ' + str(i.price) + '$\n'
        if coins_list:
            bot.send_message(query.message.chat.id, coins_list)
        else:
            bot.send_message(query.message.chat.id, "You don't have any coins", reply_markup=keyboards.CoinKeyboard)
    elif query.data in keyboards.coin_keyboard_list:
        add_coin_query(query)
    elif query.data.startswith("regular"):
        global regular_checks, regular_checks_time
        regular_checks = True
        regular_checks_time = int(query.data[7:])
        bot.send_message(query.message.chat.id,
                         "You will get the prices every " + str(int(query.data[7:]) / 60) + " hour")


bot.polling(none_stop=False, interval=0)
