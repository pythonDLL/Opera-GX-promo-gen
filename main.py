"""Really gay ass code."""
import httpx
from colorama import Fore
import os, time, ctypes, threading, json

genned = 0
failed = 0
config = json.load(open('config.json'))
def updateTitle():
    global genned
    global failed
    ctypes.windll.kernel32.SetConsoleTitleW(f"[ .gg/glossy ] Generated -> {genned} Failed -> {failed}")
def console():
    os.system("cls" or "clear")
    updateTitle()
    print(f'[{Fore.GREEN}+{Fore.WHITE}] Connected.')
    time.sleep(2)
    os.system("cls" or "clear")

def main():
    global genned
    global failed
    client = httpx.Client()

    resp = client.post("https://api.discord.gx.games/v1/direct-fulfillment", json={
        "partnerUserId": "16fde399c3739593bb0beb1b0cbf1e1122bb20d7f76ac51ef20b183ab453e605"
    })
    if resp.status_code == 200:
        print(f'[{Fore.BLUE}~{Fore.WHITE}] promo -> https://discord.com/billing/partner-promotions/1180231712274387115/{resp.json()["token"]}')
        with open('promo.txt', 'a') as f:
            f.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{resp.json()['token']}"+"\n")

        genned+=1
    else:
        failed+=1

    updateTitle()

if __name__ == "__main__":
    console()
    while True:
        if threading.active_count() < config['threads']:
            threading.Thread(target=main).start()