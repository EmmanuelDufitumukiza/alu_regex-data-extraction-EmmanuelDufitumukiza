import re

email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
url_regex = r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
phone_regex = r'(?:\(\d{3}\)\s*|\d{3}[-.])\d{3}[-.]?\d{4}'
card_regex = r'\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}'
time_regex = r'(?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s*(?:[APap][Mm])|(?:[01]?[0-9]|2[0-3]):[0-5][0-9])'

def find_data(text):
    return {
        'emails': re.findall(email_regex, text),
        'urls': re.findall(url_regex, text),
        'phones': re.findall(phone_regex, text),
        'cards': re.findall(card_regex, text),
        'times': re.findall(time_regex, text)
    }

def display(results):
    print("\n===== Extracted Data =====")
    for key, values in results.items():
        print(f"\n{key.upper()}:")
        if values:
            for v in values:
                print(f"  - {v}")
        else:
            print("  None found")

def run_demo():
    text = """
    Reach out via user@example.com or firstname.lastname@company.co.uk
    Browse at https://www.example.com or https://subdomain.example.org/page
    Phone us on (123) 456-7890, 123-456-7890, or 123.456.7890
    Accepted card numbers: 1234 5678 9012 3456, 1234-5678-9012-3456
    We're open from 14:30 until 17:00 and 9:30 AM to 5:30 PM
    """

    results = find_data(text)
    display(results)

    print("\n===== Try It Yourself =====")
    print("Paste some text and press Ctrl+D (Linux/macOS) or Ctrl+Z (Windows) to finish:")
    
    collected = ""
    try:
        while True:
            collected += input() + "\n"
    except EOFError:
        pass

    if collected.strip():
        user_data = find_data(collected)
        display(user_data)

if __name__ == "__main__":
    run_demo()
