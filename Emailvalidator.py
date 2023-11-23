import re

def is_valid_email(email):
    
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    match = email_pattern.match(email)
    
    return bool(match)

email_address = "jishnukumar.vj@gmail.com"
if is_valid_email(email_address):
    print(f"{email_address} is a valid email address.")
else:
    print(f"{email_address} is not a valid email address.")
