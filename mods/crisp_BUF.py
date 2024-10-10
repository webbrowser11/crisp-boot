import time
import os

print("hello, wlelcome to the crisp boot utils.")
if platform.system() == "Darwin":
  os.system("shutdown -h now")
elif platform.system() == "Linux":
  os.system("shutdown -h now")
elif platform.system() == "Windows":
  os.system("shutdown /s")
