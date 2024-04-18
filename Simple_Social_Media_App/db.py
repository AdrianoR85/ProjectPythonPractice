import sqlite3
    
def create_table(sql_code):
  try:
    conn = sqlite3.connect("social_media.db")
    cursor = conn.cursor()
    
    cursor.execute(sql_code)
    
    conn.commit()
    conn.close()
  except sqlite3.Error as e:
    print(f"An error occurred: {e}")
  except TypeError as e:
    print(f"An error occurred: {e}")
  except UnboundLocalError as e:
    print(f"An error occurred: {e}")
  except Exception as e:
    print(f"An error occurred: {e}")
  except ImportError as e:
    print(f"An error occurred: {e}")

def insert_into(sql_code, *data):
  try:
    conn = sqlite3.connect("social_media.db")
    cursor = conn.cursor()
    
    cursor.execute(sql_code, data)
    
    conn.commit()
    conn.close()
  except sqlite3.Error as e:
    print(f"An error occurred: {e}")
  except TypeError as e:
    print(f"An error occurred: {e}")
  except UnboundLocalError as e:
    print(f"An error occurred: {e}")
  except Exception as e:
    print(f"An error occurred: {e}")
  return True

def select(sql_code, *data):
  try:
    conn = sqlite3.connect("social_media.db")
    cursor = conn.cursor()
    
    cursor.execute(sql_code, data)
    
    data = cursor.fetchall()
    conn.close()
    return data
  except sqlite3.Error as e:
    print(f"An error occurred: {e}")
  except TypeError as e:
    print(f"An error occurred: {e}")
  except UnboundLocalError as e:
    print(f"An error occurred: {e}")
  except Exception as e:
    print(f"An error occurred: {e}")
  return