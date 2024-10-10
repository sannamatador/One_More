from aiogram.dispatcher.filters import state
import sqlite3
from keyboards import *
from crud_functions import *

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


# Регистрация

@dp.message_handler(text='Регистрация')
async def sign_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    username = message.text
    if not is_included(username):
        await state.update_data(username=username)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя")


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    age = message.text
    await state.update_data(age=age)
    data = await state.get_data()
    username = data['username']
    email = data['email']
    age = data['age']
    add_user(username, email, age)  # функция добавления пользователя в таблицу
    await message.answer("Регистрация успешна!")
    await state.finish()


# Ввод данных
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


# Расчет калорий

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * float(data['weight']) + 6.25 * float(data['height']) - 5 * float(data['age']) - 161
    await message.answer(f'Ваша норма калорий {calories}')
    await state.finish()


# Приветствие
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(
        'Привет! Я бот, помогающий твоему здоровью! Нажми "Рассчитать", чтобы узнать свю норму калорий',
        reply_markup=kb)


# Выбор опции
@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer('для женщин: 10xвес(кг)+6,25xрост(см)–5xвозраст(г)–161', reply_markup=kb)


# Покупка
@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    photo = ('vit1.jpg', 'vit2.jpg', 'vit3.jpg', 'photo_5445324181601382313_y.jpg')
    for i in range(len(list_of_goods)):
        with open(photo[i], 'rb') as img:
            await message.answer_photo(img, f'Название: {list_of_goods[i][0]} | Описание: {list_of_goods[i][1]} | Цена:'
                                            f' {list_of_goods[i][2]}', reply_markup=kb)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb3)


@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!', reply_markup=kb)


# Любое нажатие
@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.', reply_markup=kb)


connection.commit()
connection.close()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
