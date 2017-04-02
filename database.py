import sqlite3


class Database:
    @staticmethod
    def make_db():
        conn = sqlite3.connect("socks_manager.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE if not exists socks
                      (id integer primary key autoincrement,
                      name text not null,
                      description text,
                      price real not null);''')
        conn.commit()
        conn.close()

    @staticmethod
    def connect_db(query, *args):
        conn = sqlite3.connect("socks_manager.db")
        c = conn.cursor()
        c.execute(query, args)
        data = c.fetchall()
        conn.commit()
        conn.close()
        return data