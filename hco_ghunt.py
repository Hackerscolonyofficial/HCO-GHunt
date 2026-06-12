import os
import time
import sys
import subprocess

# Colors
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BOLD = '\033[1m'
RESET = '\033[0m'

def setup_engine():
    """Auto-installs engine dependencies."""
    if not os.path.exists("ghunt"):
        print(f"{YELLOW}[*] Setting up HCO-GHUNT Engine... Please wait.{RESET}")
        os.system("git clone https://github.com/mxrch/ghunt > /dev/null 2>&1")
        os.system("pip install -r ghunt/requirements.txt > /dev/null 2>&1")

def banner():
    os.system('clear')
    # ASCII Art
    print(f"{RED}{BOLD}  _    _  _____ ____  ")
    print(" | |  | |/ ____/ __ \ ")
    print(" | |__| | |   | |  | |")
    print(" |  __  | |   | |  | |")
    print(" | |  | | |___| |__| |")
    print(" |_|  |_|\_____\____/ ")
    print(f"{RESET}{RED}HCO-GHUNT BY AZHAR | HCO TEAM{RESET}\n")

def lock_screen():
    os.system('clear')
    print(f"{RED}{BOLD}!!! THIS TOOL IS LOCKED !!!{RESET}")
    print(f"{YELLOW}To use this tool, Subscribe to our YouTube channel & click the Bell Icon to unlock.{RESET}")
    print("\nRedirecting to YouTube in...", end="", flush=True)
    for i in range(5, 0, -1):
        print(f" {i}", end="", flush=True)
        time.sleep(1)
    
    # YouTube Redirect
    subprocess.run(["termux-open-url", "https://youtube.com/@hackers_colony_termux?si=18WolRHW-UiVybvf"])
    
    input(f"\n\n{BOLD}Press Enter after subscribing to Unlock the tool...{RESET}")

def run_real_scan():
    email = input(f"\n{YELLOW}Enter Target Gmail: {RESET}")
    print(f"\n{GREEN}[+] Initializing Real-Time OSINT Scan for: {email}{RESET}")
    print(f"{GREEN}[+] Please wait, gathering footprint...{RESET}\n")
    
    ghunt_path = os.path.join("ghunt", "ghunt.py")
    
    if os.path.exists(ghunt_path):
        # Real GHunt Execution
        os.system(f"python3 {ghunt_path} email {email}")
    else:
        print(f"{RED}[!] Error: Engine not found!{RESET}")
        
    input(f"\n{BOLD}Press Enter to return to menu...{RESET}")

def main():
    lock_screen()
    setup_engine()
    
    while True:
        banner()
        print("1. Run HCO-GHUNT Scan")
        print("2. Exit")
        choice = input(f"\n{BOLD}HCO@termux >> {RESET}")
        
        if choice == '1':
            run_real_scan()
        elif choice == '2':
            print(f"{RED}Exiting HCO-GHUNT...{RESET}")
            sys.exit()
        else:
            continue

if __name__ == "__main__":
    main()
