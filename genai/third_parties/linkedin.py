import requests
import os

from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile():
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    linkedin_profile_url = os.environ['LINKEDIN_URL']
    response = requests.get(linkedin_profile_url, timeout=10)
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data


if __name__ == "__main__":
    print(scrape_linkedin_profile())