import os
import time
import subprocess
import sys

def installPipreqs():
    try:
        import pipreqs
    except ImportError:
        print("pipreqs is not installed. Installing pipreqs...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pipreqs"], check=True)
        print("pipreqs installed successfully.")
        time.sleep(2)

def generateRequirements():
    try:
        subprocess.run(["pipreqs", ".", "--force"], check=True)
        print("requirements.txt generated successfully.")
        time.sleep(2)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while generating requirements.txt: {e}")
        return False
    return True

def installModules():
    try:
        installPipreqs()
        if generateRequirements():
            subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
            os.system('cls')
            print(f"All requirements installed successfully.")
            time.sleep(3)
        else:
            print("Failed to generate requirements.txt.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing requirements: {e}")

installModules()
