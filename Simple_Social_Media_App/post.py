from db import insert_post_data, get_posts

def create_post(user_id, comment):
  insert_post_data(user_id, comment)
  
def get_post():
  return get_posts()
