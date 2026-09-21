"""
Write a program using regular expressions(regex) to find email patterns.
"""
import re

def find_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, text)
    return emails


text = input("Enter text containing email addresses: ")

result = find_emails(text)

print("Email addresses found:")
for email in result:
    print(email)
"""
--> Output
Enter text containing email addresses: 
Contact me at anjali@gmail.com or support@example.com

Email addresses found:
anjali@gmail.com
support@example.com
"""
