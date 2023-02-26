import requests
from bs4 import BeautifulSoup
import os
url = 'http://xn-----6kcczalffeh6afgdgdi2apgjghic4org.xn--p1ai'
j = 0
for i in range(1,47):
    url_new = url+'/?page'+str(i)
    r = requests.get(url_new)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    
    for image in images:
        if 'stat' not in image['src']:
            link = url+image['src']
            j += 1
            with open(str(j)+'.jpg','wb') as f:
                im = requests.get(link)
                f.write(im.content)
                
        
