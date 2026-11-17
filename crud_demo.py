import sqlite3

disk = sqlite3.connect("deals.db")
conn = sqlite3.connect(":memory:")
disk.backup(conn)          # копія бази: справжній deals.db не зміниться
disk.close()
cur = conn.cursor()


def count():
    return cur.execute("SELECT COUNT(*) FROM products").fetchone()[0]


print("Товарів до змін:", count())

cur.execute("UPDATE products SET price = ROUND(price * 0.9, 2) WHERE source = 'books' AND rating = 5")
print("Знижка 10% на книжки з рейтингом 5: змінено рядків:", cur.rowcount)

cur.execute("DELETE FROM products WHERE price > 50")
print("Видалено дорожчих за 50: рядків", cur.rowcount)

print("Товарів після змін:", count())
conn.close()