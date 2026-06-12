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

def banner():
    os.system('clear')
    print(f"{RED}{BOLD}  _    _  _____ ____  ")
    print(" | |  | |/ ____/ __ \ ")
    print(" | |__| | |   | |  | |")
    print(" |  __  | |   | |  | |")
    print(" | |  | | |___| |__| |")
    print(" |_|  |_|\_____\____/ ")
    print(f"{RESET}{RED}HCO-GHUNT BY AZHAR{RESET}\n")

def lock_system():
    os.system('clear')
    print(f"{RED}{BOLD}!!! TOOL LOCKED !!!{RESET}")
    print(f"{YELLOW}To unlock this tool, you must support the channel.{RESET}")
    print("You will be redirected to YouTube. Please Like, Subscribe & Hit Bell Icon.")
    print(f"\n{GREEN}Redirecting in...{RESET}", end="", flush=True)
    
    for i in range(5, 0, -1):
        print(f" {i}", end="", flush=True)
        time.sleep(1)
    
    # YouTube Redirect
    subprocess.run(["termux-open-url", "https://youtube.com/@hackers_colony_termux?si=18WolRHW-UiVybvf"])
    
    print(f"\n\n{YELLOW}Redirected!{RESET}")
    input(f"{BOLD}Enter here after subscribing to Unlock the tool...{RESET}")

def run_real_scan():
    email = input(f"\n{YELLOW}Enter Target Email to Scan: {RESET}")
    print(f"\n{GREEN}[+] Initializing OSINT Engine...{RESET}")
    
    # Check folder path inside current directory
    ghunt_path = os.path.join(os.getcwd(), "ghunt", "ghunt.py")
    
    if os.path.exists(ghunt_path):
        os.system(f"python3 {ghunt_path} email {email}")
    else:
        print(f"\n{RED}[!] Error: 'ghunt' directory/file not found!{RESET}")
        print(f"{YELLOW}[!] Run: 'git clone https://github.com/mxrch/ghunt' inside this folder.{RESET}")
    
    input(f"\n{BOLD}Press Enter to return to menu...{RESET}")

def main():
    # Pehle Lock hoga
    lock_system()
    
    # Phir Menu loop
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
