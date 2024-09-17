from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button = KeyboardButton(text="Информация")
button2 = KeyboardButton(text="Рассчитать")
kb.add(button)
kb.add(button2)
kb.resize_keyboard = True
kb2 = InlineKeyboardMarkup()
button3 = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
kb2.add(button3, button4)
kb2.resize_keyboard = True


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_height(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.height.set()


@dp.message_handler(state=UserState.height)
async def set_weight(message, state):
    await state.update_data(height=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * float(data['weight']) + 6.25 * float(data['height']) - 5 * float(data['age']) - 161
    await message.answer(f'Ваша норма калорий {calories}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(
        'Привет! Я бот, помогающий твоему здоровью! Нажми "Рассчитать", чтобы узнать свю норму калорий',
        reply_markup=kb)


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer('для женщин: 10xвес(кг)+6,25xрост(см)–5xвозраст(г)–161', reply_markup=kb)


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.', reply_markup=kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
