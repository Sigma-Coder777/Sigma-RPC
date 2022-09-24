from urllib import response
from urllib.request import urlopen
from pypresence import Presence
import json
import random
import urllib
import time
import requests
token ="1023109691909353543"

def getQuote():
    api_key ='sOwruRjTbh/LL4ZgCSeVqw==H3P8TzQBeoiaLrJ9'
    category = 'alone'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
         quote = response.text.strip("[]")
         x = json.loads(quote)['quote']
         if len(x)<=128:
            return x
         else:
            return "GOD is watching Everything." #does this if quotes length exceeds        

         
         
         
    else:
        print("Error:", response.status_code, response.text)
        return "GOD is watching Everything."
  
    
RPC =Presence(token)
RPC.connect()
time_elapsed = int(time.time())
#unusual way of wile true xD
Nikhil = "Sigma"
while Nikhil == "Sigma":
    #gets anime gifs
    gifapi ="https://api.otakugifs.xyz/gif?reaction=angrystare"
    gifresponse =urlopen(gifapi)
    gifjson = json.loads(gifresponse.read())

    #upadating RPC
    RPC.update( 
       
        large_image=gifjson["url"],
        state="Studying",
        details=getQuote(),
        start=int(time_elapsed)

    )
    time.sleep(6)
