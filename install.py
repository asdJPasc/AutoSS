import auto

def installModules():
    try:
        auto.subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        auto.os.system('cls')
        print(f"{auto.Fore.GREEN}All requirements installed successfully.{auto.Fore.RESET}")
        auto.time.sleep(3)
    except auto.subprocess.CalledProcessError as e:
        print(f"{auto.Fore.RED}Error occurred while installing requirements: {e}{auto.Fore.RESET}")

installModules()
