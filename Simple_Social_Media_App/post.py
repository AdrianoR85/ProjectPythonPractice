from db import insert_into, select
from sql_code import sql_insert_post, sql_query_post_all, sql_query_post_id
def create_post(user_id, comment):
  commit = insert_into(sql_insert_post, user_id, comment)
  return commit
def get_posts_all():
  posts = select(sql_query_post_all)
  return posts

def get_posts_by_id(user_id):
  posts = select(sql_query_post_id, user_id)
  return posts


