import json
import requests
import urllib3
from colorama import Fore, Style, init
import socks
import socket
import idna
import certifi
from charset_normalizer import detect

init(autoreset=True)

def setup_proxy():
    """Sets up the SOCKS proxy if needed."""
    try:
        proxy_enabled = input(Fore.YELLOW + "Do you want to use a SOCKS proxy? (y/n): " + Style.RESET_ALL).lower()
        if proxy_enabled == "y":
            proxy_host = input(Fore.YELLOW + "Enter the proxy address (e.g. 127.0.0.1): " + Style.RESET_ALL)
            proxy_port = int(input(Fore.YELLOW + "Enter the proxy port (e.g. 1080): " + Style.RESET_ALL))
            
            socks.set_default_proxy(socks.SOCKS5, proxy_host, proxy_port)
            socket.socket = socks.socksocket
            print(Fore.GREEN + "SOCKS proxy set up!" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "No SOCKS proxy set up." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error setting up the proxy: {e}" + Style.RESET_ALL)

def validate_webhook(url):
    """Validates the Discord webhook URL using HTTPS requests with SSL management."""
    try:
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        response = http.request('GET', url, timeout=5)
        
        if response.status == 200:
            return True
        else:
            return False
    except urllib3.exceptions.HTTPError as e:
        print(Fore.RED + f"Connection error: {e}" + Style.RESET_ALL)
        return False

def generate_config():
    """Generates the 'config.json' configuration file."""
    print(Fore.CYAN + "Welcome to the configuration generator!")
    
    setup_proxy()

    while True:
        webhook_url = input(Fore.YELLOW + "Enter the Discord webhook URL: " + Style.RESET_ALL)
        if validate_webhook(webhook_url):
            print(Fore.GREEN + "Valid webhook!")
            break
        else:
            print(Fore.RED + "Invalid URL. Please try again.")

    message = input(Fore.YELLOW + "Enter the message to send: " + Style.RESET_ALL)

    config = {
        "webhook_url": webhook_url,
        "message": message
    }

    try:
        with open("config.json", "w") as file:
            json.dump(config, file, indent=4)
        print(Fore.GREEN + "Configuration successfully saved to 'config.json'!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error saving the file: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    generate_config()
