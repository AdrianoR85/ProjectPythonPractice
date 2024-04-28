import os
from util.user import check_user, hash_password, user_data_validation
from util.user import path

def register_teacher(user_name:str, last_name:str, password:str):
  valid_data = user_data_validation(user_name, last_name)
  valid_password = hash_password(password)
  exist_user = check_user('teachers', user_name)

  if valid_data and valid_password and not exist_user:
    try:
      with open(f'{path}/teachers.txt', 'a') as file:
        file.write(f'{user_name}, {last_name}, {valid_password},\n')
        print(f'\n{user_name}, Your registration is successful, go back and log in!\n')
        return True
    except FileNotFoundError as err:
      print('File not found')

