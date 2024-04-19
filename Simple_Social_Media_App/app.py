from sql_code import sql_create_table, sql_create_post
from db import create_table
from user import register_user, login_user
from post import create_post, get_posts_by_id, get_posts_all
from time import sleep
import os

is_path_exists = os.path.exists('social_media.db')

if not is_path_exists:
  create_table(sql_create_table)  
  create_table(sql_create_post)
  
def show_options(*texts):
  for index, text in enumerate(texts):
    print(f'{index+1}. {text}')  
  choice = input("Enter your choice: ")
  return choice  

def home_page():
  os.system('cls')
  user = None
  while not user:
    os.system('cls')
    print("=" * 25)
    print("Simple Social Media App!")
    print("=" * 25)
    opt1 = show_options('Login', 'Create User', 'Exit\n')
    if opt1 == '1':
      os.system('cls')
      print("=========LOGIN==========")
      username = input("Enter your username: ")
      password = input("Enter your password: ")
      user = login_user(username, password)
      
      if not user:
        print("\nInvalid username or password!\n")
    elif opt1 == '2':
      os.system('cls')
      print("=========REGISTER==========")
      username = input("Enter your username: ")
      password = input("Enter your password: ")
      name = input("Enter your name: ")
      created = register_user(username, password, name)  
      if created:
        print("\nUser created successfully!\n")
      else:
        print("\nInvalid username or password!\n")
    elif opt1 == '3':
      break
    else:
      print("Invalid option!")
  return user     
    
def app():
  user = home_page()
  user_id = user[0][0]
  print('\nLogin....')
  sleep(2)
  os.system('cls')
  
  while user:
    print("=" * 50)
    print(f"Hello, {user[0][2]}!")
    print("\nWhich one options below: ")
    print("-" * 50)
    opt2 = show_options('New Post','Show my posts', 'Show All posts', 'Logout')
    print("=" * 50)
    
    if opt2 == '1':
      print(user[0])
      comment = input("Enter your comment: ")
      created = create_post(user_id, comment)
      
      if created:
        print("\nPost created successfully!\n")
      else:
        print("\nInvalid comment!\n")
    elif opt2 == '2':
      posts = get_posts_by_id(user_id)
      os.system('cls')
      for post in posts:
        print(' - '.join(post))
    elif opt2 == '3':
      posts = get_posts_all()
      os.system('cls')
      for post in posts:
        print(' - '.join(post))
    elif opt2 == '4':
      user = None
    else:
      print("Invalid option!")
    
if __name__ == "__main__":
  app()