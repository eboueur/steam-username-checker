import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

base_url = "https://steamcommunity.com/id/"

with open("input.txt", "r") as file:
    usernames = file.read().splitlines()

headers = CaseInsensitiveDict()
headers["Upgrade-Insecure-Requests"] = "1"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"

for username in usernames:
    user_url = base_url + username
    resp = requests.get(user_url, headers=headers)

    if "<title>Steam Community :: Error</title>" in resp.text:
        
        with open("output.txt", "r") as output_file:
            existing_usernames = output_file.read().splitlines()
            print(f"L'utilisateur '{username}' est déjà dans la liste.")
        if username not in existing_usernames:
            with open("output.txt", "a") as output_file:
                output_file.write(username + "\n")
                print(f"L'utilisateur '{username}' n'est pas pris.")
    else:
        print(f"L'utilisateur '{username}' est déjà pris.")
