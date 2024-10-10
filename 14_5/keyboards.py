from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup()
button = KeyboardButton(text="Информация")
button2 = KeyboardButton(text="Рассчитать")
button5 = KeyboardButton(text="Купить")
button10 = KeyboardButton(text="Регистрация")
kb.add(button, button2)
kb.add(button5, button10)
kb.resize_keyboard = True
kb2 = InlineKeyboardMarkup()
button3 = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
kb2.add(button3, button4)
kb2.resize_keyboard = True
kb3 = InlineKeyboardMarkup()
button6 = InlineKeyboardButton("Продукт 1", callback_data='product_buying')
button7 = InlineKeyboardButton("Продукт 2", callback_data='product_buying')
button8 = InlineKeyboardButton("Продукт 3", callback_data='product_buying')
button9 = InlineKeyboardButton("Продукт 4 - самый лучший", callback_data='product_buying')
kb3.add(button6, button7, button8, button9)
kb3.resize_keyboard = True

