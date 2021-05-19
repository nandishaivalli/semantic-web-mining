import scrapy ,re
from .getLinks import googlesearch

class getLinks(scrapy.Spider):
    name = "getData"
   
    #start_urls = googlesearch(query=q)
    
    def start_requests(self):
        self.q = "how to install python in windows"
        urls =  googlesearch(query=self.q)
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        title = response.css('title::text').extract()
        p = []
        h1= []

        #allp = response.css('p::text').getall()
        allh1 = response.css('h1::text').getall()
        myurl = response.request.url
        
        # for i in range(len(allp)):
        #     # clean the data remove un wanted charactors
        #     allp[i] = re.sub(r'\W+',' ',allp[i])
        #     if any(ele in allp[i] for ele in (self.q).split(" ")) :
        #         p.append(allp[i])
        
        for i in range(len(allh1)):
            # clean the data remove un wanted charactors
            allh1[i] = re.sub(r'\W+',' ',allh1[i])
            if allh1[i] != " " :
                 h1.append(allh1[i])
      
        yield{ "url": myurl,"title":title,"h1":h1}
        
        #yield{ "url": myurl,"title":title,"h1":h1,"p":p }
        # for title in response.css('title').extract():
        #     yield response.follow(title,callable=self.parse_article)
        

