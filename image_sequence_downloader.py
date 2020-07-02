# Imports

import urllib.request
import os

# Functions

def extract_base_link(url):
    
    base_link = url[:url.rfind('/')] + "/"
    
    return(base_link)

def extract_folder_name(url):
    
    base_link = url[:url.rfind('/')] 
    
    foldername = base_link[base_link.rfind('/')+1:] 
    
    return(foldername)

# Main

source_link = "https://www.games-workshop.com/resources/catalog/product/threeSixty/99120199073_DaemonifugeEphraelSternKyganilSpin2360/02.jpg"



# Header needed so that browser doesn't notice that we're a script
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}

try:
    
    os.mkdir("./" + extract_folder_name(source_link))
    
except FileExistsError:
    
    print("Directory already exists")

reached_end = False    
i = 1

while not reached_end:    
    
    try:

        lnk = extract_base_link(source_link) + f"{i:02d}" + ".jpg"

        request_= urllib.request.Request(lnk, None, headers) 
        response = urllib.request.urlopen(request_)
        
        f = open("./" + extract_folder_name(lnk) + "/" + f"{i:02d}" + ".jpg" ,'wb')
        f.write(response.read())
        f.close()
        
        i += 1

    except:

        reached_end = True
        print("Found", i-1, "images")