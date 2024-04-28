import os
path = os.path.dirname(__file__)
from util.user import check_user, hash_password, user_data_validation
  
def register_teacher(user_name:str, last_name:str, password:str):
  valid_data = user_data_validation(user_name, last_name)
  valid_password = hash_password(password)
  exist_user = check_user(user_name)

  if valid_data and valid_password and not exist_user:
    try:
      with open(f'{path}/teachers.txt', 'a') as file:
        file.write(f'{user_name}, {last_name}, {valid_password}, \n')
        print(f'{user_name}, Your registration is successful, go back and log in!')
        return True
    except FileNotFoundError as err:
      print('File not found')
