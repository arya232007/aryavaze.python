import re
phone = input("Enter phone number: ")
email = input("Enter email ID: ")

# Simple patterns
phone_pattern = "^[6-9]\d{9}$" # Exactly 10 digits
email_pattern = r"^\w+@\w+\.\w{2,}$" # Basic email format

# Check phone number
if re.match(phone_pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

# Check email
if re.match(email_pattern, email):
    print("Valid Email ID")
else:
    print("Invalid Email ID")
