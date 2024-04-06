import os
import time
import subprocess

def installModules():
    try:
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        os.system('cls')
        print(f"All requirements installed successfully.")
        time.sleep(3)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing requirements: {e}")

installModules()
