import os
import time
import requests
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
    print(f"{RESET}{RED}HCO-OSINT PRO | REAL SCAN{RESET}\n")

def check_site(username, url):
    try:
        response = requests.get(url.format(username), timeout=5)
        if response.status_code == 200:
            return True
    except:
        return False
    return False

def run_scan():
    username = input(f"\n{YELLOW}Enter Username to Scan: {RESET}")
    print(f"{GREEN}[+] Searching Real-Time...{RESET}\n")
    
    # Ye asli websites hain jo check karegi
    sites = {
        "Instagram": "https://www.instagram.com/{}",
        "Twitter": "https://twitter.com/{}",
        "GitHub": "https://github.com/{}",
        "Pinterest": "https://www.pinterest.com/{}"
    }
    
    found = False
    for name, url in sites.items():
        if check_site(username, url):
            print(f"{GREEN}[FOUND]{RESET} {name}: {url.format(username)}")
            found = True
        else:
            print(f"{RED}[NOT FOUND]{RESET} {name}")
    
    if not found:
        print(f"\n{YELLOW}No data found for this username.{RESET}")
    input(f"\n{BOLD}Press Enter to return...{RESET}")

def main():
    # Lock Flow
    os.system('clear')
    print(f"{RED}{BOLD}!!! TOOL LOCKED !!!{RESET}")
    subprocess.run(["termux-open-url", "https://youtube.com/@hackers_colony_termux?si=18WolRHW-UiVybvf"])
    input(f"\n{BOLD}Press Enter after subscribing...{RESET}")
    
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
    
