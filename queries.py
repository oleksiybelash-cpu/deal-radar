import sqlite3

conn = sqlite3.connect("deals.db")
cur = conn.cursor()


def show(title, sql, params=()):
    print(f"\n{title}")
    for row in cur.execute(sql, params):
        print("  ", row)


show("1. Найдешевша книжка:",
     "SELECT title, price FROM products WHERE source = 'books' ORDER BY price LIMIT 1")

show("2. Топ-3 книжки за рейтингом (при однаковому — дешевші):",
     "SELECT title, rating, price FROM products WHERE source = 'books' "
     "ORDER BY rating DESC, price LIMIT 3")

word = "Night"
show(f"3. Пошук за словом «{word}»:",
     "SELECT title, price FROM products WHERE title LIKE ?", (f"%{word}%",))

limit = 12
show(f"4. Книжки дешевші за £{limit}:",
     "SELECT title, price FROM products WHERE source = 'books' AND price < ? ORDER BY price",
     (limit,))

show("5. Топ-3 знижки на ігри (%):",
     "SELECT title, price, old_price, ROUND((1 - price / old_price) * 100) AS discount "
     "FROM products WHERE old_price IS NOT NULL ORDER BY discount DESC LIMIT 3")

conn.close()