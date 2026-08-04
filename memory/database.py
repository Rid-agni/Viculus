import sqlite3

class MemoryDatabase:
    def __init__(self):
        self.connection = sqlite3.connect(
            "memory.db"
        )
        self.cursor = self.connection.cursor()
        self.create_tables()
    def create_tables(self):
     self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS memories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner TEXT,
        other_agent TEXT,
        interaction_type TEXT,
        description TEXT,
        importance REAL,
        source TEXT,
confidence REAL,
        timestamp INTEGER
    )
    """)
     self.connection.commit()
    def add_memory(self,owner, other,interaction_type,description,importance,source, confidence,timestamp):
     self.cursor.execute(
        """
        INSERT INTO memories(
            owner,
            other_agent,
            interaction_type,
            description,
            importance,
            source,
            confidence,
            timestamp
        )
        VALUES(?,?,?,?,?,?,?,?)
        """,
        (
            owner,
            other,
            interaction_type,
            description,
            importance,
            source,
            confidence,
            timestamp
        )

    )

     self.connection.commit()
    def get_memories(self,owner):
     self.cursor.execute(
        """
        SELECT *
        FROM memories
        WHERE owner=?
        ORDER BY timestamp DESC
        """,
        (owner,)
    )
     return self.cursor.fetchall()
    def get_memories_between(
    self,
    owner,
    other,
    limit=5
):
     self.cursor.execute(
        """
        SELECT interaction_type
        FROM memories
        WHERE owner=?
        AND other_agent=?
        ORDER BY timestamp DESC
        LIMIT ?
        """,
        (
            owner,
            other,
            limit
        )
    )
     return self.cursor.fetchall()
    def get_recent_memories(self, owner, limit=5):
     self.cursor.execute(
        """
        SELECT interaction_type,
               description,
               importance,
               source,
               confidence
        FROM memories
        WHERE owner=?
        ORDER BY timestamp DESC
        LIMIT ?
        """,
        (owner, limit)
    )
     return self.cursor.fetchall()