import hashlib
from db import insert_into, select
from sql_code import sql_insert_user, sql_query_user

def register_user(username, password, name):
  hashlib_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
  response = insert_into(sql_insert_user, username, hashlib_password, name)
  return response
def login_user(username, password):
  hashlib_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
  user = select(sql_query_user, username, hashlib_password)
  return user
  
if __name__ == '__main__':
  # register_user('Lara100', '321654', 'Lara')
  user = login_user('AdrianoR85', '123456')
  print(user) 