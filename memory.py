import sqlite3

conn = sqlite3.connect("database/memory.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations(
id INTEGER PRIMARY KEY AUTOINCREMENT,
query TEXT,
response TEXT
)
""")

conn.commit()


def save_memory(query, response):

    cursor.execute(
        """
        INSERT INTO conversations(query,response)
        VALUES (?,?)
        """,
        (query, response)
    )

    conn.commit()


def recall_memory():

    cursor.execute(
        """
        SELECT query
        FROM conversations
        ORDER BY id DESC
        LIMIT 1
        """
    )

    result = cursor.fetchone()

    if result:
        return result[0]

    return "No previous issue found."