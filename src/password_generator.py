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
    has_upper = False_
