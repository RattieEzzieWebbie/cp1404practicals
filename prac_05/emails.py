"""
Emails
Estimate: 25 minutes
Actual:   30 minutes
"""


def extract_name(email):
    """Extracts a name from the given email."""
    name_part = email.split('@')[0]
    name = " ".join(name_part.split('.')).title()
    return name


email_to_name = {}

email = input("Email: ").strip()
while email:
    suggested_name = extract_name(email)
    confirm = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()
    if confirm and confirm != 'y':
        suggested_name = input("Name: ").strip().title()

    email_to_name[email] = suggested_name
    email = input("Email: ").strip()

print("\nStored Emails and Names:")
for email, name in email_to_name.items():
    print(f"{name} ({email})")