import pytest
from src.signup import is_valid_username, contains_forbidden_words, is_duplicate_username

def test_is_valid_username():
    # Valid usernames (5–15 chars, only letters, digits, or underscores)
    assert is_valid_username("validuser") is True
    assert is_valid_username("valid_user_123") is True
    # Invalid (too short)
    assert is_valid_username("user") is False
    # Invalid (too long)
    assert is_valid_username("a" * 16) is False
    # Invalid (contains non-alphanumeric or underscore)
    assert is_valid_username("user@") is False
    # Invalid (not a string)
    assert is_valid_username(123) is False

def test_contains_forbidden_words():
    # Contains forbidden word (case-insensitive)
    assert contains_forbidden_words("admin") is True
    assert contains_forbidden_words("myAdmin") is True
    assert contains_forbidden_words("root") is True
    # Does not contain forbidden word
    assert contains_forbidden_words("user") is False
    # Custom forbidden list
    custom_forbidden = ["bad", "evil"]
    assert contains_forbidden_words("baduser", forbidden=custom_forbidden) is True
    assert contains_forbidden_words("gooduser", forbidden=custom_forbidden) is False

def test_is_duplicate_username():
    existing = ["user1", "user2", "user3"]
    # Duplicate (case-insensitive)
    assert is_duplicate_username("user1", existing) is True
    assert is_duplicate_username("USER1", existing) is True
    # Not a duplicate
    assert is_duplicate_username("user4", existing) is False
    # None or empty list
    assert is_duplicate_username("user1", None) is False
    assert is_duplicate_username("user1", []) is False 
