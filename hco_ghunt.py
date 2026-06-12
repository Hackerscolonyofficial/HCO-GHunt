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

def lock_system():
    os.system('clear')
    print(f"{RED}{BOLD}!!! TOOL LOCKED !!!{RESET}")
    print(f"{YELLOW}To unlock this tool, you need to Subscribe and click the Bell Icon.{RESET}")
    print(f"\n{GREEN}Redirecting you to YouTube in...{RESET}")
    
    # 5-second countdown
    for i in range(5, 0, -1):
        print(f"{BOLD}{i}{RESET}...", end=" ", flush=True)
        time.sleep(1)
    
    subprocess.run(["termux-open-url", "https://youtube.com/@hackers_colony_termux?si=18WolRHW-UiVybvf"])
    print(f"\n\n{YELLOW}Redirecting to YouTube App...{RESET}")
    input(f"\n{BOLD}Press Enter after subscribing to Unlock the tool...{RESET}")

def run_scan():
    username = input(f"\n{YELLOW}Enter Username/Email to Scan: {RESET}")
    print(f"\n{GREEN}[+] Starting Deep OSINT Scan for: {username}{RESET}")
    print(f"{GREEN}[+] Scanning 15+ Platforms... Please wait.{RESET}\n")
    
    # List of platforms to scan
    sites = {
        "Instagram": "https://www.instagram.com/{}",
        "Twitter/X": "https://twitter.com/{}",
        "GitHub": "https://github.com/{}",
        "Pinterest": "https://www.pinterest.com/{}",
        "Snapchat": "https://www.snapchat.com/add/{}",
        "WordPress": "https://{}.wordpress.com",
        "Telegram": "https://t.me/{}",
        "Reddit": "https://www.reddit.com/user/{}",
        "Steam": "https://steamcommunity.com/id/{}",
        "Vimeo": "https://vimeo.com/{}",
        "SoundCloud": "https://soundcloud.com/{}",
        "Behance": "https://www.behance.net/{}",
        "Medium": "https://medium.com/@{}",
        "Flickr": "https://www.flickr.com/people/{}",
        "About.me": "https://about.me/{}"
    }
    
    for name, url in sites.items():
        try:
            # Username cleanup for URLs (Kuch sites handle nahi karti @gmail.com)
            clean_user = username.split('@')[0] if "@" in username else username
            formatted_url = url.format(clean_user)
            
            response = requests.get(formatted_url, timeout=3)
            if response.status_code == 200:
                print(f"{GREEN}[FOUND]{RESET} {name: <15} : {formatted_url}")
            else:
                print(f"{RED}[NOT FOUND]{RESET} {name: <15}")
        except:
            print(f"{RED}[ERROR]{RESET} {name: <15} : Connection Failed")
        time.sleep(0.2) # Thoda delay taaki scan pro lage
    
    input(f"\n{BOLD}Press Enter to return to menu...{RESET}")

def main():
    lock_system()
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
