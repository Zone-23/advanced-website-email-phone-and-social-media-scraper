thonimport re

def extract_emails(soup):
    emails = set()
    for a_tag in soup.find_all('a', href=True):
        if "mailto:" in a_tag['href']:
            email = a_tag['href'].split("mailto:")[1]
            emails.add(email)
    return list(emails)