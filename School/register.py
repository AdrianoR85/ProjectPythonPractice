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

def register_student(student_name: str, student_score:float, teacher_name: str):
  exist_user = check_user('students', student_name)
  exist_teacher = check_user('teachers', teacher_name)
  
  if not exist_user and exist_teacher:
    try:
      with open(f'{path}/students.txt', 'a') as file:
        file.write(f'{student_name}, {student_score}, Added by Teacher {teacher_name}\n')
        print(f'Student with the {student_score} successfully added in the system\n')
        return True
    except FileNotFoundError as err:
      print('File not found')
