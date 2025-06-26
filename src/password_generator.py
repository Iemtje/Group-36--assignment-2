"""
Password generation functions for signup system.
"""
import random
import string


def build_charset():
    charset = ""
    charset += string.ascii_lowercase
    charset += string.ascii_uppercase
    charset += string.digits
    charset += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    return charset


def generate_random_chars(charset, count):
    selected_chars = []
    for _ in range(count):
        selected_chars.append(random.choice(charset))
    return selected_chars


def shuffle_password_chars(char_list):
    shuffled_chars = char_list.copy()
    for i in range(len(shuffled_chars) - 1, 0, -1):
        j = random.randint(0, i)
        shuffled_chars[i], shuffled_chars[j] = shuffled_chars[j], shuffled_chars[i]
    return ''.join(shuffled_chars)


def validate_password_requirements(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True
    
    return has_upper and has_lower and has_digit and has_special


def generate_password(length=13, include_uppercase=True, include_lowercase=True, 
                     include_digits=True, include_special=True, exclude_similar=False,
                     special_chars="!@#$%^&*()_+-=[]{}|;:,.<>?", required_types=False, debug=False):
    """
    Generate a secure password with customizable options.
    """
    if length <= 0:
        raise ValueError("Password length must be positive")
    
    if not any([include_uppercase, include_lowercase, include_digits, include_special]):
        raise ValueError("At least one character type must be selected")
    
    charset = ""
    if include_lowercase:
        charset += string.ascii_lowercase
    if include_uppercase:
        charset += string.ascii_uppercase  
    if include_digits:
        charset += string.digits
    if include_special:
        charset += special_chars
        
    if exclude_similar:
        similar_chars = "0O1lI"
        charset = ''.join(c for c in charset if c not in similar_chars)
    
    if debug:
        print(f"Included char sets: {charset}")
    
    if required_types:
        required_count = sum([include_uppercase, include_lowercase, include_digits, include_special])
        if length < required_count:
            raise ValueError("Length too short for required character types")
        
        password_chars = []
        if include_uppercase:
            password_chars.append(random.choice(string.ascii_uppercase))
        if include_lowercase:
            password_chars.append(random.choice(string.ascii_lowercase))
        if include_digits:
            password_chars.append(random.choice(string.digits))
        if include_special:
            password_chars.append(random.choice(special_chars))
            
        remaining_length = length - len(password_chars)
        for _ in range(remaining_length):
            password_chars.append(random.choice(charset))
            
        return shuffle_password_chars(password_chars)
    else:
        password_chars = generate_random_chars(charset, length)
        return shuffle_password_chars(password_chars)
