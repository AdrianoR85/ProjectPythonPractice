import os
import hashlib
path = f'{os.getcwd()}/School/data'

def check_user(data_name, user_name:str):
  try:
    with open(f'{path}/{data_name}.txt', 'r') as file:
      user_names = [line.split(',')[0].strip() for line in file]
      if user_name in user_names:
        print('\nUser already exist\n') 
        return True
      return False
  except FileNotFoundError:
    print('\nFile not found\n')
  except TypeError as err:
    print('\nData invalid ', err)

def user_data_validation(user_name:str, last_name:str):
  try:
    if len(user_name) < 3 or len(last_name) < 3:
      print('\nUsername or last_name is too short\n')
      return False
    
    if user_name.isdigit() or user_name.isdigit():
      print('\nUSERNAME or LAST NAME can not be numbers\n')
      return False
    
    return True
  
  except TypeError as err:
    print('Data invalid ', err)
    
  except SyntaxError as err:
    print('Data invalid ', err)
    
def hash_password(password:str):
  try:
    if len(password) < 6:
      print('\nPassword is too short\n')
      return False
  
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return password_hash
  
  except TypeError as err:
    print('Data invalid ', err)

def get_student_score():
  try:
    with open(f'{path}/students.txt', 'r') as students:
      return students.read()
  except FileNotFoundError:
    print('\nFile not found\n')
  except TypeError as err:
    print('\nData invalid ', err)