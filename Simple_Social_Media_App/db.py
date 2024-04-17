import sqlite3

def connection():
  return sqlite3.connect("social_media.db")

def create_user_table(connection):
  conn = connection
  cursor = conn.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT NOT NULL,
      password TEXT NOT NULL,
      name TEXT NOT NULL
    )
""")
  conn.commit()
  
def create_post_table(connection):
  conn = connection
  cursor = conn.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER NOT NULL,
      comment TEXT,
      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")
  conn.commit()

def insert_user_data(username, password, name):
  conn = connection()
  cursor = conn.cursor()
  cursor.execute("INSERT INTO users (username, password, name) VALUES (?,?,?)", (username, password, name))
  conn.commit()
  conn.close()

def insert_post_data(user_id, content):
  conn = connection()
  cursor = conn.cursor()
  cursor.execute("""
    INSERT INTO posts (user_id, comment)
    VALUES (?,?)                 
""", (user_id, content))
  conn.close()
  conn.commit()

def get_user(username, password):
  conn = connection()
  cursor = conn.cursor()
  cursor.execute("""
      SELECT id, username, name FROM users 
      WHERE username = ? AND password = ?                
  """, (username, password))
  user = cursor.fetchall()
  conn.close()
  return user

def get_posts():
  conn = connection()
  cursor = conn.cursor()
  
  cursor.execute("""
      SELECT  
        users.name,
        posts.comment,
        posts.timestamp
      FROM posts
      JOIN users ON posts.user_id = users.id
      ORDER BY posts.timestamp DESC
  """)
  posts = cursor.fetchall()
  conn.close()
  return posts

if __name__ == "__main__":
  create_user_table()
  create_post_table()
