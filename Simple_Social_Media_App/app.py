from db import connection, create_user_table, create_post_table
from user import register_user, login_user
from post import create_post, get_post
import os

is_path_exists = os.path.exists('social_media.db')

if not is_path_exists:
    conn = connection()
    create_user_table(conn)  
    create_post_table(conn)
    conn.close()
  
  