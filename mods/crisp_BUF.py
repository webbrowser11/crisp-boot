import time
import platform
import os

print("hello, welcome to the crisp boot utils.")
print("you can:")
print("shutdown")
print("restart")
print("crisp")

if answer == "shutdown":
  if platform.system() == "Darwin":
    os.system("shutdown -h now")
  elif platform.system() == "Linux":
    os.system("shutdown -h now")
  elif platform.system() == "Windows":
    os.system("shutdown /s")
elif answer == "restart":
  if platform.system() == "Darwin":
    os.system("shutodwn -r now")
  elif platform.system() == "Linux":
    os.system("shutdown -r now")
  elif platform.system() == "Windows":
    os.system("shutdown /r")
elif answer == "crisp":
  print("crispy")
  kernel_script = os.path.join(os.getcwd(), 'KERNEL', 'kernel.py')
  if os.path.isfile(kernel_script):
    try:
    # Run the kernel script as a subprocess
    subprocess.run([sys.executable, kernel_script], check=True)
    except subprocess.CalledProcessError as e:
      print(f"Error executing the kernel script: {e}")
    except Exception as e:
      print(f"An unexpected error occurred: {e}")
  else:
    print("crispy kernel not found i think... IDK IM A DUMB MOD!!")
