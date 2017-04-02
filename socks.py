from database import Database


class Product:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    @classmethod
    def find_by_id(cls, id):
        query = "SELECT * FROM socks WHERE id=?"
        data = Database.connect_db(query, id)
        product = cls(data[0][0], data[0][1], data[0][2], data[0][3])
        return product

    @classmethod
    def list_products(cls):
        query = "SELECT * FROM socks"
        data = Database.connect_db(query)
        product_list = []
        if data:
            for row in data:
                product_list.append(cls(row[0], row[1], row[2], row[3]))
        return product_list
