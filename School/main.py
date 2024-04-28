import os
from login import login
from register import register_teacher

while True:
  print(f'******* Welcome to Teacher Panel *******\n\n'
        f'What do you want to do (select a number:)\n'
        f'1) Login\n'
        f'2) Register\n'
        f'3) Exit\n')
  teacher_selection = input('> ')
  
  if teacher_selection == '1':
    print('**********Teacher Login**********')
    teacher_username = input('User Name: ')
    teacher_password = input('Password: ')
    login_result = login(teacher_username, teacher_password)
    
    while login_result != -1:
      os.system('cls')
      print(
        f'Welcome back teacher {teacher_username}!\n\n'
        f'What do you want to do (select a number)\n'
        f'1) Get Student Score\n'
        f'2) Update Student Score\n'
        f'3) Enroll New Student\n'
        f'4) Exit\n'
      )
      teacher_login_input = input('> ')
      if teacher_login_input == '4':
        os.system('cls')
        break
      
      if teacher_login_input == '1':
        ...
      elif teacher_login_input == '2':
        ...
      elif teacher_login_input == '3':
        ...
      else:
        print('Invalid option!\n')
          
  elif teacher_selection == '2':
    print('********** Teacher Registration **********')
    teacher_username = input('Username: ')
    teacher_lastname = input('Last Name: ')
    teacher_password = input('Password: ')
    
    register_teacher(teacher_username, teacher_lastname, teacher_password)
  elif teacher_selection == '3':
    break
  else:
    print('Invalid option!\n')