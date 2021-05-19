import requests,re

from bs4 import BeautifulSoup
#search query

    
def googlesearch(query):
    # 
    #query = "tesla"
    f = open('data.json','r+')
    f.truncate(0)
    f.close()

    f = open("query.txt",'w')
    f.write(query)
    f.close()
    

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    # connect to internet and search google  
    try:
        #print("Getting search results")
        request = requests.get("https://www.google.dz/search?q="+query)
        #print(request.status_code)
    except (requests.ConnectionError ,requests.Timeout) as exception:
        print("Internet connection lost...")
        exit()

    # read the page to get only the links from google and parse it 
    soup = BeautifulSoup(request.content,'html.parser')
    links = soup.findAll("a",href=True)
    csvRows = []
    #print(links)
   
    for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        url = re.split(":(?=http)",link["href"].replace("/url?q=",""))[0].split("&")[0].replace(",","")
        
        #if requests.get(url,headers=headers,timeout=5).status_code==200:

        csvRows.append(url)
        #csvRows.append((re.split(":(?=http)",link["href"].replace("/url?q=",""))))
        #csvRows.append(link['href'].split("&")[0])

    #write the links to csv file

    # csvfields = ["links"]
    # filename = ".\searchresults.csv"
    # print("Writing to %s file ..." % filename.split('\\')[-1])

    # with open(filename,'w') as csvfile:
    #     csvWriter = csv.writer(csvfile)

    #     #write fields 
    #     csvWriter.writerow(csvfields)

    #     #write data rows

    #     csvWriter.writerows(csvRows)
    
    return(csvRows)    

# if __name__=="__main__":
#     #searchObject = getlinks()
#     print(googlesearch("tesla"))