# Task 1

import os
 
def list_directory_contents():
  user_path = input("Please enter the directory path: ")
  try:
      if os.path.exists(user_path):
        print(f"\n{user_path} exists")
        files = os.listdir(user_path)
        print(f"\nThe files in the {user_path} directory are: \n{files}\n")
      else:
        print(f"\n{user_path} directory not found.\n")
       
  except FileNotFoundError:
    print("Could not find {user_path}.")
   
  except PermissionError:
    print("You do not have permission to access {user_path")
   
  except Exception as e:
    print(f"A general error has occurred: {e}")
  
list_directory_contents()