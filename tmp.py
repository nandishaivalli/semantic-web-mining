import requests

from bs4 import BeautifulSoup
#search query
query = "tesla"
try:
        
    request = requests.get("https://www.google.dz/search?q="+query)

except (requests.ConnectionError ,requests.Timeout) as exception:
    print("Internet connection lost...")
    exit()

# read the page to get only the links from google and parse it 
soup = BeautifulSoup(request.content,'html.parser')
#print(soup.title.text)

table = soup.find_all("table")

print(table)