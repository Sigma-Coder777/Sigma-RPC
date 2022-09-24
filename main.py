from pypresence import Presence
import json
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
            return "Alone is better then toxic friends"
        

         
         
         
    else:
        print("Error:", response.status_code, response.text)
        return "Padhle pehle"
  
    



RPC =Presence(token)
RPC.connect()


Nikhil = "Sigma"

while Nikhil == "Sigma":
   
    RPC.update( 
       
        large_image="anime_pfp_4",
        state="Studying",
        details=getQuote(),
        start=int(time.time())


    )
    time.sleep(60)
