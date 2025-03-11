import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(url: str, mock: bool = False):
    if mock:
        m_url = "https://gist.githubusercontent.com/shasank27/deacaa0be2655ab346c3549fb6299876/raw/914e337a7c56d4cfd72d648cc86623a43decfbb4/test.json"
        profile_url = "https://gist.githubusercontent.com/shasank27/31887f7c9af1b2b96c9d0e73bb97cf6a/raw/c99da7c76919a086939f2d52101f637d7a02157b/shasank-scrapin.json"
        response = requests.get(
            m_url,
            timeout=10
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": url
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10
        )
    data = response.json().get("person")
    data = { 
        k: v 
        for k, v in data.items()
        if not v in ([], "", None) and k not in ["certifications"]
    }
    return data

if __name__ == "__main__":
    print("Let's scrape")
    print(scrape_linkedin_profile("https://api.scrapin.io/enrichment/profile", mock=True))