import sqlite3

class UserDB:
    def __init__(self):
        db_path = "db/user_data.db"
        # Para Flask não reclamar em múltiplas requisições:
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
        self.conn.commit()
    
    def add_user(self, nome, email):
        self.cursor.execute("""
            INSERT INTO usuarios (nome, email) VALUES (?, ?)
        """, (nome, email))
        self.conn.commit()

    def list_users(self):
        self.cursor.execute("SELECT nome, email FROM usuarios")
        users = self.cursor.fetchall()
        return [{"nome": nome, "email": email} for nome, email in users]
