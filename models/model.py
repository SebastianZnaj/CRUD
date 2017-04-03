import sqlite3


class ItemList:

    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    @classmethod
    def last_id(cls):
        con = sqlite3.connect("items.db")
        cur = con.cursor()
        cur.execute("SELECT MAX(id) FROM items")
        last_item_id = cur.fetchone()[0]
        con.commit()
        con.close()
        return last_item_id

    @classmethod
    def get_all(cls):
        con = sqlite3.connect("items.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM items")
        items_list = []
        for row in cur:
            item = ItemList(row[0], row[1], row[2], row[3])
            items_list.append(item)
        con.commit()
        cur.close()
        return items_list

    @classmethod
    def get_by_id(cls, id):
        con = sqlite3.connect("items.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM items WHERE id=?", (id,))
        for row in cur:
            return ItemList(row[0], row[1], row[2], row[3])
        con.commit()
        con.close()

    def save(self):
        con = sqlite3.connect("items.db")
        cur = con.cursor()
        cur.execute("INSERT INTO items (id, name, description, price) VALUES (?, ?, ?, ?)", (self.id, self.name, self.description, self.price))
        con.commit()
        con.close()

    def delete(self):
        con = sqlite3.connect("items.db")
        cur = con.cursor()
        cur.execute("DELETE FROM items WHERE id=?", (self.id,))
        con.commit()
        con.close()

    def update(self):
        con = sqlite3.connect("items.db")
        cur = con.cursor()
        cur.execute("UPDATE items SET items (id, name, description, price) VALUES (?, ?, ?, ?)", (self.id, self.name, self.description, self.price))
        con.commit()
        con.close()

