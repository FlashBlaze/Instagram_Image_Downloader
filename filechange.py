import os
from datetime import datetime 

date_and_time = str(datetime.now()).replace(":", "_").replace(" ", "_")

new_file = date_and_time + ".jpg"
print(new_file)
old_file = "fileName.jpg"
os.rename(old_file, new_file)

