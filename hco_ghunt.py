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

# Headers for Real Scanning
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Website List (100+ targets possible here)
SITES = [
    ("Instagram", "https://www.instagram.com/{}"), ("Twitter", "https://twitter.com/{}"),
    ("GitHub", "https://github.com/{}"), ("Pinterest", "https://www.pinterest.com/{}"),
    ("Snapchat", "https://www.snapchat.com/add/{}"), ("Telegram", "https://t.me/{}"),
    ("Reddit", "https://www.reddit.com/user/{}"), ("Steam", "https://steamcommunity.com/id/{}"),
    ("WordPress", "https://{}.wordpress.com"), ("Medium", "https://medium.com/@{}"),
    ("SoundCloud", "https://soundcloud.com/{}"), ("Vimeo", "https://vimeo.com/{}"),
    ("Behance", "https://www.behance.net/{}"), ("Flickr", "https://www.flickr.com/people/{}"),
    ("About.me", "https://about.me/{}"), ("Tumblr", "https://{}.tumblr.com"),
    ("Discord", "https://discord.com/users/{}"), ("Twitch", "https://twitch.tv/{}")
]

def lock_screen():
    os.system('clear')
    print(f"{RED}{BOLD}!!! THIS TOOL IS LOCKED !!!{RESET}")
    print(f"{YELLOW}To use this tool, you need to Subscribe and click on the Bell Icon.{RESET}")
    print(f"{GREEN}Redirecting you to YouTube in...{RESET}")
    for i in range(7, -1, -1):
        print(f"{BOLD}{i}{RESET}", end=" ", flush=True)
        time.sleep(1)
    subprocess.run(["termux-open-url", "https://youtube.com/@hackers_colony_termux?si=18WolRHW-UiVybvf"])
    input(f"\n\n{BOLD}Press Enter after subscribing to Unlock...{RESET}")

def banner():
    os.system('clear')
    print(f"{GREEN}{BOLD}  _    _  _____ ____  {RESET}")
    print(f"{GREEN} | |  | |/ ____/ __ \\ {RESET}")
    print(f"{GREEN} | |__| | |   | |  | |{RESET}")
    print(f"{GREEN} |  __  | |   | |  | |{RESET}")
    print(f"{GREEN} | |  | | |___| |__| |{RESET}")
    print(f"{GREEN} |_|  |_|\\_____\\____/ {RESET}")
    print(f"{RED}HCO-GHUNT BY AZHAR | HCO TEAM{RESET}\n")

def run_scan():
    user = input(f"{YELLOW}Enter Gmail ID/Username to scan: {RESET}").split('@')[0]
    print(f"\n{GREEN}[+] Starting Scan on {len(SITES)} platforms...{RESET}\n")
    
    found = []
    for name, url in SITES:
        print(f"{YELLOW}[SCANNING]{RESET} {name: <15}", end="\r")
        try:
            r = requests.get(url.format(user), headers=HEADERS, timeout=3)
            if r.status_code == 200:
                print(f"{GREEN}[FOUND] >> {name: <15} (AVAILABLE){RESET}")
                found.append(name)
            else:
                pass # Not found list me shor nahi machayenge
        except:
            pass
    
    print(f"\n{BOLD}{GREEN}--- SCAN COMPLETE ---{RESET}")
    print(f"{YELLOW}Total Accounts Found: {len(found)}{RESET}")
    for i, name in enumerate(found, 1):
        print(f"{YELLOW}{i}. {name}{RESET}")
    input(f"\n{BOLD}Press Enter to return...{RESET}")

def main():
    lock_screen()
    while True:
        banner()
        print("1. Run Tool")
        print("2. Exit")
        ch = input(f"\n{BOLD}HCO@termux >> {RESET}")
        if ch == '1': run_scan()
        elif ch == '2': sys.exit()

if __name__ == "__main__":
    main()
