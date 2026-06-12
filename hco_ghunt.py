import os
import sys
import subprocess

# Colors
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BOLD = '\033[1m'
RESET = '\033[0m'

def auto_setup():
    """Ye function tool ke liye engine khud download karega."""
    if not os.path.exists("sherlock"):
        print(f"{YELLOW}[*] Downloading Engine... Please wait.{RESET}")
        subprocess.run(["git", "clone", "https://github.com/sherlock-project/sherlock"])
        subprocess.run(["pip", "install", "-r", "sherlock/requirements.txt"])

def banner():
    os.system('clear')
    print(f"{RED}{BOLD}  _    _  _____ ____  ")
    print(" | |  | |/ ____/ __ \ ")
    print(" | |__| | |   | |  | |")
    print(" |  __  | |   | |  | |")
    print(" | |  | | |___| |__| |")
    print(" |_|  |_|\_____\____/ ")
    print(f"{RESET}{RED}HCO-OSINT BY AZHAR{RESET}\n")

def main():
    # Lock Flow
    os.system('clear')
    print(f"{RED}!!! TOOL LOCKED !!!{RESET}")
    print("Redirecting to YouTube to unlock...")
    subprocess.run(["termux-open-url", "https://youtube.com/@hackers_colony_termux?si=18WolRHW-UiVybvf"])
    input(f"\n{BOLD}Press Enter after subscribing...{RESET}")

    auto_setup()

    while True:
        banner()
        print("1. Run Real OSINT Scan")
        print("2. Exit")
        ch = input(f"\n{BOLD}HCO@termux >> {RESET}")
        
        if ch == '1':
            target = input(f"{YELLOW}Enter Username: {RESET}")
            # Correct Path Execution
            subprocess.run(["python3", "sherlock/sherlock/sherlock.py", target])
            input(f"\n{BOLD}Press Enter...{RESET}")
        elif ch == '2':
            sys.exit()

if __name__ == "__main__":
    main()
    
