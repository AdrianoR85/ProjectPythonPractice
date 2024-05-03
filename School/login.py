import hashlib
from util.user import path
def login(user_name, password:str):
  new_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
  try:
    with open(f'{path}/teachers.txt', 'r') as teachers:
      for teacher in teachers:
        teacher = teacher.split(',')
        
        if teacher[0] == user_name:
          striped_string = teacher[2][1:]
          if new_password == striped_string:
            return True
    print('User not found')
    return -1
  
  except FileNotFoundError:
    print('File not found')