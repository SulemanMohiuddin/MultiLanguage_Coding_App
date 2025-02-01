import sqlite3

def setup_db():
    conn = sqlite3.connect("leaderboard.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS leaderboard (
            username TEXT,
            score INTEGER
        )
    """)
    conn.commit()
    conn.close()

def update_score(username, score):
    conn = sqlite3.connect("leaderboard.db")
    c = conn.cursor()
    c.execute("INSERT INTO leaderboard (username, score) VALUES (?, ?)", (username, score))
    conn.commit()
    conn.close()

def get_leaderboard():
    conn = sqlite3.connect("leaderboard.db")
    c = conn.cursor()
    c.execute("SELECT * FROM leaderboard ORDER BY score DESC")
    results = c.fetchall()
    conn.close()
    return results
