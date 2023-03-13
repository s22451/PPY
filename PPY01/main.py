import webbrowser
import requests as requests

dateurl = input("Podaj stronę internetową: ")



date1 = input("podaj 1. date w formacie rok-miesiac-dzien = 20230126: ")
url = "https://archive.org/wayback/available?url=" + dateurl + "&timestamp=" + str(date1)
response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

date2 = input("podaj 2. date w formacie rok-miesiac-dzien = 20230126: ")
url2 = "https://archive.org/wayback/available?url=" + dateurl + "&timestamp=" + str(date2)
response = requests.get(url2)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

date3 = input("podaj 3. date w formacie rok-miesiac-dzien = 20230126: ")
url3 = "https://archive.org/wayback/available?url=" + dateurl + "&timestamp=" + str(date3)
response = requests.get(url3)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)