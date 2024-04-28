import os
import hashlib
path = f'{os.getcwd()}/School'

def check_user(user_name:str):
  try:
    with open(f'{path}/teachers.txt', 'r') as file:
      user_names = [line.split(',')[0].strip() for line in file]
      if user_name in user_names:
        print('User already exist') 
        return True
      return False
  except FileNotFoundError:
    print('File not found')
  except TypeError as err:
    print('Data invalid ', err)

def user_data_validation(user_name:str, last_name:str):
  try:
    if len(user_name) < 3 or len(last_name) < 3:
      print('Username or last_name is too short')
      return False
    
    if user_name.isdigit() or user_name.isdigit():
      print('USERNAME or LAST NAME can not be numbers')
      return False
    
    return True
  
  except TypeError as err:
    print('Data invalid ', err)
    
  except SyntaxError as err:
    print('Data invalid ', err)
    
def hash_password(password:str):
  try:
    if len(password) < 6:
      print('Password is too short')
      return False
  
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return password_hash
  except TypeError as err:
    print('Data invalid ', err)