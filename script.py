import pandas as pd     #Module loads saved data from csv, text and html files
import requests         #Uses requests to access servers and their information
from io import StringIO
url ="https://en.wikipedia.org/wiki/Bukayo_Saka"   #Wikipedia = server, URL is the location of all the information being held
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}


response = requests.get(url, headers = headers)


print(response.status_code)
print(len(response.text))
peripherals = pd.read_html(StringIO(response.text))

for table in peripherals:
    print(table)

#headers = {
#    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#    "Accept-Language": "en-US,en;q=0.9",
#    "Accept-Encoding": "gzip, deflate, br",
#    "Connection": "keep-alive",
#    "Upgrade-Insecure-Requests": "1"
#}