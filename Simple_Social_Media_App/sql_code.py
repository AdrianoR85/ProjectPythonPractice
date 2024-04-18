sql_create_table = """
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        name TEXT NOT NULL
      )
"""
sql_create_post = """
      CREATE TABLE IF NOT EXISTS posts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        comment TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
  )
"""
sql_insert_user = "INSERT INTO users (username, password, name) VALUES (?,?,?)"
sql_insert_post = "INSERT INTO posts (user_id, comment) VALUES (?,?)"
sql_query_user = "SELECT id, username, name FROM users WHERE username = ? AND password = ? "
sql_query_post_all = """
      SELECT  
        users.name,
        posts.comment,
        posts.timestamp
      FROM posts
      JOIN users ON posts.user_id = users.id
      ORDER BY posts.timestamp DESC
      """

sql_query_post_id = """
      SELECT  
        users.name,
        posts.comment,
        posts.timestamp
      FROM posts
      JOIN users ON posts.user_id = users.id
      WHERE users.id = ?
      ORDER BY posts.timestamp DESC
      """