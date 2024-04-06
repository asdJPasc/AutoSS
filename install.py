import subprocess

def installModules():
    try:
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        print("All requirements installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing requirements: {e}")

installModules()