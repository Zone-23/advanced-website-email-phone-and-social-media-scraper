thonimport re

def extract_phone_numbers(soup):
    phone_numbers = set()
    phone_pattern = r'\+?\d{1,4}[\s\-]?\(?\d{1,3}\)?[\s\-]?\d{1,4}[\s\-]?\d{1,4}'
    for text in soup.stripped_strings:
        phone_numbers.update(re.findall(phone_pattern, text))
    return list(phone_numbers)