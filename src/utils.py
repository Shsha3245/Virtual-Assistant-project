import sqlite3

class Utility:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        # Tabloyu oluştur (ilk çalıştırmada)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS responses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                response TEXT
            )
        """)
        self.conn.commit()

    def save_response(self, response):
        self.cursor.execute("INSERT INTO responses (response) VALUES (?)", (response,))
        self.conn.commit()
