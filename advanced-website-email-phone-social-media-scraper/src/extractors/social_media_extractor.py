thonimport re

def extract_social_media_links(soup):
    social_links = {
        "facebook": None,
        "twitter": None,
        "linkedin": None,
        "instagram": None
    }
    
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if "facebook.com" in href and not social_links["facebook"]:
            social_links["facebook"] = href
        elif "twitter.com" in href and not social_links["twitter"]:
            social_links["twitter"] = href
        elif "linkedin.com" in href and not social_links["linkedin"]:
            social_links["linkedin"] = href
        elif "instagram.com" in href and not social_links["instagram"]:
            social_links["instagram"] = href
            
    return social_links