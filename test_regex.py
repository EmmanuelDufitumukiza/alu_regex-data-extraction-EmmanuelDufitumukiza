"""
Runs checks on different regex-based data extraction functionalities.
"""

import regex_data_extraction as extractor

def check_emails():
    text = "Contact us at user@example.com or firstname.lastname@company.co.uk"
    result = extractor.extract_data(text)

    print("Email Extraction Test:")
    expected = ["user@example.com", "firstname.lastname@company.co.uk"]
    actual = result["emails"]

    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print("Result:", "PASSED" if set(expected) == set(actual) else "FAILED")
    print()

def check_urls():
    text = "Visit https://www.example.com or https://subdomain.example.org/page"
    result = extractor.extract_data(text)

    print("URL Extraction Test:")
    expected = ["https://www.example.com", "https://subdomain.example.org/page"]
    actual = result["urls"]

    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print("Result:", "PASSED" if set(expected) == set(actual) else "FAILED")
    print()

def check_phones():
    text = "Call (123) 456-7890 or 123-456-7890 or 123.456.7890"
    result = extractor.extract_data(text)

    print("Phone Number Extraction Test:")
    expected = ["(123) 456-7890", "123-456-7890", "123.456.7890"]
    actual = result["phone_numbers"]

    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print("Result:", "PASSED" if set(expected) == set(actual) else "FAILED")
    print()

def check_cards():
    text = "Use 1234 5678 9012 3456 or 1234-5678-9012-3456 for payment"
    result = extractor.extract_data(text)

    print("Credit Card Extraction Test:")
    expected = ["1234 5678 9012 3456", "1234-5678-9012-3456"]
    actual = result["credit_cards"]

    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print("Result:", "PASSED" if set(expected) == set(actual) else "FAILED")
    print()

def check_times():
    text = "Working hours: 14:30 to 17:00 and 9:30 AM to 5:30 PM"
    result = extractor.extract_data(text)

    print("Time Format Extraction Test:")
    expected = ["14:30", "17:00", "9:30 AM", "5:30 PM"]
    actual = result["times"]

    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print("Result:", "PASSED" if set(expected) == set(actual) else "FAILED")
    print()

def run_tests():
    print("===== Starting Regex Extraction Tests =====\n")
    check_emails()
    check_urls()
    check_phones()
    check_cards()
    check_times()
    print("===== All Tests Finished =====")

if __name__ == "__main__":
    run_tests()
