# Приложение для туристического агентства ТУР.
# Таблица Турист должна содержать следующую информацию о клиентах турфирмы:
# Код клиента, Клиент (Фамилия), Телефон, Название страны, Регион, Продолжительность поездки, Стоимость путевки.

import sqlite3 as sq
from dates import info_users

with sq.connect("Tur.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS tourist")
    cur.execute("""CREATE TABLE IF NOT EXISTS tourist (
        klient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        famil TEXT NOT NULL,
        number INTEGER NOT NULL DEFAULT 1,
        country TEXT NOT NULL,
        Region TEXT,
        Prod_poezd DATETIME DEFAULT 0,
        Stoim_put INTEGER DEFAULT 0)""")

with sq.connect("Tur.db") as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO tourist VALUES (?, ?, ?, ?, ? ,? ,?)",info_users)

with sq.connect("Tur.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM tourist WHERE Stoim_put > 100000")
    res = cur.fetchall()
    print(res)

with sq.connect("Tur.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM tourist WHERE Prod_poezd > 10")
    res = cur.fetchall()
    print(res)

with sq.connect("Tur.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM tourist WHERE Stoim_put < 150000 AND Prod_poezd > 5")
    res = cur.fetchall()
    print(res)


with sq.connect("Tur.db") as con:
    cur = con.cursor()
    cur.execute("UPDATE tourist SET Stoim_put = Stoim_put+3000 WHERE Region LIKE 'А%'")
    cur.execute("SELECT * FROM tourist")
    resul = cur.fetchall()
    print(resul)



with sq.connect("Tur.db") as con:
    cur = con.cursor()
    cur.execute("UPDATE tourist SET Prod_poezd = Prod_poezd+2 WHERE country LIKE 'Т%'")
    cur.execute("SELECT * FROM tourist")
    resul = cur.fetchall()
    print(resul)

with sq.connect("Tur.db") as con:
    cur = con.cursor()
    cur.execute("DELETE FROM tourist WHERE klient_id = 2")
    cur.execute("SELECT * FROM tourist")
    resul = cur.fetchall()
    print(resul)

with sq.connect("Tur.db") as con:
    cur = con.cursor()
    cur.execute("DELETE FROM tourist WHERE  famil LIKE 'К%'")
    cur.execute("SELECT * FROM tourist")
    resul = cur.fetchall()
    print(resul)

with sq.connect("Tur.db") as con:
    cur = con.cursor()
    cur.execute("DELETE FROM tourist WHERE Stoim_put < 100000")
    cur.execute("SELECT * FROM tourist")
    resul = cur.fetchall()
    print(resul)