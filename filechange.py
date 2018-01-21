import os
from datetime import datetime 

date_and_time = str(datetime.now()).replace(":", "_").replace(" ", "_")

new_file = date_and_time + ".jpg"
old_file = "fileName.jpg"

try:
  os.rename(old_file, new_file)
  print("New file is: " + new_file)
except FileNotFoundError:
  print("File name is already changed")

