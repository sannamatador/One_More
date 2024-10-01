import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"User{i}", f"example{i}@gmail.com", f"{10 * i}", "1000"))
#
# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id = ?", (f"{i}",))
#
#
# for i in range(1, 11, 2):
#     cursor.execute("UPDATE Users SET Balance = ? WHERE id = ?", (f"{500}", f"{i}"))
#
# cursor.execute("SELECT username, email, age, balance from Users WHERE age <> '60'")
# users = cursor.fetchall()
# for user in users:
#     print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")


cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(Balance) FROM Users")
all_balances = cursor.fetchone()[0]

cursor.execute("SELECT AVG(Balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(avg_balance)
print(all_balances / total_users)

# cursor.execute("DELETE FROM Users")

connection.commit()
connection.close()
