# -*- coding: utf-8 -*-
#twitter.com/pijawca
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start_btn = KeyboardButton('🚀 Главная')
weather_btn = KeyboardButton('📰 Новости')
bots_btn = KeyboardButton('🤖 Боты')
donate_btn = KeyboardButton('💎 Купить подписку')
showmehidebot_pass = InlineKeyboardButton(text='@showmehidebot')
back_btn = KeyboardButton('🔙 Назад')
markup = ReplyKeyboardMarkup(resize_keyboard=False).row(start_btn, weather_btn).row(bots_btn, donate_btn).add(KeyboardButton('💕 Написать в ЛС',))
markup_bots = ReplyKeyboardMarkup(resize_keyboard=True).row(showmehidebot_pass).add(back_btn)

showmehidebot_btn = InlineKeyboardButton('@showmehidebot', url='https://oplata.qiwi.com/form?invoiceUid=5319fdd2-5a8a-47dc-b149-52bc64c13d0d')
inline_kb2 = InlineKeyboardMarkup().add(showmehidebot_btn)
contact_btn = InlineKeyboardButton('💕 Написать в ЛС', url='http://t.me/pijawca')
inline_kb1 = InlineKeyboardMarkup().add(contact_btn)
