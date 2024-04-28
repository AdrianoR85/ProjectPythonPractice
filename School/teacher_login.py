import hashlib
from util.user import path
def teacher_login(user_name, password:str):
  new_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
  try:
    with open(f'{path}/teachers.txt', 'r') as teachers:
      for teacher in teachers:
        teacher = teacher.split(',')
        
        if teacher[0] == user_name:
          striped_string = teacher[2][1:]
          if new_password == striped_string:
            return teacher
    return False
  
  except FileNotFoundError:
    print('File not found')