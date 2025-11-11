thonimport requests
from bs4 import BeautifulSoup
from extractors.email_extractor import extract_emails
from extractors.phone_extractor import extract_phone_numbers
from extractors.social_media_extractor import extract_social_media_links
from utils.helpers import save_data

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        emails = extract_emails(soup)
        phone_numbers = extract_phone_numbers(soup)
        social_media_links = extract_social_media_links(soup)

        data = {
            "emails": emails,
            "phoneNumbers": phone_numbers,
            "socialMediaLinks": social_media_links
        }

        save_data(data)
    except requests.RequestException as e:
        print(f"Error fetching the website {url}: {e}")

if __name__ == "__main__":
    url = "https://example.com"
    scrape_website(url)