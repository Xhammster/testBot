from gc import callbacks

import telebot
from pyexpat.errors import messages
from telebot import  types
from telebot.apihelper import ApiTelegramException

bot = telebot.TeleBot("5845684557:AAGZiSc2-hQXCclTvSxPvu5fkSPNHFhDjIc")

@bot.message_handler(func= lambda message: True )
def menu(message):
    kb = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='Экипировка' , callback_data="ekip1")
    btn2 = types.InlineKeyboardButton(text='Спортпит', callback_data="Sportik")
    kb.add(btn1,btn2)
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name} ,выбери нужный раздел",reply_markup=kb)
    try:
        bot.delete_message(message.chat.id, message.id)
    except ApiTelegramException:
        pass

@bot.message_handler(func= lambda message: True )
def menu2(message):
    kb = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='Экипировка' , callback_data="ekip1")
    btn2 = types.InlineKeyboardButton(text='Спортпит', callback_data="Sportik")
    kb.add(btn1,btn2)
    bot.send_message(message.chat.id, f"Выбери нужный раздел",reply_markup=kb)
    try:
        bot.delete_message(message.chat.id, message.id)
    except ApiTelegramException:
        pass

@bot.callback_query_handler(func=lambda call: call.data == "ekip1")
def ekip(call):
       murk = types.InlineKeyboardMarkup(row_width=2)
       but1=types.InlineKeyboardButton(text='Поясной ремень', url= "https://lyl.su/7qLw")
       but2 = types.InlineKeyboardButton(text='Лямки', url= "https://lyl.su/e0zs")
       bot.delete_message(call.message.chat.id, call.message.message_id)
       bun3 = types.InlineKeyboardButton(text='Назад',callback_data= "back" )
       murk.add(but1, but2,bun3)
       bot.send_message(call.message.chat.id, f"Поясной ремень-помогает сдерживать брюшное давление \n Лямки-сохроняют предплечия снижают нагрузку на кисти " , reply_markup=murk)




@bot.callback_query_handler(func=lambda call: call.data == "Sportik")
def pit(call):
        murk1 = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text='Казеин', url='https://health-store.ru/catalog/kazein/')
        btn2 = types.InlineKeyboardButton(text='протеин', url='https://clck.ru/3F2fHd')
        bot.delete_message(call.message.chat.id, call.message.message_id)
        btn3 = types.InlineKeyboardButton(text='Назад',callback_data="back")
        murk1.add(btn1,btn2,btn3)
        bot.send_message(call.message.chat.id, f"Протеиновый белок-поможет в массанаборе,в наборе суточной нормы белка. \n Казеиновый белок-поможет качественному восстановлению провоцирует снижение жира под кожей.", reply_markup=murk1)

@bot.callback_query_handler(func=lambda call: call.data == "back" )
def naz(call):
    menu2(call.message)











bot.polling(non_stop=True)
