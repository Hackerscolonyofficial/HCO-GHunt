import os
import sys
import time

# Colors
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BOLD = '\033[1m'
RESET = '\033[0m'

def banner():
    os.system('clear')
    print(f"{RED}{BOLD}  _    _  _____ ____  ")
    print(" | |  | |/ ____/ __ \ ")
    print(" | |__| | |   | |  | |")
    print(" |  __  | |   | |  | |")
    print(" | |  | | |___| |__| |")
    print(" |_|  |_|\_____\____/ ")
    print(f"{RESET}{RED}HCO-GHUNT REAL OSINT ENGINE{RESET}\n")

def run_real_scan():
    email = input(f"{YELLOW}Enter Target Email to Scan: {RESET}")
    print(f"\n{GREEN}[+] Initializing Real-Time OSINT Engine...{RESET}")
    print(f"{GREEN}[+] Targeting: {email}{RESET}\n")
    
    # Ye path check karega ki official GHunt engine hai ya nahi
    if os.path.exists("ghunt/ghunt.py"):
        # Real GHunt Command Execution
        os.system(f"python3 ghunt/ghunt.py email {email}")
    else:
        print(f"{RED}[!] Error: 'ghunt' folder not found!{RESET}")
        print(f"{YELLOW}[!] Please run: git clone https://github.com/mxrch/ghunt{RESET}")
    
    input(f"\n{BOLD}Press Enter to return to menu...{RESET}")

def main():
    while True:
        banner()
        print("1. Run HCO-GHUNT (Real OSINT)")
        print("2. Exit")
        choice = input(f"\n{BOLD}HCO@termux >> {RESET}")
        
        if choice == '1':
            run_real_scan()
        elif choice == '2':
            sys.exit()

if __name__ == "__main__":
    main()
