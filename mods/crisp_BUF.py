import time
import os

# utils to be added
print("this aint here yet. btw we are shutting down ur pc now.")
if platform.system() == "Darwin":
  os.system("shutdown -h now")
elif platform.system() == "Linux":
  os.system("shutdown -h now")
elif platform.system() == "Windows":
  os.system("shutdown /s")
