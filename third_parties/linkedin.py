from dotenv import load_dotenv
import os
import requests
load_dotenv()

def scrape_linkedin_profile(linkedin_url: str, mock: bool = False):

   response = requests.get(linkedin_url, timeout=10)
   if response.status_code != 200:
       raise Exception(f"Failed to fetch LinkedIn profile: {response.status_code}")
   
   data = response.json().get("person")

   data = {
       k:v
       for k, v in data.items()
       if v not in [None, "", [], {}] and k not in ["certificates"]
   }

   return data

if __name__ == "__main__":

    url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
    res = scrape_linkedin_profile(url, mock=True)
    print(res)
    
    