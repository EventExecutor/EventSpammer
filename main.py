import json
import requests
import time
from colorama import Fore, Style, init

init(autoreset=True)

def load_config():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(Fore.RED + "Errore: 'config.json' non trovato." + Style.RESET_ALL)
        exit()
    except json.JSONDecodeError:
        print(Fore.RED + "Errore: 'config.json' contiene errori di formattazione." + Style.RESET_ALL)
        exit()

def send_message(webhook_url, message):
    try:
        response = requests.post(webhook_url, json={"content": message})
        if response.status_code == 204:
            print(Fore.GREEN + "[Sent] " + Style.RESET_ALL + f"{message}")
        else:
            print(Fore.RED + f"Errore nell'invio del messaggio: {response.status_code}" + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Errore di connessione: {e}" + Style.RESET_ALL)

def main():
    print(Fore.WHITE + "-----------------------------")
    print(Fore.GREEN + "EventSpammer - Version 1.0")
    print(Fore.WHITE + "-----------------------------" + Style.RESET_ALL)

    config = load_config()
    webhook_url = config.get("webhook_url")
    message = config.get("message")

    if not webhook_url or not message:
        print(Fore.RED + "Errore: 'webhook_url' o 'message' mancante in 'config.json'." + Style.RESET_ALL)
        exit()

    print(Fore.CYAN + "Inizio invio messaggi..." + Style.RESET_ALL)
    while True:
        send_message(webhook_url, message)
        time.sleep(1)  # Imposta un delay di 1 secondo per evitare spam eccessivo

if __name__ == "__main__":
    main()
