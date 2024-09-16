from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
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
    await message.answer('Привет! Я бот, помогающий твоему здоровью! Нажми "Рассчитать", чтобы узнать свю норму калорий',reply_markup=kb)


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.', reply_markup=kb)


kb = ReplyKeyboardMarkup()
button = KeyboardButton(text="Информация")
button2 = KeyboardButton(text="Рассчитать")
kb.row(button)
kb.row(button2)
kb.resize_keyboard = True

#для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
