import string

def evaluate_password_strength(password):
 
    min_length = 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(char in string.punctuation for char in password)

 
    if len(password) < min_length:
        return "Weak: Password is too short."
    elif not has_uppercase or not has_lowercase:
        return "Weak: Password should contain both uppercase and lowercase letters."
    elif not has_digit:
        return "Weak: Password should contain at least one digit."
    elif not has_special_char:
        return "Moderate: Consider adding a special character for increased security."
    else:
        return "Strong: Password meets all criteria for strength."


user_password = input("Enter your password: ")
result = evaluate_password_strength(user_password)
print(result)
