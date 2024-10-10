import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL 
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')


def is_included(username):
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    return cursor.fetchone() is not None


def add_user(username, email, age):
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",(f"{username}", f"{email}", f"{age}",  1000))
    connection.commit()


def get_all_products():
    cursor.execute("SELECT title, description, price FROM Products")
    products = cursor.fetchall()
    return products


# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products (title, description, price)  VALUES (?,?,?)",(f"Product {i}", f"Description {i}", f"{i * 100}"))

initiate_db()

list_of_goods = get_all_products()


# cursor.execute("DELETE FROM Products")

connection.commit()
connection.close()
