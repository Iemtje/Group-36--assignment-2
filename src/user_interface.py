"""
Username validation functions for signup system.
"""

def validate_username_length(username, min_length=3, max_length=20):
    return min_length <= len(username) <= max_length


def validate_username_characters(username):
    return all(char.isalnum() for char in username)


def check_username_exists(username, user_database):
    return any(existing_user.lower() == username.lower() for existing_user in user_database)
