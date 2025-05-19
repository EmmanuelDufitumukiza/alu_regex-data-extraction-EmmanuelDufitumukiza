# alu_regex-data-extraction-EmmanuelDufitumukiza

A Python program that leverages regular expressions to identify and extract specific types of information from plain text.

Supported Data Types:

Email addresses
Web URLs
Telephone numbers
Credit card numbers
Time expressions (12-hour and 24-hour formats)

The script will first analyze sample text and display the results.
Then, it will prompt you to enter your own text for analysis.

Regex Patterns Explained
Email Addresses
pythonemail_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

Matches: user@example.com, firstname.lastname@company.co.uk
Explanation: Captures username, @ symbol, domain name, and domain extension

URLs
pythonurl_pattern = r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'

Matches: https://www.example.com, https://subdomain.example.org/page
Explanation: Captures protocol (http/https), domain, and optional path

Phone Numbers
pythonphone_pattern = r'(?:\(\d{3}\)\s*|\d{3}[-.])\d{3}[-.]?\d{4}'

Matches: (123) 456-7890, 123-456-7890, 123.456.7890
Explanation: Captures various US phone number formats with different separators

Credit Card Numbers
pythoncredit_card_pattern = r'\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}'

Matches: 1234 5678 9012 3456, 1234-5678-9012-3456
Explanation: Captures 16-digit numbers with optional spaces or hyphens

The Formats of Time
pythontime_pattern = r'(?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s*(?:AM|PM|am|pm)|(?:(?:[01]?[0-9]|2[0-3]):[0-5][0-9]))'

Matches: 14:30 (24-hour format), 2:30 PM (12-hour format)
Explanation: Captures both 12-hour and 24-hour time formats.
