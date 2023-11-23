def is_palindrome(input_str):
   
    cleaned_str = ''.join(input_str.split()).lower()
    
    return cleaned_str == cleaned_str[::-1]

word = "madam"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
