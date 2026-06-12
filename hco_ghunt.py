import os
import time
import subprocess
import sys

# Colors
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BOLD = '\033[1m'
RESET = '\033[0m'

def setup_env():
    # Sherlock ko auto-install karne ka logic
    if not os.path.exists("sherlock"):
        print(f"{YELLOW}[*] Setting up Real OSINT Engine...{RESET}")
        os.system("git clone https://github.com/sherlock-project/sherlock > /dev/null 2>&1")
        os.system("cd sherlock && pip install -r requirements.txt > /dev/null 2>&1")

def banner():
    os.system('clear')
    print(f"{RED}{BOLD}  _    _  _____ ____  ")
    print(" | |  | |/ ____/ __ \ ")
    print(" | |__| | |   | |  | |")
    print(" |  __  | |   | |  | |")
    print(" | |  | | |___| |__| |")
    print(" |_|  |_|\_____\____/ ")
    print(f"{RESET}{RED}HCO-REAL OSINT SCANNER{RESET}\n")

def run_scan():
    username = input(f"\n{YELLOW}Enter Username/Email to Scan: {RESET}")
    print(f"\n{GREEN}[+] Starting Real-Time Global Scan for: {username}{RESET}")
    print(f"{GREEN}[+] Searching 500+ Websites... Please Wait.{RESET}\n")
    
    # Real Sherlock execution
    # Ye tool sach mein internet request bhejta hai, fake nahi hai.
    sherlock_path = os.path.join("sherlock", "sherlock")
    os.system(f"python3 {sherlock_path} {username}")
    
    input(f"\n{BOLD}Press Enter to return to menu...{RESET}")

def main():
    # Lock Flow (Jaise tumne kaha tha)
    os.system('clear')
    print(f"{RED}{BOLD}!!! TOOL LOCKED !!!{RESET}")
    print("Redirecting to YouTube to unlock...")
    time.sleep(2)
    os.system("termux-open-url https://youtube.com/@hackers_colony_termux?si=18WolRHW-UiVybvf")
    input(f"\n{BOLD}Press Enter after subscribing...{RESET}")
    
    setup_env()
    
    while True:
        banner()
        print("1. Run Real OSINT Scan")
        print("2. Exit")
        choice = input(f"\n{BOLD}HCO@termux >> {RESET}")
        
        if choice == '1':
            run_scan()
        elif choice == '2':
            sys.exit()

if __name__ == "__main__":
    main()
    
