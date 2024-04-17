import hashlib
from db import insert_user_data, get_user

def register_user(username, password, name):
  hashlib_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
  insert_user_data(username, hashlib_password, name)
  
def login_user(username, password):
  hashlib_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
  user = get_user(username, hashlib_password)
  return user
  