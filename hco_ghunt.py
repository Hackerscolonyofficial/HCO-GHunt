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

# User-Agent headers (taaki website block na kare)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

def banner():
    os.system('clear')
    print(f"{RED}{BOLD}  _    _  _____ ____  ")
    print(" | |  | |/ ____/ __ \ ")
    print(" | |__| | |   | |  | |")
    print(" |  __  | |   | |  | |")
    print(" | |  | | |___| |__| |")
    print(" |_|  |_|\_____\____/ ")
    print(f"{RESET}{RED}HCO-OSINT PRO | REAL SCAN{RESET}\n")

def run_scan():
    username = input(f"\n{YELLOW}Enter Username/Email: {RESET}").split('@')[0]
    print(f"\n{GREEN}[+] Initializing Deep Scan for: {username}{RESET}")
    
    sites = {
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter/X": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Telegram": f"https://t.me/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "WordPress": f"https://{username}.wordpress.com",
        "Medium": f"https://medium.com/@{username}",
        "Behance": f"https://www.behance.net/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "About.me": f"https://about.me/{username}"
    }
    
    found_list = []
    not_found_list = []
    
    for name, url in sites.items():
        try:
            # Request with headers (Bot protection bypass)
            response = requests.get(url, headers=HEADERS, timeout=5)
            if response.status_code == 200:
                found_list.append(name)
            else:
                not_found_list.append(name)
        except:
            not_found_list.append(name)
    
    # RESULT PRINTING
    print(f"\n{BOLD}{GREEN}--- FOUND ({len(found_list)}) ---{RESET}")
    for item in found_list:
        print(f"{GREEN}[FOUND] >> {item}{RESET}")
        
    print(f"\n{BOLD}{RED}--- NOT FOUND ({len(not_found_list)}) ---{RESET}")
    for item in not_found_list:
        print(f"{RED}[NOT FOUND] >> {item}{RESET}")
        
    input(f"\n{BOLD}Press Enter to return...{RESET}")

def main():
    # Lock Flow
    os.system('clear')
    print(f"{RED}{BOLD}!!! TOOL LOCKED !!!{RESET}")
    subprocess.run(["termux-open-url", "https://youtube.com/@hackers_colony_termux?si=18WolRHW-UiVybvf"])
    input(f"\n{BOLD}Press Enter after subscribing to Unlock...{RESET}")
    
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
