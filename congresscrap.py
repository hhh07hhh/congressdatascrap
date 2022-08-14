


import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest





sponsors = []
cospnmbrsa = []
cospnames = []
linko = []
titless = []
comittes = []
trackss = []






result = requests.get("https://www.congress.gov/search?q=%7B%22source%22%3A%22legislation%22%7D&pageSize=100&page=2")


# you can change the link to whatever page you want in congress.gov


src = result.content





soup = BeautifulSoup(src, "lxml")






blocks = soup.find_all("li", {"class":"expanded"})

for block in blocks:
    
    title = block.find("span", {"class":"result-title"})
    
    committe = block.find_all("span",{"class":"result-item"})
    hh = [item.text.strip() for item in committe]
    
    o = hh[1].replace('Committees: '," ")
    
    
    comittes.append(o)
    
    tracker = block.find("li", {"class":"selected"})
    
    track = [item.text.strip() for item in tracker]
    
    
    s = track[0]
    trackss.append(s)
    
    
    
    
    titless.append(title.text.strip())
    sponsor = block.find("span", {"class":"result-item"})
    sponrs = sponsor.find("a", {"target":"_blank"})
    
    a=sponrs.text
    
    sponsors.append(a)
    
    cosponsor = block.find("span", {"class":"result-item"})
    
    cospnsr = cosponsor.find_all("a")[-1]
    b=cospnsr.text
    cospnmbrs = b
    cospnmbrsa.append(cospnmbrs)
    
  
    
    
    if cospnmbrs != "0" :
        urls = cosponsor.find_all("a")
        'https://www.congress.gov/' + urls[1]['href']
        link = 'https://www.congress.gov/' + urls[1]['href']        
                
        result = requests.get(link)
        src = result.content
        souproot = BeautifulSoup(src, "lxml")
        
    
        cospname = souproot.find("table", {"class":"item_table"})
        
        csopnames = cospname.find_all("a",{"target":"_blank"} )
        
        hamid = [item.text.strip() for item in csopnames]
        #print(hamid)
      
        
        hamids='|'.join(hamid)
        
        cospnames.append(hamids)
    else:
        cospnames.append(" ")
    
       





file_list = [titless, sponsors, cospnmbrsa, cospnames, comittes, trackss]
exported = zip_longest(*file_list)

with open(" folder path to store the csv file exemple :C:\\Users\\\Bureau\\pyproject\\congress.csv", "w", encoding = 'utf-8') as myfile:
        wr = csv.writer(myfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        wr.writerow(["title", "sponsor_name", "cosponsor_number", "cosponsor_name", "comittes", "track stage"]) #these are the headers that would created on csv file
        wr.writerows(exported)








# In[ ]:




