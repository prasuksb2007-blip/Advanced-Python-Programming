"""
Write a program using regular expressions(regex) to find email patterns.
"""
import re

def extract_email_addresses(text):
    # Regex pattern matching username@domain.extension
    # Username: letters, digits, dots, hyphens, underscores ([a-zA-Z0-9._%+-]+)
    # Domain: letters, digits, hyphens ([a-zA-Z0-9.-]+)
    # Extension: letters, 2 to 4 characters long ([a-zA-Z]{2,4})
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
    
    # re.findall() returns a list of all matching email patterns
    emails = re.findall(email_pattern, text)
    return emails

# Sample execution
if __name__ == "__main__":
    sample_text = """
    Hello! You can reach out to support at support.team@domain-name.com or 
    john_doe123@example.org. For queries, contact info@company.co or admin@test.net.
    Invalid formats like user@, @domain.com, or test@domain.123 should be ignored.
    """

    found_emails = extract_email_addresses(sample_text)

    print("Found Email Addresses:")
    for idx, email in enumerate(found_emails, start=1):
        print(f"{idx}. {email}")
"""
--> Output
Found Email Addresses:
1. support.team@domain-name.com
2. john_doe123@example.org
3. info@company.co
4. admin@test.net
"""
