
from projectFolder.scrapData.scrapData.spiders.getLinks import googlesearch

for link in googlesearch(query = "how to get job at tesla"):
    print(link)