import sqlite3


class ItemList:

    def __init__(self, name, description, price):
        self.id = None
        self.name = name
        self.description = description
        self.price = price

    @classmethod
    def get_all(cls):
        con = sqlite3.connect("items.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM items")
        items_list = []
        for row in cur:
            item = ItemList(row[1], row[2], row[3])
            items_list.append(item)
        con.commit()
        cur.close()
        return items_list

    @classmethod
    def get_by_id(cls):
        pass

    def add(self):
        pass

    def remove(self):
        pass

    def edit(self):
        pass

