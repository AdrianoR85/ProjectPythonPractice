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
def app():
  print("=" * 50)
  print("Welcome to Simple Social Media App!")
  print("Which one options below: ")
  print("-" * 50)
  opt1 = show_options('Login', 'Create User', 'Exit')
  user = None
  
  while True:
    if opt1 == '1':
      while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user = login_user(username, password)
        
        if user:
          os.system('cls')
          print("Login successful")
          sleep(2)
          os.system('cls')
          print("Which one options below: ")
          opt2 = show_options("Show my posts", "Show All posts", "Create New Post" ,"Logout")
          
          if opt2 == '1':
            posts = get_posts_by_id(user[0])
            for post in posts:
              print(" - ".join(post))
          elif opt2 == '2':
            posts = get_posts_all()
            for post in posts:
              print(" - ".join(post))
            print("-" * 50)
          elif opt2 == '3':
            ...
          elif opt2 == '4':
            print("You have logged out successfully!")
            break
          else:
            print("Invalid option!")
    elif opt1 == '2':
      username = input("Enter your username: ")
      password = input("Enter your password: ")
      name = input("Enter your name: ")
      created = register_user(username, password, name)  
      if created:
        print("You have logged in successfully!")
      else:
        print("\nInvalid username or password!\n")
    elif opt1 == '3':
      print("You have logged out successfully!")
      break
    else:
      print("Invalid option!")    
    
if __name__ == "__main__":
  app()