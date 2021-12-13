import telebot

start_message = '''
Hello, this is cryptocurrency bot)
It can help you find and check your favorite coins

In order to add some coin:
Type "add" and the coin
If you want to check Bitcoin, you have to type "btc"
Also you can remover the coin:
Type "remove" and coin
To start the cycle of tracing just type "Go"
And to stop it type "Stop". Good luck
You can choose the time you wanna get the price
It will send you the price of the coins in some time
By default it equals to 1 time per minute
You can choose how per how many minutes you wanna get the prices
Just type "change time to " number
If you wanna get the average prices in some time
Type "regular checks [minutes]" they are off by default
And will send you the prices every hour
and if you don't want to get the average price
put time as 0'''

coin_keyboard_list = ['BTC', 'ETH', 'BNB', 'KAVA', 'EOS', 'ALGO']

CoinKeyboard = telebot.types.InlineKeyboardMarkup()
CoinKeyboard.row(
    telebot.types.InlineKeyboardButton("BTC", callback_data='BTC'),
    telebot.types.InlineKeyboardButton("ETH", callback_data='ETH'),
    telebot.types.InlineKeyboardButton("BNB", callback_data='BNB')
)
CoinKeyboard.row(
    telebot.types.InlineKeyboardButton("Kava", callback_data="KAVA"),
    telebot.types.InlineKeyboardButton("EOS", callback_data="EOS"),
    telebot.types.InlineKeyboardButton("ALGO", callback_data="ALGO")
)

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(
    telebot.types.InlineKeyboardButton('Show coins', callback_data="Show coins")
)

regular_checks_keyboard = telebot.types.InlineKeyboardMarkup()
regular_checks_keyboard.row(
    telebot.types.InlineKeyboardButton("1 hour", callback_data="regular60")
)
regular_checks_keyboard.row(
    telebot.types.InlineKeyboardButton("2 hours", callback_data="regular120")
)
regular_checks_keyboard.row(
    telebot.types.InlineKeyboardButton("4 hours", callback_data="regular240")
)
regular_checks_keyboard.row(
    telebot.types.InlineKeyboardButton("12 hours", callback_data="regular720")
)

keyboard_list = [keyboard, CoinKeyboard, regular_checks_keyboard]
